from google.cloud import texttospeech
import speech_recognition as sr
from bidi.algorithm import get_display
from arabic_reshaper import reshape
import os

def recognize_arabic_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please start speaking...")
        audio = r.listen(source)
    try:
        # Use the Google Speech Recognition API for Arabic
        text = r.recognize_google(audio, language='ar-AR')
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    except sr.RequestError:
        print("Sorry, I'm currently experiencing technical issues.")

# Example usage
recognized_text = recognize_arabic_speech()
reshaped_text = reshape(recognized_text)
display_text = get_display(reshaped_text)
print("Recognized text:")
print(display_text)

def convert_text_to_speech(text, output_file):
    client = texttospeech.TextToSpeechClient()
    
    # Set the desired voice parameters
    voice = texttospeech.VoiceSelectionParams(
        language_code='ar-AR',
        name='ar-XA-Standard-A',
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    # Set the audio parameters
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Synthesize speech
    synthesis_input = texttospeech.SynthesisInput(text=text)
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    # Save the audio response to a file
    with open(output_file, 'wb') as out_file:
        out_file.write(response.audio_content)

# Example usage
output_file = "output.mp3"
convert_text_to_speech(display_text, output_file)
os.system(f"start {output_file}")
