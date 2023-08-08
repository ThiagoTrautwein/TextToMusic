
class VolumeControler:
    defaultVolume = 30

    def __init__(self, out):
        self.volume = self.defaultVolume
        self.SetVolume(out)

    def GetVolume (self):
        return self.volume

    def SetVolume (self, out):
        out.send_message([0xB4, 0x07, self.GetVolume()])

    def ChangeVolume (self, volume, out):
        self.volume = volume
        self.SetVolume(out)

    def DoubleVolume (self, out):
        self.volume = self.GetVolume() * 2
        self.SetVolume(out)

    def DefaultVolume (self, out):
        self.volume = self.defaultVolume
        self.SetVolume(out)
