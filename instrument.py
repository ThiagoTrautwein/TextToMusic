

class Instrument(): 

    def __init__(self):
        self.instrument = 0

    def __SetInstrument(self, instrument, time, out, MIDI):
        self.instrument = instrument
        out.send_message([0xC4, instrument])
        MIDI.addProgramChange(0, 0, time, instrument)

    def ChangeInstrument(self, instrument, time, out, MIDI):
        self.__SetInstrument(instrument, time, out, MIDI)