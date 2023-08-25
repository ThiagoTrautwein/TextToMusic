from random import random
import rtmidi
from note import Note
from instrument import Instrument
from music_controler import VolumeControler

class Text:
        
    def __init__(self, texto):
        self.text = texto
        self.char = ''
        self.notes = ['A','B','C','D','E','F','G']
        self.text_length = len(texto)
        self.out = rtmidi.MidiOut()
        self.out.open_port(0)
        self.note = Note(36, self.out)
        self.instrument = Instrument(self.out)
        self.volume = VolumeControler(self.out)

    def GetText(self):
        return print(self.text)

    def GetLen(self):
        return self.text_length
    
    def GetCharWithLen(self, posicao):
        return self.text[posicao]

    def ScanText(self):
        for i in range(0, self.GetLen()):
            previous_char = self.char
            self.char = self.GetCharWithLen(i)
            self.CallFunctions(previous_char)

    def CallFunctions(self, previous_char):
        print(self.char)
        match self.char:
            case ' ':
                pass
                #self.volume.StopSong()
            case 'A'|'B'|'C'|'D'|'E'|'F'|'G'|'a'|'b'|'c'|'d'|'e'|'f'|'g':
                #se caractere = B; checar próximos 3 caracteres para ver se é 'BPM+'
                self.note.ChangeNote(self.char, self.out)
            case 'O'|'I'|'U'|'o'|'i'|'u':
                if previous_char in ['A','B','C','D','E','F','G','a','b','c','d','e','f','g','?']:
                    self.note.RepeatNote(self.out)
                else:
                    self.instrument.SetInstrument(124, self.out)
            case '+':
                self.volume.DoubleVolume(self.out)
            case '-':
                self.volume.DefaultVolume(self.out)
            case '?':
                char = self.notes[random.randrange(0,6)]
                self.note.ChangeNote(char, self.out)
            # novo case 'R' + checar se próximo caractere é '-' ou '+'
            case '\n':
                self.instrument.SetInstrument(random.randrange(0,126), self.out)
            case ';':
                self.note.SetVelocity(random.randrange(30,140))
            case _:
                pass
