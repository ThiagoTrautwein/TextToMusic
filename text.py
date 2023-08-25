from random import random
from music_controler import MusicControler

class Text:
        
    def __init__(self):
        self.text = ''
        self.char = ''
        self.notes = ['A','B','C','D','E','F','G']
        self.text_lenght = 0
        self.music = MusicControler()

    def GetText(self):
        return self.text

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

    def GetCharWithLen(self, position):
        return self.text[position]

    def ScanText(self):
        for i in range(0, self.text_lenght):
            print(i)
            previous_char = self.char
            self.char = self.GetCharWithLen(i)
            if self.char == '+' or self.char == '-':
                if previous_char == 'R':
                    pass
                else:
                    self.CallFunctions(previous_char, i)
            else:
                self.CallFunctions(previous_char, i)
        self.music.writeFile()

    def CallFunctions(self, previous_char, i):
        print(self.char + ' + ' + previous_char)
        #print(self.GetCharWithLen(i) + self.GetCharWithLen(i+1) + self.GetCharWithLen(i+2))
        match self.char:
            case ' ':
                pass
                #self.volume.StopSong()
            case 'A'|'B'|'C'|'D'|'E'|'F'|'G'|'a'|'b'|'c'|'d'|'e'|'f'|'g':
                #se char = B; checar próximos 3 caracteres para ver se é 'BPM+'
                self.music.ChangeNote(self.char)
            case 'O'|'I'|'U'|'o'|'i'|'u':
                if previous_char in ['A','B','C','D','E','F','G','a','b','c','d','e','f','g','?']:
                    self.music.RepeatNote()
                else:
                    self.music.SetInstrument(10)
            case '+':
                self.music.DoubleVolume()
            case '-':
                self.music.DefaultVolume()
            case '?':
                char =  'A' #'self.notes[random.randrange(0,6)]'
                self.music.ChangeNote(char) #
            case 'R':
                if self.GetCharWithLen(i+1)=='+':
                    self.music.RaiseOctave()
                elif self.GetCharWithLen(i+1)=='-':
                    self.music.LowerOctave()
            case '\n':
                self.music.SetInstrument(random.randrange(0,126))
            case ';':
                self.music.SetVelocity(random.randrange(30,140))
            case _:
                self.music.DefaultVolume()