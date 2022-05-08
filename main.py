import arcade
from views.game_start_view import GameStartView
import time

# CONSTANTS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "wordMD"
musicList = ["resources/sounds/driftveil.mp3"]

def main():
    """ Main function """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = GameStartView()
    window.show_view(start_view)
    arcade.run()
    play_song()


if __name__ == "__main__":
    main()
    

def play_song(self):
    current = None
    music = None
    print(f"Playing {musicList[0]}")
    if self.music:
        self.music.stop()
    self.music = arcade.Sound(musicList[0], streaming = True)
    self.current = self.music.play(volume = 0.2, loop = True)
    time.sleep(.03)