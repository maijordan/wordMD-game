import arcade


class GameView(arcade.View):
    """View to show game screen"""

    def on_show(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_GRAY)

    def on_draw(self):
        self.clear()
        arcade.draw_text(
            "wordMD game goes here",
            self.window.width / 2,
            self.window.height / 2,
            arcade.color.WHITE,
            font_size=24,
            anchor_x="center",
        )

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        print("clicked")
