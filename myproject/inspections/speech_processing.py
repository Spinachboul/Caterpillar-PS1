import os
import speech_recognition as sr
from gtts import gTTS
from nltk.tokenize import word_tokenize
from fpdf import FPDF
import nltk

nltk.download('punkt')

# Define prompts for the inspection
prompts = {
    "header": [
        "Please provide the truck serial number.",
        "What is the truck model?",
        "Please provide the inspection ID."
    ]
}

# Function to convert text to speech
def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    os.system(f"start {filename}")  # For Windows
    # os.system(f"afplay {filename}")  # For macOS
    # os.system(f"mpg321 {filename}")  # For Linux

# Function to convert speech to text
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak now...")
        audio = r.listen(source)
        print("Recognizing...")
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand you. Please try again.")
            return ""
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
            return ""

# Function to process text with NLP
def process_text(text):
    tokens = word_tokenize(text)
    return tokens

# PDF generation class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Inspection Report', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_section(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)

# Function to create PDF from collected data
def create_pdf(data):
    pdf = PDF()
    pdf.add_page()
    
    for section, questions in prompts.items():
        body = "\n".join([f"{question} {data.get(question, '')}" for question in questions])
        pdf.add_section(section.upper(), body)
    
    pdf_output_path = "inspection_report.pdf"
    pdf.output(pdf_output_path)

    print(f"PDF created: {pdf_output_path}")
    return pdf_output_path

def run_inspection():
    data = {}  # Dictionary to store responses
    for section, questions in prompts.items():
        for question in questions:
            text_to_speech(question, "prompt.mp3")
            response_text = speech_to_text()
            data[question] = response_text
    
    pdf_path = create_pdf(data)
    if os.path.exists("prompt.mp3"):
        os.remove("prompt.mp3")
    
    return pdf_path
