from unidecode import unidecode
from errors import NoteNameError
class Note:
    notes = {
        "do":"C",
        "fa":"F",
        "la":"A",
        "mi":"E",
        "re":"D",
        "si":"B",
        "sol":"G"
    }
    frequency_default = 500

    def __init__(self, name):
        self.frequency = self.frequency_default
        self.name = self.ProcessNoteName(name)

    def ProcessNoteName(self,name):
        name = unidecode(name.lower())
        if name in self.notes:
            return self.notes[name]
        raise NoteNameError("Nome da nota inválido")
        
    def GetNote (self):
        return self.frequency

    def SetNote (self, frequency):
        self.frequency = frequency

    def RaiseOctave (self):
        self.frequency = self.frequency + 250

    def DefaultOctave (self):
        self.frequency = self.frequency_default
