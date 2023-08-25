
class Instrument:
    code_midi_default = 0

    def __init__(self, out):
        self.codeMIDI = self.code_midi_default
        self.SetInstrument(self.GetInstrument(), out)      

    def GetInstrument (self):
        return self.codeMIDI

    def SetInstrument (self, code_midi, out):
        self.codeMIDI = code_midi
        out.send_message ([0xC4, self.GetInstrument()])

    def CalculateNewInstrument (self, valor_numerico, out):
        self.codeMIDI = self.codeMIDI + valor_numerico
        self.SetInstrument(self.GetInstrument(), out)