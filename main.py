import arcade
from game_start_view import GameStartView

# CONSTANTS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "wordMD"


def main():
    """ Main function """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = GameStartView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()