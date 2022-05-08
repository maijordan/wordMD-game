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
    music = arcade.Sound(musicList[0], streaming = True)
    current = music.play(volume = 0.2, loop = True)
    start_view = GameStartView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
    