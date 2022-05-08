import arcade
from arcade import gui
import views.game_view
import views.game_start_view
from style import Style


class GameEndView(arcade.View):
    """View to show ending screen"""

    def on_show(self):
        self.manager = gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.csscolor.DARK_SLATE_GRAY)

        self.menuGrp = gui.UIBoxLayout()

        title = gui.UISpriteWidget(
            sprite=arcade.Sprite("resources/title_01.png"), width=350
        )
        self.menuGrp.add(title.with_space_around(bottom=50))

        restartBtn = gui.UIFlatButton(
            text="Try Again!", width=200, style=Style.primary_btn
        )
        self.menuGrp.add(restartBtn.with_space_around(bottom=20))
        restartBtn.on_click = self.restart

        quitBtn = gui.UIFlatButton(
            text="Main Menu", width=200, style=Style.secondary_btn
        )
        self.menuGrp.add(quitBtn.with_space_around(bottom=20))
        quitBtn.on_click = self.openStart

        quitBtn = gui.UIFlatButton(text="Quit", width=200, style=Style.secondary_btn)
        self.menuGrp.add(quitBtn.with_space_around(bottom=20))
        quitBtn.on_click = self.quit

        self.manager.add(
            gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.menuGrp
            )
        )

    def restart(self, event):
        self.manager.disable()
        self.window.show_view(views.game_view.GameView())

    def openStart(self, event):
        self.manager.disable()
        self.window.show_view(views.game_start_view.GameStartView())

    def quit(self, event):
        arcade.exit()

    def on_draw(self):
        self.clear()
        self.manager.draw()