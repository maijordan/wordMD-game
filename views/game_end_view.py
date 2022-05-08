import arcade
from arcade import gui
import views.game_view
import views.game_start_view
from style import Style


class GameEndView(arcade.View):
    """View to show ending screen"""

    def on_show(self):
        self.manager = gui.UIManager()
        file = open("scores.txt", "r")
        score = file.readline()
        file.close()
        self.manager.enable()

        arcade.set_background_color(arcade.csscolor.DARK_SLATE_GRAY)

        self.menu_grp = gui.UIBoxLayout()

        title = gui.UISpriteWidget(
            sprite=arcade.Sprite("resources/title_01.png"), width=350
        )
        self.menu_grp.add(title.with_space_around(bottom=30))
        
        yourScoreText = arcade.gui.UILabel(text = "Your Score",font_size = 18)
        self.menu_grp.add(yourScoreText.with_space_around(bottom=10))
    
        playerScore = str(self.findPlayerScore(score))
        playerText = arcade.gui.UILabel(text = playerScore,font_size = 18,text_color = arcade.color.BLUE_GREEN)
        self.menu_grp.add(playerText.with_space_around(bottom=10))
        
    
        highestScoreText = arcade.gui.UILabel(text = "High Score",font_size = 18)
        self.menu_grp.add(highestScoreText.with_space_around(bottom=10))
        
       
        highScore = str(self.findHighestScore(score))
        highscoreText = arcade.gui.UILabel(text = highScore,font_size = 18, text_color = arcade.color.BLUE_GREEN)
        self.menu_grp.add(highscoreText.with_space_around(bottom=30))
          
        start_btn = gui.UIFlatButton(
            text="Try Again!", width=200, style=Style.primary_btn
        )
        self.menu_grp.add(start_btn.with_space_around(bottom=20))
        start_btn.on_click = self.restart

        quit_btn = gui.UIFlatButton(
            text="Main Menu", width=200, style=Style.secondary_btn
        )
        self.menu_grp.add(quit_btn.with_space_around(bottom=20))
        quit_btn.on_click = self.open_start

        quit_btn = gui.UIFlatButton(text="Quit", width=200, style=Style.secondary_btn)
        self.menu_grp.add(quit_btn.with_space_around(bottom=20))
        quit_btn.on_click = self.quit

        self.manager.add(
            gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.menu_grp
            )
            
        
        )
        
        

    def restart(self, event):
        print("Restarting wordMD")
        self.manager.disable()
        self.window.show_view(views.game_view.GameView())

    def open_start(self, event):
        print("Opening start view")
        self.manager.disable()
        self.window.show_view(views.game_start_view.GameStartView())

    def quit(self, event):
        print("Exiting wordMD")
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
 