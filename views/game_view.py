import arcade
from arcade import gui
from sprites.bullets import BulletList
from sprites.letters import LetterList
from sprites.backgrounds import ScrollingBkgrdList
from sprites.players import PlayerList
from utils.ui_utils import genBtn
import views.game_end_view
from utils.constants import BKGRD_COLOR,FONT_NAME, NUM_LIVES,CORRECT_SOUND,INCORRECT_SOUND,INFECTED_COUNT_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH

class GameView(arcade.View):
    """View to show game screen"""

    def __init__(self):
        super().__init__()

        #init all spritelists
        self.letterList = LetterList()
        self.bulletList = BulletList()
        self.playerList = PlayerList()
        self.backgroundList = ScrollingBkgrdList()
        

    def setup(self):
        #reset flags
        self.spacePressed = False
        self.rightPressed = False
        self.leftPressed = False
        self.showInfected = False
        self.paused = False
        
        self.letterList = LetterList()
        self.bulletList = BulletList()
        self.playerList = PlayerList()
        
        #reset game status
        self.playerPoints = 0
        self.lives = NUM_LIVES
        
        #DW about this
        # self.secret = arcade.Sprite("resources/secret.png", 0.1)
        # self.secret.center_x = 985
        # self.secret.center_y = 3600
        # self.secret.change_y = -15
                
        self.manager = gui.UIManager()
        self.menuGrp = gui.UIBoxLayout()
        
        resumeBtn = genBtn("Resume",self.resume)
        self.menuGrp.add(resumeBtn)
        
        restartBtn = genBtn("Restart",self.restart,False)
        self.menuGrp.add(restartBtn)
        
        menuBtn = genBtn("Main Menu",self.openStart,False)
        self.menuGrp.add(menuBtn)
        
        quitBtn = genBtn("Quit",self.quit,False)
        self.menuGrp.add(quitBtn)

        self.manager.add(
            gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.menuGrp
            )
        )
        
    def resume(self,event):
        self.paused = not self.paused
        
    def restart(self,event):
        self.setup()
    
    def openStart(self,event):
        self.manager.disable()
        self.window.show_view(views.game_start_view.GameStartView())
    
    def quit(self,event):
        arcade.exit()

    def on_show(self):
        self.setup() #dif func bc setup also used when restart game

    def on_draw(self):
        self.clear()

        self.backgroundList.draw()

        if not self.paused:
            self.letterList.draw()
            self.bulletList.draw()
            self.playerList.draw()
        
        self.drawLives()
        self.drawPoints()
        self.drawInfected()
                        
        if self.paused:
            arcade.draw_lrtb_rectangle_filled(0, self.window.width, self.window.height, 0, arcade.make_transparent_color(arcade.csscolor.DARK_SLATE_GRAY, 100))
            self.manager.enable()
            self.manager.draw()
        else:
            self.manager.disable()
            
            
    def on_update(self, delta_time):
        # self.secret.update()
        # if self.secret.top <=0:
        #     self.secret.center_y = 4000
        
        #check keyboard flags
        if self.spacePressed:
            self.bulletList.createBullet(self.playerList.centerX,self.playerList.centerY + 4)
        if self.leftPressed:
            self.playerList.move(-1)
        if self.rightPressed:
            self.playerList.move(1)
        
        #check for when word reached player (player loses a life bc they were too slow)
        if(self.letterList.bottom < self.playerList.top):
            self.handleWrong()
            
        self.backgroundList.update()
        
        #check for bullet-letter collisions and get any points scored
        self.playerPoints += self.bulletList.update(self.letterList,self.handleRight,self.handleWrong)
        

    def drawLives(self):
        """Draws current number of lives in top right corner"""
        
        self.drawCornerBoard("Lives","\u2665 " * self.lives,SCREEN_WIDTH - 130, SCREEN_WIDTH - 42,True)
    
    def drawPoints(self):
        """Draws current number of points in top left corner"""
        self.drawCornerBoard("Points",str(self.playerPoints),42,136)
    
    def drawCornerBoard(self,topTxt,btmTxt,left,right,isSymbol=False):
        arcade.draw_lrtb_rectangle_filled(left,right, SCREEN_HEIGHT - 10, SCREEN_HEIGHT - 80, BKGRD_COLOR);
        arcade.draw_lrtb_rectangle_outline(left,right, SCREEN_HEIGHT - 10, SCREEN_HEIGHT - 80, arcade.csscolor.WHITE, 3);

        arcade.draw_text(
            topTxt.strip(),
            left + (right - left) / 2, #calcs middle of corner board to center text
            SCREEN_HEIGHT - 45,
            arcade.csscolor.WHITE,
            font_size=26,
            anchor_x="center",
            font_name=FONT_NAME
        )

        #draws white points or pink hearts depending on isSymbol flag
        arcade.draw_text(
            btmTxt.strip(),
            left + (right - left) / 2, #calcs middle of corner board to center text
            SCREEN_HEIGHT - 67,
            arcade.csscolor.LIGHT_PINK if isSymbol else arcade.csscolor.WHITE_SMOKE,
            font_size=18,
            anchor_x="center",
            font_name=("arial" if isSymbol else FONT_NAME) #hearts only print properly in arial font
        )
        
    def drawInfected(self):
        """If tab is currently pressed, draws infected count as an overlay"""

        if not self.paused and self.showInfected:
            arcade.draw_text(
                    "REMAINING",
                    SCREEN_WIDTH / 2,
                    SCREEN_HEIGHT / 2 + 70,
                    INFECTED_COUNT_COLOR,
                    font_size=36,
                    anchor_x="center",
                    font_name=FONT_NAME
                )
                
            arcade.draw_text(
                self.letterList.infectedCount,
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 - 100,
                INFECTED_COUNT_COLOR,
                font_size=200,
                anchor_x="center",
                font_name=FONT_NAME
            )
    
    def handleWrong(self):
        """Called when word was incorrectly cured"""

        arcade.play_sound(INCORRECT_SOUND)
        self.lives -= 1
        
        #if no more lives, go to end game view
        if self.lives == 0:
            file = open("scores.txt", "a")
            file.write(str(self.playerPoints) + ",")
            file.close()
            self.window.show_view(views.game_end_view.GameEndView())

        #gen next word
        self.letterList.genWord()
            
    def handleRight(self):
        """Called when word was correctly cured"""

        arcade.play_sound(CORRECT_SOUND)
        
        #gen next word
        self.letterList.genWord()
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.paused = not self.paused
            self.spacePressed = False
            self.leftPressed = False
            self.rightPressed = False
            self.showInfected = False
        elif key == arcade.key.SPACE:
            self.spacePressed = True
        elif key == arcade.key.LEFT:
            self.leftPressed = True
        elif key == arcade.key.RIGHT:
            self.rightPressed = True
        elif key == arcade.key.LSHIFT:
            self.showInfected = True

    def on_key_release(self, key, modifiers):
        if self.paused:
            return
        if key == arcade.key.SPACE:
            self.spacePressed = False
        elif key == arcade.key.LEFT:
            self.leftPressed = False
        elif key == arcade.key.RIGHT:
            self.rightPressed = False
        elif key == arcade.key.LSHIFT:
            self.showInfected = False