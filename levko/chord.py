# -*- coding: utf-8 -*-
import random


class Chord:
  INTERVALS = []

  def __init__(self, root_note):
    self._root_note = root_note

  def pick_random_note(self):
    return self._root_note + random.choice(self.INTERVALS)


class MajorChord(Chord):
  INTERVALS = [0, 4, 7]

class MinorChord(Chord):
  INTERVALS = [0, 3, 7]

class DominantSeventh(Chord):
  INTERVALS = [0, 4, 7, 10]

class MajorSeventh(Chord):
  INTERVALS = [0, 4, 7, 11]

class MinorSeventh(Chord):
  INTERVALS = [0, 3, 7, 10]
