import numpy as np
from scipy.io import wavfile

print('TestToneGenerator')
print('Exponential')
# f(t) = f0*(k^t)

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
print('Time length:',  * gainStepNum, 's')

timeTab = np.linspace(0, lengthTime, sampleNum)
gainTab = np.linspace(gainStep, 1.0, gainStepNum)

k = (stopFreq/startFreq)**(1/lengthTime)
phi0 = 0

chirpTab = np.sin(phi0 + 2 * np.pi * startFreq * ((k**timeTab - 1)/(np.log(k))))

TestTone = np.array([])
for i in gainTab:
    temp = chirpTab * 0.99 * 2**15 * i
    TestTone = np.concatenate([TestTone, temp])

TestTone = np.asarray(TestTone, dtype=np.int16)

wavfile.write('TestToneGenExp.wav', fs, TestTone)
print('TestToneGenExp.wav was saved!')
