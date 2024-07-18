import numpy as np
import soundfile as sf

class Generator:
    def __init__(self):
        pass

    def generateTestTone(self, fs, time, type, gainStep, startFreq, stopFreq):
        n_samples = int(fs * time)
        n_gainStep = int(1/gainStep)
        timeTab = np.linspace(0, time, n_samples)
        gainTab = np.linspace(gainStep, 1.0, n_gainStep)
        c = (stopFreq - startFreq) / time
        k = (stopFreq/startFreq)**(1/time)

        if type == "exp":
            freqAxis = startFreq * (k**timeTab)
            chirpTab = np.sin(2 * np.pi * startFreq * ((k**timeTab - 1)/(np.log(k))))
        elif type == "lin":
            freqAxis = (c * timeTab) + startFreq
            chirpTab = np.sin(2 * np.pi * ((c * 0.5 * timeTab**2) + startFreq * timeTab))

        self.testTone = np.array([])
        for i in gainTab:
            temp = chirpTab * 0.99 * 2**15 * i
            self.testTone = np.concatenate([self.testTone, temp])

        self.testTone = np.asarray(self.testTone, dtype=np.int16)

        return self.testTone

    def saveFile(self, file_path, fs):
        self.file_path = file_path
        sf.write(file_path, self.testTone, fs)
