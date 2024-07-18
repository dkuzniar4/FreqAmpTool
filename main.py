import tkinter as tk
from tkinter import filedialog
from Analyzer import Analyzer
from Generator import Generator


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.gen = Generator()
        self.an = Analyzer()
        self.createGUI()

    def createGUI(self):
        self.title("FreqAmpTool")
        self.geometry("350x600")
        self.resizable(False, False)

        self.an = Analyzer()

        # Generator section
        self.GenLabel = tk.Label(self, text="Parameters", bg="black", fg="white")
        self.GenLabel.place(x=10, y=20)

        # fs
        self.fsLabel = tk.Label(self, text="Sampling frequency [Hz]")
        self.fsLabel.place(x=10, y=50)

        self.fsEntry = tk.Entry(self, width=15)
        self.fsEntry.insert(0, "48000")
        self.fsEntry.place(x=200, y=50)

        # time duration
        self.timeLabel = tk.Label(self, text="Time duration [s]")
        self.timeLabel.place(x=10, y=80)

        self.timeEntry = tk.Entry(self, width=15)
        self.timeEntry.insert(0, "1")
        self.timeEntry.place(x=200, y=80)

        # type (exp, lin)
        self.typeLabel = tk.Label(self, text="Type")
        self.typeLabel.place(x=10, y=110)
        self.typeVar = tk.StringVar(value="exp")
        self.typeRadio1 = tk.Radiobutton(text="exp", variable=self.typeVar, value="exp")
        self.typeRadio1.place(x=200, y=110)
        self.typeRadio2 = tk.Radiobutton(text="lin", variable=self.typeVar, value="lin")
        self.typeRadio2.place(x=270, y=110)

        # gainStep [0.01 - 1]
        self.gainLabel = tk.Label(self, text="gain step [0.01 - 1]")
        self.gainLabel.place(x=10, y=140)

        self.gainEntry = tk.Entry(self, width=15)
        self.gainEntry.insert(0, "0.05")
        self.gainEntry.place(x=200, y=140)

        # startFreq
        self.startFreqLabel = tk.Label(self, text="start freq [Hz]")
        self.startFreqLabel.place(x=10, y=170)

        self.startFreqEntry = tk.Entry(self, width=15)
        self.startFreqEntry.insert(0, "100")
        self.startFreqEntry.place(x=200, y=170)

        # stopFreq
        self.stopFreqLabel = tk.Label(self, text="stop freq [Hz]")
        self.stopFreqLabel.place(x=10, y=200)

        self.stopFreqEntry = tk.Entry(self, width=15)
        self.stopFreqEntry.insert(0, "20000")
        self.stopFreqEntry.place(x=200, y=200)

        # save params
        self.SaveButton = tk.Button(self, text="Save params", bg="green", fg="white", command=self.setParams)
        self.SaveButton.place(x= 10, y=250)
        self.setParams()

        # generate button
        self.generateButton = tk.Button(self, text="Generate test tone", bg="green", fg="white", command=self.chooseFileToSave)
        self.generateButton.place(x=150, y=250)

        # Load input file
        self.LoadLabel = tk.Label(self, text="Load processed wav file", bg="black", fg="white")
        self.LoadLabel.place(x=10, y=330)

        self.loadFileButton = tk.Button(self, text="Load wav file", bg="green", fg="white", command=self.chooseFileToLoad)
        self.loadFileButton.place(x=10, y=360)
        
        self.fileInfoText = tk.Text(self, height=4, width=30)
        self.fileInfoText.place(x=10, y=400)

        # Graph section
        self.FigLabel = tk.Label(self, text = "3D figure", bg="black", fg="white")
        self.FigLabel.place(x=10, y=500)

        self.showFigureButton = tk.Button(self, text="Show figure", bg="green", fg="white", command=self.showFigure)
        self.showFigureButton.place(x=10, y=530)



    def chooseFileToLoad(self):
        file_path = filedialog.askopenfilename(
            title="Load WAV file",
            filetypes=(("Wav files", "*.wav"),)
        )
        # Open file
        self.an.loadFile(file_path)
        self.fileInfoText.delete("1.0", tk.END)
        self.fileInfoText.insert(tk.END,
        f"Sample rate: {self.an.sampleRate} Hz\n"
        f"Time duration: {self.an.time} s\n"
        f"Number of samples: {self.an.n_samples}")

    def chooseFileToSave(self):
        file_path = filedialog.asksaveasfilename(
            title="Save testTone",
            filetypes=(("Wav files", "*.wav"),)
        )

        
        self.gen.saveFile(file_path, self.fs)

    def setParams(self):
        self.fs = int(self.fsEntry.get())
        self.time = int(self.timeEntry.get())
        self.type = str(self.typeVar.get())
        self.gainStep = float(self.gainEntry.get())
        self.startFreq = int(self.startFreqEntry.get())
        self.stopFreq = int(self.stopFreqEntry.get())
        self.testTone = self.gen.generateTestTone(self.fs, self.time, self.type, self.gainStep, self.startFreq, self.stopFreq)

    def showFigure(self):
        self.an.prepareFigure(self.fs, self.time, self.type, self.gainStep, self.startFreq, self.stopFreq, self.testTone)
        self.an.showFigure()



if __name__ == "__main__":
    app = App()
    app.mainloop()
