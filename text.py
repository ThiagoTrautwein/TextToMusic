import random
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
    
    def GetCharWithLen(self, position):
        return self.text[position]

    def SetText(self, text):
        self.text = text
        self.SetLen()
        self.ScanText()

    def SetLen(self):
        self.text_lenght = len(self.text)

    def SetTextFromArchive(self, archive):
        with open(archive, 'r') as file:
            self.text = file.read()
            self.SetLen()
            self.ScanText()

    def ScanText(self):
        skip = 0
        for i in range(0, self.text_lenght):
            if skip == 0:
                previous_char = self.char
                self.char = self.GetCharWithLen(i)
                if self.char == '+' or self.char == '-':
                    if previous_char == 'R':
                        pass
                    else:
                        self.CallFunctions(previous_char, i)
                elif self.char == 'B' and self.GetCharWithLen(i+1) == 'P' and self.GetCharWithLen(i+2) == 'M' and self.GetCharWithLen(i+3) == '+':
                    self.music.RaiseTempo(80)
                    skip = 3
                else:
                    self.CallFunctions(previous_char, i)
            else:
                skip = skip - 1
        self.music.writeFile()

    def CallFunctions(self, previous_char, i):
        print(i ," - " , self.char)
        match self.char:
            case ' ':
                self.music.SilentNote()
            case 'A'|'B'|'C'|'D'|'E'|'F'|'G'|'a'|'b'|'c'|'d'|'e'|'f'|'g':
                self.music.ChangeNote(self.char)
            case 'O'|'I'|'U'|'o'|'i'|'u':
                if previous_char in ['A','B','C','D','E','F','G','a','b','c','d','e','f','g','?']:
                    self.music.RepeatNote()
                else:
                    self.music.SetInstrument(124)
            case '+':
                self.music.DoubleVolume()
            case '-':
                self.music.DefaultVolume()
            case '?':
                char = self.notes[random.randint(0,6)]
                self.music.ChangeNote(char)
            case 'R':
                if self.GetCharWithLen(i+1)=='+':
                    self.music.RaiseOctave()
                elif self.GetCharWithLen(i+1)=='-':
                    self.music.LowerOctave()
            case '\n':
                self.music.SetInstrument(0)
            case ';':
                self.music.SetTempo(random.randrange(30,140))
            case _:
                pass