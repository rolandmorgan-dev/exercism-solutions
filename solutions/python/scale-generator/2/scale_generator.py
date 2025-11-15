SHARP = ("A","A#","B","C","C#","D","D#","E","F","F#","G","G#")
FLAT  = ("A","Bb","B","C","Db","D","Eb","E","F","Gb","G","Ab")
STEP  = {"m" : 1, "M" : 2, "A" : 3}

class Scale:
    def __init__(self, tonic):
        flats = ("F","Bb","Eb","Ab","Db","Gb","d","g","c","f","bb","eb")
        self.scale = FLAT if tonic in flats else SHARP
        self.tonic = tonic.capitalize()
        self.index = self.scale.index(self.tonic)
    
    def chromatic(self):
        return [self.scale[i % 12] for i in range(self.index, self.index+12)]
    
    def interval(self, steps):
        i = self.index
        scale_notes = [self.tonic]
        for s in steps:
            i = (i + STEP[s]) % 12
            scale_notes.append(self.scale[i])
        return scale_notes