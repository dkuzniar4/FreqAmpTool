import soundfile as sf
import numpy as np
from Generator import Generator
from DSP import LowPassSinglePole
import plotly.graph_objects as go



class Analyzer:
    def __init__(self):
        self.lowPass = LowPassSinglePole()

    def loadFile(self, file_path):
        self.file_path = file_path
        self.inputData, self.sampleRate = sf.read(self.file_path)
        self.n_samples = len(self.inputData)
        self.time = self.n_samples / self.sampleRate
        
    def prepareFigure(self, fs, time, type, gainStep, startFreq, stopFreq, testTone):
        n_samples = int(fs * time)
        n_gainStep = int(1/gainStep)
        self.type = type
        timeTab = np.linspace(0, time, n_samples)
        self.gainTab = np.linspace(gainStep, 1.0, n_gainStep)
        c = (stopFreq - startFreq) / time
        k = (stopFreq/startFreq)**(1/time)

        # prepare freq axis
        if self.type == "exp":
            self.freqAxis = startFreq * (k**timeTab)
        elif self.type == "lin":
            self.freqAxis = (c * timeTab) + startFreq

        # cut signal
        corr = np.correlate(self.inputData[0:fs], testTone[0:fs], mode="full")
        maxIndex = np.argmax(corr) + 1 - fs

        firstSample = maxIndex if maxIndex >= 0 else 0
        self.inputData = self.inputData[firstSample:n_samples*n_gainStep+firstSample]

        self.figureData = np.reshape(self.inputData, (n_gainStep, n_samples))
        self.figureData = self.figureData.astype(np.float32)

        # low pass IIR 10 Hz
        self.lowPass.setParam(10, fs)

        for j in range(n_gainStep):
            for i in range(n_samples):
                self.figureData[j][i] *= (1.0 / self.gainTab[j]) / (2**15)
                self.figureData[j][i] = abs(self.figureData[j][i])
                self.figureData[j][i] = self.lowPass.filter(self.figureData[j][i])

    def showFigure(self):
        fig = go.Figure(data=[go.Surface(z=self.figureData, x=self.freqAxis, y=self.gainTab*100, colorscale='portland')])
        fig.update_scenes(xaxis_type="log")
        fig.update_layout(title="3D frequency characteristics", autosize=True,
            scene_aspectmode="cube", scene=dict(xaxis_title="frequency [Hz]", yaxis_title="gain [%]", zaxis_title="amplitude [ku]"))
        fig.show()
