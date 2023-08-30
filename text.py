import random
from music_controler import MusicControler


class Text:
        
    def __init__(self):
        self.text = ''
        self.char = ''
        self.notes = ['A','B','C','D','E','F','G']
        self.text_lenght = 0
        self.music = MusicControler()

    def __GetLen(self):
        return self.text_lenght
    
    def __GetCharWithLen(self, position):
        return self.text[position]

    def SetText(self, text):
        self.text = text
        self.__SetLen()
        self.__ScanText()

    def __SetLen(self):
        self.text_lenght = len(self.text)

    #def SetTextFromArchive(self, archive):
    #    with open(archive, 'r') as file:
    #        self.text = file.read()
    #        self.__SetLen()
    #        self.__ScanText()

    def __ScanText(self):
        skip = 0
        for i in range(0, self.__GetLen()):
            if skip == 0:   #caso tenha lido 'BPM+' pula os caracteres 'PM+'
                previous_char = self.char
                self.char = self.__GetCharWithLen(i)
                if self.char == '+' or self.char == '-':
                    if previous_char == 'R':
                        pass
                    else:
                        self.__CallFunctions(previous_char, i)
                elif self.char == 'B' and self.__GetCharWithLen(i+1) == 'P' and self.__GetCharWithLen(i+2) == 'M' and self.__GetCharWithLen(i+3) == '+':
                    self.music.RaiseTempo(80)
                    skip = 3
                else:
                    self.__CallFunctions(previous_char, i)
            else:
                skip = skip - 1
        self.music.writeFile()

    def __CallFunctions(self, previous_char, i):
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
                    self.music.ChangeInstrument(124)
            case '+':
                self.music.DoubleVolume()
            case '-':
                self.music.DefaultVolume()
            case '?':
                char = self.notes[random.randint(0,6)]
                self.music.ChangeNote(char)
            case 'R':
                if self.__GetCharWithLen(i+1)=='+':
                    self.music.RaiseOctave()
                elif self.__GetCharWithLen(i+1)=='-':
                    self.music.LowerOctave()
            case '\n':
                self.music.ChangeInstrument(0)
            case ';':
                self.music.ChangeTempo(random.randrange(50,140))
            case _:
                pass