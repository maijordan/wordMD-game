import arcade
from utils.constants import BKGRD_MUSIC, SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH
from views.game_start_view import GameStartView

def main():
    """ Main function (run to start game)"""

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    music = arcade.Sound(BKGRD_MUSIC, streaming = True)
    music.play(volume = 0.2, loop = True)
    start_view = GameStartView()
    window.show_view(start_view)
    
    arcade.run()


if __name__ == "__main__":
    main()
    