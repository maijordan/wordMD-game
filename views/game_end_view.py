import arcade
from utils.constants import BKGRD_COLOR, SCORE_FILE
from arcade import gui
from utils.ui_utils import genBtn, genLabel, genTitle
import views.game_view
import views.game_start_view

class GameEndView(arcade.View):
    """View to show ending screen"""

    def on_show(self):
        #init ui manager
        self.manager = gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(BKGRD_COLOR)
        
        #create box to group all btns
        self.menuGrp = gui.UIBoxLayout()

        #add logo
        self.menuGrp.add(genTitle())
        
        #retrieve and show scores
        playerScore,highScore = self.processScoreFile()
        
        yourScoreText = genLabel("Your Score")
        self.menuGrp.add(yourScoreText)
        
        playerText = genLabel(playerScore,True)
        self.menuGrp.add(playerText)
        
        highestScoreText = genLabel("High Score")
        self.menuGrp.add(highestScoreText)
        
        highscoreText = genLabel(highScore,True)
        self.menuGrp.add(highscoreText.with_space_around(bottom=30))
          
        #create and add btns
        restartBtn = genBtn("Try Again!",self.restart)
        self.menuGrp.add(restartBtn)

        startBtn = genBtn("Main Menu",self.openStart,False)
        self.menuGrp.add(startBtn)

        quitBtn = genBtn("Quit",self.quit,False)
        self.menuGrp.add(quitBtn)

        #add and center btn group
        self.manager.add(
            gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.menuGrp
            )
        )

    def restart(self, event):
        self.manager.disable() #disable btns before moving to new view
        self.window.show_view(views.game_view.GameView())

    def openStart(self, event):
        self.manager.disable() #disable btns before moving to new view
        self.window.show_view(views.game_start_view.GameStartView())

    def quit(self, event):
        arcade.exit()

    def on_draw(self):
        self.clear()
        self.manager.draw()
        
    def processScoreFile(self):
        """Processes score file and returns (last score, high score)"""
        file = open(SCORE_FILE, "r")
        scores = file.readline()
        file.close()
        splitScores = scores.split(",")[:-1]
        lastScore = splitScores[-1]
        highScore = max(map(int,splitScores))
        return lastScore,highScore
 