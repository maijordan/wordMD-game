import arcade
from utils.constants import BKGRD_COLOR
from arcade import gui
from utils.ui_utils import genBtn, genTitle
import views.game_view
import views.game_start_view

class GameEndView(arcade.View):
    """View to show ending screen"""

    def on_show(self):
        #init ui manager
        self.manager = gui.UIManager()
        file = open("scores.txt", "r")
        score = file.readline()
        file.close()
        self.manager.enable()

        arcade.set_background_color(BKGRD_COLOR)
        
        #create box to group all btns
        self.menuGrp = gui.UIBoxLayout()

        #add logo
        self.menuGrp.add(genTitle())
        
        yourScoreText = arcade.gui.UILabel(text = "Your Score",font_size = 18)
        self.menuGrp.add(yourScoreText.with_space_around(bottom=10))
    
        playerScore = str(self.findPlayerScore(score))
        playerText = arcade.gui.UILabel(text = playerScore,font_size = 18,text_color = arcade.color.BLUE_GREEN)
        self.menuGrp.add(playerText.with_space_around(bottom=10))
        
    
        highestScoreText = arcade.gui.UILabel(text = "High Score",font_size = 18)
        self.menuGrp.add(highestScoreText.with_space_around(bottom=10))
        
       
        highScore = str(self.findHighestScore(score))
        highscoreText = arcade.gui.UILabel(text = highScore,font_size = 18, text_color = arcade.color.BLUE_GREEN)
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
        
    def findHighestScore(self, scores):
        splitScores = scores.split(",")
        splitScores.pop()
        highScore = 0
        for score in splitScores:
            if int(score) > highScore:
                highScore = int(score)
        
        return highScore
    
    def findPlayerScore(self,scores):
        splitScore = scores.split(",")
        splitScore.pop()
        return splitScore[len(splitScore)-1]
 