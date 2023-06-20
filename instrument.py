class Instrument:
    code_midi_default = 1

    def __init__(self):
        self.codeMIDI = self.code_midi_default

    def GetInstrument (self):
        return self.codeMIDI

    def SetInstrument (self, code_midi):
        self.codeMIDI = code_midi

    def CalculateNewInstrument (self, valor_numerico):
        self.codeMIDI = self.codeMIDI + valor_numerico

