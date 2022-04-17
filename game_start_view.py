import imp
import arcade
from arcade import gui
from game_view import GameView
from style import Style


class GameStartView(arcade.View):
    """View to show start screen"""

    def on_show(self):
        self.manager = gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.csscolor.DARK_SLATE_GRAY)

        self.btn_grp = gui.UIBoxLayout()

        start_btn = gui.UIFlatButton(text="Start", width=200, style=Style.primary_btn)
        self.btn_grp.add(start_btn.with_space_around(bottom=20))
        start_btn.on_click = self.start

        quit_btn = gui.UIFlatButton(text="Quit", width=200, style=Style.secondary_btn)
        self.btn_grp.add(quit_btn.with_space_around(bottom=20))
        quit_btn.on_click = self.quit

        self.manager.add(
            gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.btn_grp
            )
        )

    def start(self, event):
        print("Starting wordMD")
        game_view = GameView()
        self.manager.disable()
        self.window.show_view(game_view)

    def quit(self, event):
        print("Exiting wordMD")
        arcade.exit()

    def on_draw(self):
        self.clear()
        self.manager.draw()