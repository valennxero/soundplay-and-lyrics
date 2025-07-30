import time
import sys
import pygame
pygame.mixer.init()
def run_lyrics():
  lyrics = [
    ("Well, I've been holding on tonight", 0.1),
    ("What's the worst that I can say?", 0.1),
    ("Things are better if I stay", 0.1),
    ("So long and goodnight",0.1),
    ("So long and goodnight",0.1),
    ("Well, if you carry on this way",0.1),
    ("Things are better if I stay",0.1),
    ("So long and goodnight",0.1),
    ("So long and goodnight",0.2),
    ]
  delay = [1.7, 1.2, 1.1, 1.6, 1.1, 1, 1, 0.7, 1.2]
  print("\nHelena - My Chemical Romance", "\n")
  time.sleep(0.1)
  for i, (baris_lagu, delay_char) in enumerate(lyrics):
    for karakter in baris_lagu:
      print(karakter, end='')
      sys.stdout.flush()
      time.sleep(delay_char)
    time.sleep(delay[i])
    print('')
  print("\nCode by Valen")

run_lyrics()
pygame.mixer.music.load("helena.mp3")
pygame.mixer.music.play()