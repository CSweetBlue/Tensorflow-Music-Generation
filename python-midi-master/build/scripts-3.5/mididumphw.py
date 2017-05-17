#!C:\Users\Christian\AppData\Local\Programs\Python\Python35\python.exe
"""
Print a description of the available devices.
"""
import midi.sequencer as sequencer

s = sequencer.SequencerHardware()

print(s)