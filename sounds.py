import pygame


class SoundManager:

    def __init__(self):

        pygame.mixer.init()

    def win_sound(self):

        print("🎵 Victory Sound")

    def lose_sound(self):

        print("🎵 Defeat Sound")