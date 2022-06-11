import numpy as np
from scipy.io import wavfile

print('TestToneGenerator')
print('Linear')

startFreq = 100
stopFreq = 20000
fs = 44100
ts = 1/fs
lengthTime = 1.0
sampleNum = int(fs * lengthTime)
gainStep = 0.05
gainStepNum = int(1.0/gainStep)

print('Sampling frequency:', fs, 'Hz')
print('Number of samples:', sampleNum * gainStepNum)
print('Time length:', lengthTime * gainStepNum, 's')

timeTab = np.linspace(0, lengthTime, sampleNum)
freqTab = np.linspace(startFreq, stopFreq, sampleNum)
gainTab = np.linspace(gainStep, 1.0, gainStepNum)

c = (stopFreq - startFreq) / lengthTime
phi0 = 0

chirpTab = np.sin(phi0 + 2 * np.pi * ((c * 0.5 * timeTab * timeTab) + startFreq * timeTab))

TestTone = np.array([])
for i in gainTab:
    temp = chirpTab * 0.99 * 2**15 * i
    TestTone = np.concatenate([TestTone, temp])

TestTone = np.asarray(TestTone, dtype=np.int16)

wavfile.write('TestToneGenLin.wav', fs, TestTone)
print('TestToneGenLin.wav was saved!')
