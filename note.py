import time

class Note:
    ## valor da nota em inteiro
    ## Range: 0-127
    note_default = 36
    velocity_default = 100
    C = [0,12,24,36,48,60,72,84,96,108,120]
    # Csharp = [1,13,25,37,49,61,73,85,97,109,121]
    D = [2,14,26,38,50,62,74,86,98,110,122]
    # Dsharp = [3,15,27,39,51,63,75,87,99,111,123]
    E = [4,16,28,40,52,64,76,88,100,112,124]
    F = [5,17,29,41,53,65,77,89,101,113,125]
    # Fsharp = [6,18,30,42,54,66,78,90,102,114,126]
    G = [7,19,31,43,55,67,79,91,103,115,127]
    # Gsharp = [8,20,32,44,56,68,80,92,104,116]
    A = [9,21,33,45,57,69,81,93,105,117]
    # Asharp = [10,22,34,46,58,70,82,94,106,118]
    B = [11,23,35,47,59,71,83,95,107,119]

    def __init__(self, nota, out):
        self.note = nota
        self.velocity = 100
        self.PlayNote(out)
        
    def GetNote (self):
        return self.note

    def SetNote (self, note, out):
        self.SilenceNote(out)
        self.note = note
        self.PlayNote(out)

    def SetVelocity (self, velocity):
        self.velocity = velocity

    def PlayNote(self, out):
        # src = 0x94 = note on
        out.send_message([0x94, self.GetNote(), self.velocity])
        time.sleep(1.0)

    def SilenceNote(self, out):
        # src = 0x84 = note off
        out.send_message([0x84, self.GetNote(), 0])
        time.sleep(0.1)

    def ChangeNote(self, caractere, out):
        match caractere:
            case 'A' | 'a':
                self.SetNote(33, out)
            case 'B' | 'b':
                self.SetNote(35, out)
            case 'C' | 'c':
                self.SetNote(36, out)
            case 'D' | 'd':
                self.SetNote(38, out)
            case 'E' | 'e':
                self.SetNote(40, out)
            case 'F' | 'f':
                self.SetNote(41, out)
            case 'G' | 'g':
                self.SetNote(43, out)
            

    def RaiseOctave (self, out):
        self.SilenceNote(out)
        self.note = self.GetNote() + 12
        self.PlayNote(out)

    def LowerOctave (self, out):
        self.SilenceNote(out)
        self.note = self.GetNote() - 12
        self.PlayNote(out)

    def DefaultOctave (self, out):
        self.SilenceNote(out)
        self.note = self.note_default
        self.PlayNote(out)

    def RepeatNote(self, out):
        self.SetNote(self.note, out)
