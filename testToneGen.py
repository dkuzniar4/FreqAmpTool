from settings import *

print('TestToneGenerator')
print('Exponential')
# f(t) = f0*(k^t)

print('Sampling frequency:', fs, 'Hz')
print('Number of samples:', sampleNum * gainStepNum)
print('Time length:', lengthTime * gainStepNum, 's')

if testToneType == 'exp':
    chirpTab = np.sin(phi0 + 2 * np.pi * startFreq * ((k**timeTab - 1)/(np.log(k))))
elif testToneType == 'lin':
    chirpTab = np.sin(phi0 + 2 * np.pi * ((c * 0.5 * timeTab * timeTab) + startFreq * timeTab))

TestTone = np.array([])
for i in gainTab:
    temp = chirpTab * 0.99 * 2**15 * i
    TestTone = np.concatenate([TestTone, temp])

TestTone = np.asarray(TestTone, dtype=np.int16)

wavfile.write('TestTone.wav', fs, TestTone)
print('TestTone.wav was saved!')
