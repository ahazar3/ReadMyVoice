from App import WavRecorder


class App:
    def __init__(self):
        self.wr = WavRecorder.WavRecorder()

    def loop(self):
        self.wr.record(3)

    def main(self):
        self.loop()


def main():
    x = App()
    x.main()


if __name__ == "__main__": main()