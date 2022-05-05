import arcade
from arcade import gui
from style import Style
import views.game_view


class GameStartView(arcade.View):
    """View to show start screen"""

    def on_show(self):
        self.manager = gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.csscolor.DARK_SLATE_GRAY)

        self.menu_grp = gui.UIBoxLayout()

        title = gui.UISpriteWidget(
            sprite=arcade.Sprite("resources/title_01.png"), width=350
        )
        self.menu_grp.add(title.with_space_around(bottom=50))

        start_btn = gui.UIFlatButton(text="Start", width=200, style=Style.primary_btn)
        self.menu_grp.add(start_btn.with_space_around(bottom=20))
        start_btn.on_click = self.start

        quit_btn = gui.UIFlatButton(text="Quit", width=200, style=Style.secondary_btn)
        self.menu_grp.add(quit_btn.with_space_around(bottom=20))
        quit_btn.on_click = self.quit

        self.manager.add(
            gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.menu_grp
            )
        )

    def start(self, event):
        print("Starting wordMD")
        self.manager.disable()
        self.window.show_view(views.game_view.GameView())

    def quit(self, event):
        print("Exiting wordMD")
        arcade.exit()

    def on_draw(self):
        self.clear()
        self.manager.draw()