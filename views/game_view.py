import arcade
import views.game_end_view


class GameView(arcade.View):
    """View to show game screen"""

    def on_show(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_GRAY)
        # sprite list to hold all sprites
        self.bullet_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.test = arcade.SpriteList()

        self.player_model = arcade.Sprite("resources/ambulance_01.png", 0.05)
        self.player_model.center_x = self.window.width / 2
        self.player_model.center_y = 50
        self.player_list.append(self.player_model)
        self.test_subject = arcade.Sprite("resources/ambulance_01.png", 0.05)
        self.test_subject.center_x = self.window.width / 2
        self.test_subject.center_y = 400
        self.test.append(self.test_subject)

        self.lives = 3

    def on_draw(self):
        self.clear()
        arcade.draw_text(
            "Lives: " + "\u2665 " * self.lives,
            self.window.width - 160,
            self.window.height - 40,
            arcade.csscolor.TOMATO,
            font_size=18,
            anchor_x="left",
        )
        self.player_list.draw()
        # test for collision
        self.test.draw()
        self.bullet_list.draw()

    def on_update(self, delta_time):
        self.bullet_list.update()
        for bullet in self.bullet_list:

            hit_list = arcade.check_for_collision_with_list(bullet, self.test)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            if bullet.bottom > self.window.height:
                bullet.remove_from_sprite_lists()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        print("clicked")

    def die(self):
        self.lives -= 1
        if self.lives == 0:
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
            if self.player_model.center_x - 100 < 0:
                print("don't do it")
            else:
                self.player_model.center_x += -100
        elif key == arcade.key.RIGHT:
            if self.player_model.center_x + 100 > self.window.width:
                print("don't do it")
            else:
                self.player_model.center_x += 100
        # temporary way to get to end screen: type the letter d
        elif key == arcade.key.D:
            self.die()
