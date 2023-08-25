from midiutil import MIDIFile
from instrument import Instrument


class MusicControler():
    ## valor da nota em inteiro
    ## Range: 0-127
    velocity_default = 100
    octave_default = 3
    C = [0,12,24,36,48,60,72,84,96,108,120]
    # Csharp = [1,13,25,37,49,61,73,85,97,109,121]
    D = [2,14,26,38,50,62,74,86,98,110,122]
    # Dsharp = [3,15,27,39,51,63,75,87,99,111,123]
    E = [4,16,28,40,52,64,76,88,100,112,124]
    F = [5,17,29,41,53,65,77,89,101,113,125]
    # Fsharp = [6,18,30,42,54,66,78,90,102,114,126]
    G = [7,19,31,43,55,67,79,91,103,115,127]
    # Gsharp = [8,20,32,44,56,68,80,92,104,116]
    A = [9,21,33,45,57,69,81,93,105,117]
    # Asharp = [10,22,34,46,58,70,82,94,106,118]
    B = [11,23,35,47,59,71,83,95,107,119]
    defaultVolume = 30
    
    
    def __init__(self):
        #super.__init__(self,1)
        self.note = 0
        self.track = 0
        self.channel = 0
        #nota
        self.note = 0
        #octave
        self.octave = 3
        self.time = 0
        self.duration = 1
        self.tempo = 60
        self.volume = self.defaultVolume
        self.MIDI = MIDIFile(1)
        self.instrument = Instrument()

    def GetVolume (self):
        return self.volume
    
    def GetNote (self):
        return self.note

    def GetOctave(self):
        return self.octave

    def GetVelocity(self):
        return self.velocity

    def SetVolume (self, volume):
        self.volume = volume
    
    def SetNote (self, note):
        self.note = note
    
    def SetOctave (self, octave):
        self.octave = octave

    def SetVelocity (self, velocity):
        self.velocity = velocity

    def DoubleVolume (self):
        volume = self.GetVolume() * 2
        self.SetVolume(volume)

    def DefaultVolume (self):
        self.SetVolume(self.defaultVolume)

    def PlayNote(self):
        note = self.GetNote() + self.GetOctave() * 12
        self.MIDI.addNote(self.track, self.channel, note, self.time, self.duration, self.volume)
        
    def RepeatNote(self, out):
        self.SetNote(self.note, out)
        
    def SilenceNote(self):
        self.MIDI.addNote(self.track, self.channel, 0, self.time, self.duration, 0)

    def ChangeNote(self, caractere):
        match caractere:
            case 'A' | 'a':
                note = self.A[self.GetOctave()]
            case 'B' | 'b':
                note = self.B[self.GetOctave()]
            case 'C' | 'c':
                note = self.C[self.GetOctave()]
            case 'D' | 'd':
                note = self.D[self.GetOctave()]
            case 'E' | 'e':
                note = self.E[self.GetOctave()]
            case 'F' | 'f':
                note = self.F[self.GetOctave()]
            case 'G' | 'g':
                note = self.G[self.GetOctave()]
        self.SetNote(note)            

    def RaiseOctave (self, out):
        self.SilenceNote(out)
        if self.GetOctave() == 10:
            self.DefaultOctave()
        else:
            self.SetOctave(self.GetOctave() + 1)
        self.PlayNote(out)

    def LowerOctave (self, out):
        self.SilenceNote(out)
        if self.GetOctave() == 0:
            self.DefaultOctave()
        else:
            self.SetOctave(self.GetOctave() - 1)
        self.PlayNote(out)

    def DefaultOctave (self):
        self.SetOctave(self.octave_default)

    def writeFile(self):
        with open("trabalhoFinal.mid", "wb") as output_file:
            self.MIDI.writeFile(output_file)

    def SetInstrument (self, instrument):
        self.MIDI.addProgramChange(0, 0, 3.0, instrument)

