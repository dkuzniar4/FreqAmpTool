from settings import *

print('TestToneGenerator')
print('Exponential')
# f(t) = f0*(k^t)

print('Sampling frequency:', fs, 'Hz')
print('Number of samples:', sampleNum * gainStepNum)
print('Time length:', lengthTime * gainStepNum, 's')



chirpTab = np.sin(phi0 + 2 * np.pi * startFreq * ((k**timeTab - 1)/(np.log(k))))

TestTone = np.array([])
for i in gainTab:
    temp = chirpTab * 0.99 * 2**15 * i
    TestTone = np.concatenate([TestTone, temp])

TestTone = np.asarray(TestTone, dtype=np.int16)

wavfile.write('TestToneGenExp.wav', fs, TestTone)
print('TestToneGenExp.wav was saved!')
