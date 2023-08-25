class Instrument:
    code_midi_default = 0

    def __init__(self):
        self.codeMIDI = self.code_midi_default

    def GetInstrument (self):
        return self.codeMIDI

    def CalculateNewInstrument (self, valor_numerico, out):
        self.codeMIDI = self.codeMIDI + valor_numerico
        self.SetInstrument(self.GetInstrument(), out)