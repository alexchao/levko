# -*- coding: utf-8 -*-
import random
import mido

from levko.chord import MajorChord
from levko.chord import MinorChord
from levko.chord import DominantSeventh
from levko.chord import MajorSeventh
from levko.chord import MinorSeventh

from levko.note import Note

NUM_PARTS = 8
TIME_STEP = 1024

CHORDS = [
  MajorSeventh(Note.C),
  DominantSeventh(Note.G),
  MinorSeventh(Note.A),
  MajorSeventh(Note.F),
  DominantSeventh(Note.E),
  MinorSeventh(Note.A),
  MinorSeventh(Note.D),
  DominantSeventh(Note.G),
  MajorSeventh(Note.C)
]

out_file = mido.MidiFile()
tracks = []

for i in range(NUM_PARTS):
  track = mido.MidiTrack()
  track.append(mido.Message('program_change', program=1))

  tracks.append(track)
  out_file.tracks.append(track)

for chord in CHORDS:
  for track in tracks:
    note_value = chord.pick_random_note()
    note_value += random.choice([36, 48, 60])
    track.append(mido.Message('note_on', note=note_value, velocity=100, time=0))
    track.append(mido.Message('note_off', note=note_value, velocity=100, time=TIME_STEP))

out_file.save('track.mid')
