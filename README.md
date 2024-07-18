# FreqAmpTool
Tool for creating 3D frequency characteristics vs gain

Before use this tool you should install dependencies:

plotly, numpy, soundfile

1. In GUI you can set measurements parameters:

   Sampling frequency

   Time duration (of test tone)

   Type of test tone

   Gain step

   Start frequency

   Stop frequency

   \# --------------------------------------------------

2. Next step is generation of test tone:

   Click "Save params"  button and then click "Generate test tone" to save test tone to wav file.

3. Pass test tone through the DUT (e.g. guitar amp) and record it.

4. Prepare test tone output by cut signal to the same length or slightly longer like original test tone

   You can use Audacity to do it

   ![alt](<Docs/Images/audacityCut.png>)

   Export processed signal to wav file.

5. Load processed wav file by clicking "Load wav file" button.

6. Click "Show figure" to see 3D surface plot in you browser.

   ![alt](<Docs/Images/3dFig.png>)

   todo:

   - change amplitude scale to dB

   - ...

      

      

   

