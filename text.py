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
            self.CallFunctions(caractere_anterior)

    def CallFunctions(self, caractere_anterior):
        print(self.caractere)
        match self.caractere:
            case ' ':
                pass
                #self.volume.StopSong()
            case 'A'|'B'|'C'|'D'|'E'|'F'|'G'|'a'|'b'|'c'|'d'|'e'|'f'|'g':
                #se caractere = B; checar próximos 3 caracteres para ver se é 'BPM+'
                self.note.ChangeNote(self.caractere, self.out)
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
                caractere = self.notas[random.randrange(0,6)]
                self.note.ChangeNote(caractere, self.out)
            # novo case 'R' + checar se próximo caractere é '-' ou '+'
            case '\n':
                self.instrument.SetInstrument(random.randrange(0,126), self.out)
            case ';':
                self.note.SetVelocity(random.randrange(30,140))
            case _:
                pass
