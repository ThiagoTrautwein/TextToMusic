

class Note:
    frequency_default = 500

    def __init__(self, name):
        self.frequency = self.frequency_default
        self.name = name


    def GetNote (self):
        return self.frequency

    def SetNote (self, frequency):
        self.frequency = frequency

    def RaiseOctave (self):
        self.frequency = self.frequency + 250

    def DefaultOctave (self):
        self.frequency = self.frequency_default
