from midiutil import MIDIFile
import rtmidi
import time
from instrument import Instrument

# Controla volume, notas e tempo
class MusicControler():
    ## valor da nota em inteiro
    ## Range: 0-127
    # C =       [0,12,24,36,48,60,72,84,96,108,120]
    # Csharp =  [1,13,25,37,49,61,73,85,97,109,121]
    # D =       [2,14,26,38,50,62,74,86,98,110,122]
    # Dsharp =  [3,15,27,39,51,63,75,87,99,111,123]
    # E =       [4,16,28,40,52,64,76,88,100,112,124]
    # F =       [5,17,29,41,53,65,77,89,101,113,125]
    # Fsharp =  [6,18,30,42,54,66,78,90,102,114,126]
    # G =       [7,19,31,43,55,67,79,91,103,115,127]
    # Gsharp =  [8,20,32,44,56,68,80,92,104,116]
    # A =       [9,21,33,45,57,69,81,93,105,117]
    # Asharp =  [10,22,34,46,58,70,82,94,106,118]
    # B =       [11,23,35,47,59,71,83,95,107,119]
    defaultVolume = 30
    defaultTempo = 60
    defaultOctave = 3    
    noteDuration = 3
    
    def __init__(self):
        self.track = 0
        self.channel = 0
        self.note = 0 
        self.octave = self.defaultOctave
        self.time = 3       #tempo em segundos que a nota deve ser tocada (rtmidi)
        self.note_time = 0  #beat de inicio da gravação da nota no arquivo (MIDIutil)
        self.duration = self.noteDuration   #beats por nota para ser ultilizado na gravação no arquivo (MIDIutil)
        self.tempo = self.defaultTempo      #BPM, usado no arquivo e para calcular o self.time quando BPM é alterado
        self.volume = self.defaultVolume
        self.MIDI = MIDIFile(1)
        self.out = rtmidi.MidiOut()
        self.out.open_port(0)
        self.instrument = Instrument()

    def __GetVolume (self):
        return self.volume
    
    def __GetNote (self):
        return self.note

    def __GetOctave(self):
        return self.octave

    def __GetTime(self):
        return self.time

    def __GetNoteTime(self):
        return self.note_time

    def __GetTempo(self):
        return self.tempo
    
    def __SetVolume (self, volume):
        print ("Volume: " + str(volume))
        self.volume = volume
        self.out.send_message([0xB4, 0x07, volume])
    
    def __SetNote (self, note):
        self.note = note
    
    def __SetOctave (self, octave):
        self.octave = octave

    def __SetTime(self, time):
        self.time = time

    def __SetNoteTime(self, note_time):
        self.note_time = note_time

    def __SetTempo(self, tempo):
        self.tempo = tempo
        duracao_nota = 3 * (60 / tempo)
        self.__SetTime(duracao_nota)
        self.MIDI.addTempo(0, self.__GetNoteTime(), tempo)



    def DoubleVolume(self):
        if (self.__GetVolume() < 64):
            volume = self.__GetVolume() * 2
            self.__SetVolume(volume)
        else:
            self.__SetVolume(self.__GetVolume())

    def DefaultVolume(self):
        self.__SetVolume(self.defaultVolume)

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
        self.__SetNote(note)
        self.PlayNote()   

    def RaiseOctave(self):
        if self.__GetOctave() == 10:
            self.DefaultOctave()
        else:
            self.__SetOctave(self.__GetOctave() + 1)

    def LowerOctave(self):
        if self.__GetOctave() == 0:
            self.DefaultOctave()
        else:
            self.__SetOctave(self.__GetOctave() - 1)

    def DefaultOctave(self):
        self.__SetOctave(self.defaultOctave)

    def ChangeTempo(self, tempo):
        print("BPM: " + str(tempo))
        self.__SetTempo(tempo)

    def RaiseTempo(self, bpm):
        tempo = self.__GetTempo() + bpm
        print("BPM: " + str(tempo))
        self.__SetTempo(tempo)



    def ChangeInstrument(self, instrument):
        self.instrument.ChangeInstrument (instrument, self.__GetNoteTime(), self.out, self.MIDI)



    def PlayNote(self):
        note = self.__GetNote() + self.__GetOctave() * 12
        self.MIDI.addNote(self.track, self.channel, note, self.__GetNoteTime(), self.duration, self.volume)
        self.__SetNoteTime(self.__GetNoteTime() + self.noteDuration)
        self.out.send_message([0x94, note, self.__GetVolume()])
        time.sleep(self.__GetTime())
        self.out.send_message([0x84, note, 0])
        time.sleep(0.01)
        
    def RepeatNote(self):
        self.PlayNote()
        
    def SilentNote(self):
        self.MIDI.addNote(self.track, self.channel, 0, self.__GetNoteTime(), self.duration, 0)
        self.__SetNoteTime(self.__GetNoteTime() + self.noteDuration)
        self.out.send_message([0x84, 0, 0])
        time.sleep(self.__GetTime())
       


    def writeFile(self):
        with open("trabalhoFinal.mid", "wb") as output_file:
            self.MIDI.writeFile(output_file)