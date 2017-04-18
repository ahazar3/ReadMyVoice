import speech_recognition
import os
import serial

class App:
    def __init__(self):

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getcwd() + "\ReadMyVoice.json"

        # self.ser = serial.Serial()
        self.recognizer = speech_recognition.Recognizer()
        self.recognizer.dynamic_energy_threshold = True
        self.iterations = 0

    def loop(self):
        with speech_recognition.Microphone() as microphone:
            # do level check every five iterations
            if self.iterations % 5 == 0:
                print("Adjusting for ambient noise...\n")
                self.recognizer.adjust_for_ambient_noise(source=microphone, duration=2)

            # capture audio
            print("Speak now!")
            audio = self.recognizer.record(microphone, duration=5, offset=None)

            # recognize audio
            print("I heard you! Recognizing...\n")
            try:
                transcription = self.recognizer.recognize_google_cloud(
                                                                    audio,
                                                                    credentials_json=None,
                                                                    language='en-US',
                                                                    preferred_phrases=None,
                                                                    show_all=False)
            except speech_recognition.UnknownValueError:
                print("Couldn't understand you, sorry\n")
                return
            '''
            except speech_recognition.RequestError:
                print("Couldn't connect to Google... hmm\n")
                return
            '''
            print("You said \"" + transcription + "\"\n")
            self.iterations += 1

    def main(self):
        while True:
            self.loop()


def main():
    x = App()
    x.main()

if __name__ == "__main__":
    main()
