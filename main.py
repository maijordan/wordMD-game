import arcade
from constants import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH
from views.game_start_view import GameStartView

def main():
    """ Main function """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    startView = GameStartView()
    window.show_view(startView)
    arcade.run()


if __name__ == "__main__":
    main()