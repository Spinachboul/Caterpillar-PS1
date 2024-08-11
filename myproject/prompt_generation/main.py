from gtts import gTTS
import os
import speech_recognition as sr
import nltk
from nltk.tokenize import word_tokenize
from fpdf import FPDF

# Define prompts for each section
prompts = {
    "header": [
        "Please provide the truck serial number.",
        "What is the truck model?",
        "Please provide the inspection ID.",
        "Who is the inspector?",
        "What is the inspection employee ID?",
        "When is the inspection date and time?",
        "Where is the location of the inspection?",
        "Please provide the geo coordinates of the inspection.",
        "What is the service meter hours reading?",
        "Please provide the inspector's signature.",
        "What is the customer or company name?",
        "What is the CAT customer ID?"
    ],
    "tires": [
        "What is the tire pressure for the left front tire?",
        "What is the tire pressure for the right front tire?",
        "What is the tire condition for the left front tire? (Good, Ok, Needs Replacement)",
        "What is the tire condition for the right front tire? (Good, Ok, Needs Replacement)",
        "What is the tire pressure for the left rear tire?",
        "What is the tire pressure for the right rear tire?",
        "What is the tire condition for the left rear tire? (Good, Ok, Needs Replacement)",
        "What is the tire condition for the right rear tire? (Good, Ok, Needs Replacement)",
        "Please provide an overall summary of the tires."
    ],
    "battery": [
        "What is the battery make?",
        "When was the battery replaced?",
        "What is the battery voltage?",
        "What is the battery water level? (Good, Ok, Low)",
        "Is there any damage to the battery? (Yes/No)",
        "Is there any leak or rust in the battery? (Yes/No)",
        "Please provide an overall summary of the battery."
    ],
    "exterior": [
        "Is there any rust, dent, or damage to the exterior? (Yes/No)",
        "If yes, please explain.",
        "Is there any oil leak in the suspension? (Yes/No)",
        "Please provide an overall summary of the exterior."
    ],
    "brakes": [
        "What is the brake fluid level? (Good, Ok, Low)",
        "What is the brake condition for the front? (Good, Ok, Needs Replacement)",
        "What is the brake condition for the rear? (Good, Ok, Needs Replacement)",
        "What is the condition of the emergency brake? (Good, Ok, Low)",
        "Please provide an overall summary of the brakes."
    ],
    "engine": [
        "Is there any rust, dent, or damage in the engine? (Yes/No)",
        "If yes, please explain.",
        "What is the condition of the engine oil? (Good/Bad)",
        "What is the color of the engine oil? (Clean/Brown/Black)",
        "What is the condition of the brake fluid? (Good/Bad)",
        "What is the color of the brake fluid? (Clean/Brown/Black)",
        "Is there any oil leak in the engine? (Yes/No)",
        "Please provide an overall summary of the engine."
    ],
    "voice_of_customer": [
        "Please provide any feedback from the customer."
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
    # Apply more NLP techniques if needed
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
