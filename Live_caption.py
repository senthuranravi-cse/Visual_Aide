import concurrent.futures
import speech_recognition as sr
import time
import logging
#kirthi and Senthuran
def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(levelname)s - %(message)s")

    def listen(mic, id):
        logging.debug(f"Listening... {id}")
        with mic as source:
            audio = r.listen(source, timeout=10, phrase_time_limit=5)
            return audio


    def transcribe(audio):
        logging.debug(f"transcribing...")
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            print("\r...")

    r = sr.Recognizer()
    r.pause_threshold = 2

    mic = sr.Microphone(device_index=1)
    while True:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            listener = executor.submit(listen, mic, 1)
            subtitles = executor.submit(transcribe, listener.result())
            print(subtitles)
            logging.info(subtitles.result())