import pyaudio
import wave


class WavRecorder:

    def __init__(self):
        self.chunk_size = 1024
        self.format = pyaudio.paInt16
        self.channels = 2
        self.rate = 44100
        self.p = pyaudio.PyAudio()
        self.filename = 'output.wav'

    def record(self, seconds):

        stream = self.p.open(format=self.format,
                             channels=self.channels,
                             rate=self.rate,
                             input=True,
                             frames_per_buffer=self.chunk_size)

        print("Recording...")

        frames = []

        for i in range(0, int(self.rate/self.chunk_size*seconds)):
            data = stream.read(self.chunk_size)
            frames.append(data)

        print("Done recording")

        # close stream
        stream.stop_stream()
        stream.close()

        # terminate py audio
        self.p.terminate()

        # save to wave
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()
