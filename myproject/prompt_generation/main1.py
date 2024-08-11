from gtts import gTTS
import os
import speech_recognition as sr
import nltk
from nltk.tokenize import word_tokenize
from fpdf import FPDF

# Define prompts for testing with only 3 questions
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
    # Play the audio on the system
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

nltk.download('punkt')

# Function to process text with NLP
def process_text(text):
    tokens = word_tokenize(text)
    # Can apply more nlp techniques
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

# Main function
def main():
    data = {}  # Dictionary to store responses
    for section, questions in prompts.items():
        for question in questions:
            text_to_speech(question, "prompt.mp3")
            print("Listening...")
            response_text = speech_to_text()
            print(f"Response: {response_text}")
            # Process the response with NLP if needed
            data[question] = response_text
    
    create_pdf(data)
    # Cleanup temporary files
    if os.path.exists("prompt.mp3"):
        os.remove("prompt.mp3")

if __name__ == "__main__":
    main()
