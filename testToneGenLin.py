from settings import *

print('TestToneGenerator')
print('Linear')
# f(t) = c*t + f0

print('Sampling frequency:', fs, 'Hz')
print('Number of samples:', sampleNum * gainStepNum)
print('Time length:', lengthTime * gainStepNum, 's')



chirpTab = np.sin(phi0 + 2 * np.pi * ((c * 0.5 * timeTab * timeTab) + startFreq * timeTab))

TestTone = np.array([])
for i in gainTab:
    temp = chirpTab * 0.99 * 2**15 * i
    TestTone = np.concatenate([TestTone, temp])

TestTone = np.asarray(TestTone, dtype=np.int16)

wavfile.write('TestToneGenLin.wav', fs, TestTone)
print('TestToneGenLin.wav was saved!')
