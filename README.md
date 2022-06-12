# FreqAmpTool
Tool for creating multidimensional frequency characteristics

Before use this tool you should install dependencies:

plotly, numpy, scipy

1. For first you should edit file settings.py as you prefer:

   \# Settings

   \# --------------------------------------------------

   \# start frequency [Hz]

   startFreq = 100

   \# stop frequency [Hz]

   stopFreq = 20000

   \# sampling frequency [Hz]

   fs = 44100

   \# length time (for one amp measure) [s]

   lengthTime = 1.0

   \# step for amplitude gain [0 < gainStep < 1.0] 

   gainStep = 0.05

   \# start phase in [rad]

   phi0 = 0

   \# test tone type 'exp' or 'lin'

   testToneType = 'exp'

   \# --------------------------------------------------

2. Next step is generation of test tone:

   Depend of choosen test tone type run

   python testToneGenExp.py

   or

   python testToneGenLin.py

3. Pass test tone through the DUT (e.g. guitar amp) and record it.

4. Prepare test tone output by cut signal to the same length like original test tone

   You can use Audacity to do it

   ![alt](<Docs/Images/audacityCut.png>)

   Save it in the same format.

5. Run FreqAmpTool <"wav file"> to plot 3d surface figure with Frequency characteristics depends of signal amplitude

   e.g.

   python FreqAmpTool.py Output.wav

   then you should see 3D surface plot in you browser.

   ![alt](<Docs/Images/3dFig.png>)

   todo:

   - add labels to axes
   - change amplitude scale to dB
   - ...
   
      
   
      
   
   

