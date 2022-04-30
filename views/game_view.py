import arcade
from letter_list import LetterList
import views.game_end_view

class GameView(arcade.View):
    """View to show game screen"""

    def __init__(self):
        super().__init__()

        self.letter_list = LetterList(self.window.width)

    def setup(self):
        self.background = arcade.load_texture("resources/road_01.png")

        arcade.set_background_color(arcade.csscolor.DARK_SLATE_GRAY)
        # sprite list to hold all sprites
        self.bullet_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        self.player_model = arcade.Sprite("resources/ambulance_01.png", 0.05)
        self.player_model.center_x = self.window.width / 2
        self.player_model.center_y = 50
        self.player_list.append(self.player_model)

    def on_show(self):
        self.setup()

    def on_draw(self):
        self.clear()

        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.window.width, self.window.height, self.background
        )

        self.player_list.draw()

        self.letter_list.letters.draw()
        self.bullet_list.draw()

    def on_update(self, delta_time):
        self.bullet_list.update()
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(
                bullet, self.letter_list.letters
            )
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                for letter in hit_list:
                    self.letter_list.remove(letter)

            if bullet.bottom > self.window.height:
                bullet.remove_from_sprite_lists()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        print("clicked")

    def end_game(self):
        self.window.show_view(views.game_end_view.GameEndView())

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            print("space")
            # creation of bullet to add to bullet sprite list
            gun_sound = arcade.load_sound(":resources:sounds/hurt4.wav")
            bullet = arcade.Sprite("resources/syringe_01.png", 0.02)
            arcade.play_sound(gun_sound)
            bullet.change_y = 10
            bullet.center_x = self.player_model.center_x
            bullet.bottom = self.player_model.center_y + 45
            self.bullet_list.append(bullet)

        elif key == arcade.key.LEFT:
            if self.player_model.center_x - 50 < 0:
                print("don't do it")
            else:
                self.player_model.center_x += -50
        elif key == arcade.key.RIGHT:
            if self.player_model.center_x + 50 > self.window.width:
                print("don't do it")
            else:
                self.player_model.center_x += 50
        # temporary way to get to end screen: type the letter d
        elif key == arcade.key.D:
            self.end_game()
