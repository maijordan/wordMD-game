import arcade
from utils.constants import BKGRD_COLOR
from arcade import gui
from utils.ui_utils import genBtn, genTitle
import views.game_view


class GameStartView(arcade.View):
    """View to show start screen"""

    def on_show(self):
        #init ui manager
        self.manager = gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(BKGRD_COLOR)

        #create box to group all btns
        self.menuGrp = gui.UIBoxLayout()

        #add logo
        self.menuGrp.add(genTitle())

        #create and add btns
        startBtn = genBtn("Start",self.start)
        self.menuGrp.add(startBtn)

        quitBtn = genBtn("Quit",self.quit,False)
        self.menuGrp.add(quitBtn)

        #add and center btn group
        self.manager.add(
            gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.menuGrp
            )
        )

    def start(self, event):
        self.manager.disable() #disable btns before moving to new view
        self.window.show_view(views.game_view.GameView())

    def quit(self, event):
        arcade.exit()

    def on_draw(self):
        self.clear()
        self.manager.draw()