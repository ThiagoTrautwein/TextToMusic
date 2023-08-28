from midiutil import MIDIFile
import rtmidi
import time

class MusicControler():
    ## valor da nota em inteiro
    ## Range: 0-127
    # C = [0,12,24,36,48,60,72,84,96,108,120]
    # Csharp = [1,13,25,37,49,61,73,85,97,109,121]
    # D = [2,14,26,38,50,62,74,86,98,110,122]
    # Dsharp = [3,15,27,39,51,63,75,87,99,111,123]
    # E = [4,16,28,40,52,64,76,88,100,112,124]
    # F = [5,17,29,41,53,65,77,89,101,113,125]
    # Fsharp = [6,18,30,42,54,66,78,90,102,114,126]
    # G = [7,19,31,43,55,67,79,91,103,115,127]
    # Gsharp = [8,20,32,44,56,68,80,92,104,116]
    # A = [9,21,33,45,57,69,81,93,105,117]
    # Asharp = [10,22,34,46,58,70,82,94,106,118]
    # B = [11,23,35,47,59,71,83,95,107,119]
    defaultVolume = 30
    defaultTempo = 60
    defaultOctave = 3
    
    noteDuration = 3
    
    def __init__(self):
        #super.__init__(self,1)
        self.track = 0
        self.channel = 0
        self.note = 0
        self.octave = self.defaultOctave
        self.time = 0
        self.duration = self.noteDuration
        self.tempo = self.defaultTempo
        self.volume = self.defaultVolume
        self.MIDI = MIDIFile(1)
        self.out = rtmidi.MidiOut()
        self.out.open_port(0)

    def GetVolume (self):
        return self.volume
    
    def GetNote (self):
        return self.note

    def GetOctave(self):
        return self.octave

    def GetTime(self):
        return self.time

    def GetTempo(self):
        return self.tempo
    
    def SetVolume (self, volume):
        self.volume = volume
        self.out.send_message([0xB4, 0x07, volume])
    
    def SetNote (self, note):
        self.note = note
    
    def SetOctave (self, octave):
        self.octave = octave

    def SetTime (self, time):
        self.time = time

    def SetTempo (self, tempo):
        self.tempo = tempo
        self.MIDI.addTempo(0, self.GetTime(), self.GetTempo())

    def SetInstrument (self, instrument):
        print("instrumento  "+ str(instrument))
        self.out.send_message([0xC4, instrument])
        self.MIDI.addProgramChange(0, 0, self.GetTime(), instrument)

    def DoubleVolume (self):
        volume = self.GetVolume() * 2
        self.SetVolume(volume)

    def DefaultVolume (self):
        self.SetVolume(self.defaultVolume)

    def RaiseOctave (self):
        if self.GetOctave() == 10:
            self.DefaultOctave()
        else:
            self.SetOctave(self.GetOctave() + 1)

    def LowerOctave (self):
        if self.GetOctave() == 0:
            self.DefaultOctave()
        else:
            self.SetOctave(self.GetOctave() - 1)

    def DefaultOctave (self):
        self.SetOctave(self.octave_default)

    def RaiseTempo (self, bpm):
        tempo = self.tempo + bpm
        self.SetTempo(tempo)



    def PlayNote(self):
        note = self.GetNote() + self.GetOctave() * 12
        self.MIDI.addNote(self.track, self.channel, note, self.time, self.duration, self.volume)
        self.SetTime(self.GetTime() + self.noteDuration)
        self.out.send_message([0x94, note, self.GetVolume()])
        time.sleep(1.0)
        self.out.send_message([0x84, note, 0])
        time.sleep(0.1)
        
    def RepeatNote(self):
        self.PlayNote()
        
    def SilentNote(self):
        self.MIDI.addNote(self.track, self.channel, 0, self.time, self.duration, 0)
        self.SetTime(self.GetTime() + self.noteDuration)
        self.out.send_message([0x84, 0, 0])
        time.sleep(1.0)

    def ChangeNote(self, caractere):
        match caractere:
            case 'A' | 'a':
                note = 9
            case 'B' | 'b':
                note = 11
            case 'C' | 'c':
                note = 0
            case 'D' | 'd':
                note = 2
            case 'E' | 'e':
                note = 4
            case 'F' | 'f':
                note = 5
            case 'G' | 'g':
                note = 7
        self.SetNote(note)
        self.PlayNote()            

    def writeFile(self):
        with open("trabalhoFinal.mid", "wb") as output_file:
            self.MIDI.writeFile(output_file)