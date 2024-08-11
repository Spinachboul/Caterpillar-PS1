from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
from django.conf import settings
from PIL import Image
import numpy as np
import os
from django.http import JsonResponse, HttpResponse
import speech_recognition as sr
from gtts import gTTS
from fpdf import FPDF
from .models import InspectionResult
import cv2

class ImageAugmentView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        # Get the image from the request
        image_file = request.FILES['image']
        image = Image.open(image_file)
        
        # Convert the image to a format that OpenCV can work with
        image_np = np.array(image)
        image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
        
        # Perform image enhancement (example: converting to grayscale)
        enhanced_image_cv = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
        
        # Convert back to a format that can be sent to the frontend
        _, buffer = cv2.imencode('.png', enhanced_image_cv)
        enhanced_image = buffer.tobytes()
        
        # Send the enhanced image back to the frontend
        return HttpResponse(enhanced_image, content_type='image/png')

class SpeechToTextPDFView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        prompts = {
            "header": [
                "Please provide the truck serial number.",
                "What is the truck model?",
                "Please provide the inspection ID."
            ]
        }
        
        recognizer = sr.Recognizer()
        data = {}

        for section, questions in prompts.items():
            for question in questions:
                # Convert text to speech
                tts = gTTS(text=question, lang='en')
                tts.save("prompt.mp3")
                os.system(f"start prompt.mp3")  # Windows

                # Convert speech to text
                with sr.Microphone() as source:
                    print("Please speak now...")
                    audio = recognizer.listen(source)
                    try:
                        response_text = recognizer.recognize_google(audio)
                        print(f"You said: {response_text}")
                        data[question] = response_text

                        # Save the result in the database
                        InspectionResult.objects.create(
                            section=section,
                            text_result=response_text
                        )
                    except sr.UnknownValueError:
                        return Response({'error': 'Speech not understood'}, status=400)
                    except sr.RequestError as e:
                        return Response({'error': f'Request error: {str(e)}'}, status=500)
                    finally:
                        if os.path.exists("prompt.mp3"):
                            os.remove("prompt.mp3")

        # Generate PDF after capturing data
        pdf_path = self.create_pdf(data)
        return Response({'results': data, 'pdf_url': pdf_path})

    def create_pdf(self, data):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, 'Inspection Report', 0, 1, 'C')

        for section, text in data.items():
            pdf.add_page()
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(0, 10, section, 0, 1, 'L')
            pdf.ln(4)
            pdf.set_font('Arial', '', 12)
            pdf.multi_cell(0, 10, text)
            pdf.ln()

        pdf_output_path = os.path.join(settings.MEDIA_ROOT, "inspection_report.pdf")
        pdf.output(pdf_output_path)

        return f'/media/inspection_report.pdf'

class NoiseCancellationView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        audio = request.FILES.get('audio')
        if not audio:
            return Response({'error': 'No audio provided'}, status=400)

        buzzwords = ['example', 'buzzword']
        return Response({'buzzwords': buzzwords})
