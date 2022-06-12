from settings import *
import sys
import plotly.graph_objects as go
import math

fileName = str(sys.argv[1])

# Low pass IIR filter
# ---------------------------------------------------------
freqCut = startFreq
fc = freqCut / fs
decay = math.exp(-2 * math.pi * fc)

class LowPassSinglePole:
    def __init__(self, decay):
        self.b = 1 - decay
        self.reset()
    def reset(self):
        self.y = 0
    def filter(self, x):
        self.y += self.b * (x - self.y)
        return self.y

low_pass_single_pole = LowPassSinglePole(decay)
# ---------------------------------------------------------


# load wav file
sampleRate, Signal = wavfile.read(fileName)
# extract only first column (one channel)
Signal = Signal[:,[0]]

# reshape Signal to separate characteristics
SignalOut = np.reshape(Signal, (gainStepNum,sampleNum))
# cast int to float
SignalOut = SignalOut.astype(np.float32)

for j in range(gainStepNum):
    for i in range(sampleNum):
        # normalisation of amplitude 
        SignalOut[j][i] = SignalOut[j][i] * (1.0 / gainTab[j]) / (2**15)
        # absolute value
        SignalOut[j][i] = abs(SignalOut[j][i])
        # low pass filter
        SignalOut[j][i] = low_pass_single_pole.filter(SignalOut[j][i])

# Assign proper axix type
if testToneType == 'exp':
    axisType = freqAxisExp
elif testToneType == 'lin':
    axisType = freqAxisExp

# plot 3d surface figure
fig = go.Figure(data=[go.Surface(z=SignalOut, x=axisType, y=gainTab)])
fig.update_scenes(xaxis_type="log")
fig.show()
