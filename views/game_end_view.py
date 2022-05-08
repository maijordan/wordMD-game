import arcade
from utils.constants import BKGRD_COLOR
from arcade import gui
from utils.ui_utils import genBtn, genTitle
import views.game_view
import views.game_start_view

class GameEndView(arcade.View):
    """View to show ending screen"""

    def on_show(self):
        self.manager = gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(BKGRD_COLOR)

        self.menuGrp = gui.UIBoxLayout()

        self.menuGrp.add(genTitle())

        restartBtn = genBtn("Try Again!",self.restart)
        self.menuGrp.add(restartBtn)

        quitBtn = genBtn("Main Menu",self.openStart,False)
        self.menuGrp.add(quitBtn)

        quitBtn = genBtn("Quit",self.quit,False)
        self.menuGrp.add(quitBtn)

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