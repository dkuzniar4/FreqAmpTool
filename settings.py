import numpy as np
from scipy.io import wavfile
# Settings
# --------------------------------------------------
# start frequency [Hz]
startFreq = 100
# stop frequency [Hz]
stopFreq = 20000
# sampling frequency [Hz]
fs = 44100
# length time (for one amp measure) [s]
lengthTime = 1.0
# step for amplitude gain [0 < gainStep < 1.0] 
gainStep = 0.05
# start phase in [rad]
phi0 = 0
# test tone type 'exp' or 'lin'
testToneType = 'exp'
# --------------------------------------------------

# Common variables
ts = 1/fs
sampleNum = int(fs * lengthTime)
gainStepNum = int(1.0/gainStep)
timeTab = np.linspace(0, lengthTime, sampleNum)
gainTab = np.linspace(gainStep, 1.0, gainStepNum)
c = (stopFreq - startFreq) / lengthTime
k = (stopFreq/startFreq)**(1/lengthTime)

# Calculate frequency axis
# Linear 
# f(t) = c*t + f0
freqAxisLin = (c * timeTab) + startFreq
# Exponential
# f(t) = f0*(k^t)
freqAxisExp = startFreq * (k**timeTab)

