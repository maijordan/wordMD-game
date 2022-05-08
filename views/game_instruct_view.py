import arcade
from arcade import gui
from utils.constants import FONT_NAME, READABLE_FONT_NAME, SCREEN_HEIGHT, SCREEN_WIDTH
from utils.ui_utils import genBtn
import views.game_start_view

class GameInstructView(arcade.View):
    """View to show game instructions"""

    def on_show(self):
        #init ui manager
        self.manager = gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.csscolor.DARK_SLATE_GRAY)

        #create box to group all btns
        self.menuGrp = gui.UIBoxLayout()

        backBtn = genBtn("Back",self.back)
        self.menuGrp.add(backBtn.with_space_around(top=450))

        self.manager.add(gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.menuGrp))

    def on_draw(self):
        self.clear()
        
        #print instructions
        self.drawCenteredText("How to Play", 120,large=True)
        self.drawCenteredText("Random letters have infected words!", 200)
        self.drawCenteredText("Shoot the incorrect letters to save them!", 250)
        self.drawListText("1. Use the right and left arrow keys or A and D to move the vehicle.",330)
        self.drawListText("2. Hold the spacebar to shoot.",380)
        self.drawListText("3. Hold Shift to show the number of remaining incorrect letters.",430)
        self.drawListText("4. Press Esc to pause the game or return to the main menu.",480)

        #draw back btn
        self.manager.draw()

    def drawCenteredText(self,title,heightOffset,large=False):
        arcade.draw_text(title, SCREEN_WIDTH / 2, SCREEN_HEIGHT - heightOffset,arcade.color.WHITE, font_size=(70 if large else 35), anchor_x="center",font_name=(FONT_NAME if large else READABLE_FONT_NAME))
        
    def drawListText(self,title,heightOffset):
        arcade.draw_text(title,90, SCREEN_HEIGHT - heightOffset, arcade.color.WHITE, font_size=28,anchor_x="left",font_name=READABLE_FONT_NAME)

    def back(self, event):
        self.manager.disable()
        self.window.show_view(views.game_start_view.GameStartView())
  
    