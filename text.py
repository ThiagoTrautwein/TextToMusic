from random import random
import rtmidi
from note import Note
from instrument import Instrument
from music_controler import VolumeControler

class Text:
        
    def __init__(self, texto):
        self.texto = texto
        self.caractere = ''
        self.notas = ['A','B','C','D','E','F','G']
        self.texto_tamanho = len(texto)
        self.out = rtmidi.MidiOut()
        self.out.open_port(0)
        self.note = Note(36, self.out)
        self.instrument = Instrument(self.out)
        self.volume = VolumeControler(self.out)

    def GetText(self):
        return print(self.texto)

    def GetLen(self):
        return self.texto_tamanho
    
    def GetCharWithLen(self, posicao):
        return self.texto[posicao]

    def PercorreTexto(self):
        for i in range(0, self.GetLen()):
            caractere_anterior = self.caractere
            self.caractere = self.GetCharWithLen(i)
            if self.caractere == '+' or self.caractere == '-':
                if caractere_anterior != 'R':
                    self.CallFunctions(caractere_anterior, i)
            else:
                self.CallFunctions(caractere_anterior, i)

    def CallFunctions(self, caractere_anterior, i):
        print(self.caractere + ' + ' + caractere_anterior)
        #print(self.GetCharWithLen(i) + self.GetCharWithLen(i+1) + self.GetCharWithLen(i+2))
        match self.caractere:
            case ' ':
                pass
                return 0
                #self.volume.StopSong()
            case 'A'|'B'|'C'|'D'|'E'|'F'|'G'|'a'|'b'|'c'|'d'|'e'|'f'|'g':
                #se caractere = B; checar próximos 3 caracteres para ver se é 'BPM+'
                self.note.ChangeNote(self.caractere, self.out) #
                return 0
            case 'O'|'I'|'U'|'o'|'i'|'u':
                if caractere_anterior in ['A','B','C','D','E','F','G','a','b','c','d','e','f','g','?']:
                    self.note.RepeatNote(self.out)
                    return 0
                else:
                    self.instrument.SetInstrument(124, self.out)
                    return 0
            case '+':
                self.volume.DoubleVolume(self.out)
                return 0
            case '-':
                self.volume.DefaultVolume(self.out)
                return 0
            case '?':
                caractere =  'A' #'self.notas[random.randrange(0,6)]'
                self.note.ChangeNote(caractere, self.out) #
                return 0
            case 'R':
                if self.GetCharWithLen(i+1)=='+':
                    self.note.RaiseOctave(self.out)
                    return 1
                elif self.GetCharWithLen(i+1)=='-':
                    self.note.LowerOctave(self.out)
                    return 1
            case '\n':
                self.instrument.SetInstrument(random.randrange(0,126), self.out)
                return 0
            case ';':
                self.note.SetVelocity(random.randrange(30,140))
                return 0
            case _:
                return 0
