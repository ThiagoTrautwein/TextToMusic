from random import random
import rtmidi
from midiutil import MIDIFile
from note import Note
from instrument import Instrument
from music_controler import VolumeControler

class Text:
        
    def __init__(self):
        self.text = ''
        self.char = ''
        self.notes = ['A','B','C','D','E','F','G']
        self.text_lenght = 0
        self.myMIDI = MIDIFile(1)
        self.note = Note(self.out)
        self.instrument = Instrument(self.out)
        self.volume = VolumeControler(self.out)

    def GetText(self):
        return print(self.text)

    def GetLen(self):
        return self.text_lenght
    
    def SetText(self, text):
        self.text = text
        self.SetLen()
        self.ScanText()

    def SetLen(self):
        self.text_lenght = len(self.text)

    def ReadTextFromArchive(self, archive):
        with open(archive, 'r') as file:
            self.text = file.read()
            self.SetLen()
            self.ScanText()

    def GetCharWithLen(self, posicao):
        return self.text[posicao]

    def ScanText(self):
        for i in range(0, self.text_lenght):
            previous_char = self.char
            self.char = self.GetCharWithLen(i)
            if self.char == '+' or self.char == '-':
                if previous_char == 'R':
                    pass
                else:
                    self.CallFunctions(previous_char, i)
            else:
                self.CallFunctions(previous_char, i)

        with open("trabalhoFinal.mid", "wb") as output_file:
            self.MyMIDI.writeFile(output_file)

    def CallFunctions(self, caractere_anterior, i):
        print(self.char + ' + ' + caractere_anterior)
        #print(self.GetCharWithLen(i) + self.GetCharWithLen(i+1) + self.GetCharWithLen(i+2))
        match self.char:
            case ' ':
                pass
                #self.volume.StopSong()
            case 'A'|'B'|'C'|'D'|'E'|'F'|'G'|'a'|'b'|'c'|'d'|'e'|'f'|'g':
                #se char = B; checar próximos 3 caracteres para ver se é 'BPM+'
                self.note.ChangeNote(self.char, self.out) #
            case 'O'|'I'|'U'|'o'|'i'|'u':
                if caractere_anterior in ['A','B','C','D','E','F','G','a','b','c','d','e','f','g','?']:
                    self.note.RepeatNote(self.out)
                else:
                    self.instrument.SetInstrument(124, self.out)
            case '+':
                self.volume.DoubleVolume(self.out)
            case '-':
                self.volume.DefaultVolume(self.out)
            case '?':
                char =  'A' #'self.notes[random.randrange(0,6)]'
                self.note.ChangeNote(char, self.out) #
            case 'R':
                if self.GetCharWithLen(i+1)=='+':
                    self.note.RaiseOctave(self.out)
                elif self.GetCharWithLen(i+1)=='-':
                    self.note.LowerOctave(self.out)
            case '\n':
                self.instrument.SetInstrument(random.randrange(0,126), self.out)
            case ';':
                self.note.SetVelocity(random.randrange(30,140))
            case _:
                pass
        
        self.MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)