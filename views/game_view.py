import arcade
from sprites.bullets import BulletList
from sprites.letters import LetterList
from sprites.backgrounds import ScrollingBkgrdList
from sprites.players import PlayerList
import views.game_end_view
from constants import BKGRD_COLOR,FONT_NAME, NUM_LIVES,CORRECT_SOUND,INCORRECT_SOUND,INFECTED_COUNT_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH

class GameView(arcade.View):
    """View to show game screen"""

    def __init__(self):
        super().__init__()

        self.letterList = LetterList()
        self.bulletList = BulletList()
        self.playerList = PlayerList()
        self.backgroundList = ScrollingBkgrdList()
        self.spacePressed = False
        self.rightPressed = False
        self.leftPressed = False
        self.showInfected = False

    def setup(self):
        self.playerPoints = 0
        self.lives = NUM_LIVES
        
        #DW about this
        # self.secret = arcade.Sprite("resources/secret.png", 0.1)
        # self.secret.center_x = 985
        # self.secret.center_y = 3600
        # self.secret.change_y = -15
        

    def on_show(self):
        self.setup()


    def on_draw(self):
        self.clear()

        self.backgroundList.draw()
        self.bulletList.draw()
        self.playerList.draw()
        self.letterList.draw()
        
        self.drawLives()
        self.drawPoints()
        self.drawInfected()

    def on_update(self, delta_time):
        # self.secret.update()
        # if self.secret.top <=0:
        #     self.secret.center_y = 4000
        
        if self.spacePressed:
            self.bulletList.createBullet(self.playerList.centerX,self.playerList.centerY + 4)
        if self.leftPressed:
            self.playerList.move(-1)
        if self.rightPressed:
            self.playerList.move(1)
        
        #check for when letter reaches the player height
        if(self.letterList.bottom < self.playerList.top):
            self.handleWrong()
            
        self.backgroundList.update()
        
        self.playerPoints += self.bulletList.update(self.letterList,self.handleRight,self.handleWrong)

    def drawLives(self):
        self.drawSideBoard("Lives","\u2665 " * self.lives,SCREEN_WIDTH - 130, SCREEN_WIDTH - 42,True)
    
    def drawPoints(self):
        self.drawSideBoard("Points",str(self.playerPoints),42,136)
    
    def drawSideBoard(self,topTxt,btmTxt,left,right,isSymbol=False):
        arcade.draw_lrtb_rectangle_filled(left,right, SCREEN_HEIGHT - 10, SCREEN_HEIGHT - 80, BKGRD_COLOR);
        arcade.draw_lrtb_rectangle_outline(left,right, SCREEN_HEIGHT - 10, SCREEN_HEIGHT - 80, arcade.csscolor.WHITE, 3);

        arcade.draw_text(
            topTxt.strip(),
            left + (right - left) / 2,
            SCREEN_HEIGHT - 45,
            arcade.csscolor.WHITE,
            font_size=26,
            anchor_x="center",
            font_name=FONT_NAME
        )

        arcade.draw_text(
            btmTxt.strip(),
            left + (right - left) / 2,
            SCREEN_HEIGHT - 67,
            arcade.csscolor.LIGHT_PINK if isSymbol else arcade.csscolor.WHITE_SMOKE,
            font_size=18,
            anchor_x="center",
            font_name=("arial" if isSymbol else FONT_NAME)
        )
        
    def drawInfected(self):
        if self.showInfected:
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
        arcade.play_sound(INCORRECT_SOUND)
        self.lives -= 1
        if self.lives == 0:
            self.window.show_view(views.game_end_view.GameEndView())
        self.letterList.genWord()
            
    def handleRight(self):
        arcade.play_sound(CORRECT_SOUND)
        self.letterList.genWord()
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.spacePressed = True
        elif key == arcade.key.LEFT:
            self.leftPressed = True
        elif key == arcade.key.RIGHT:
            self.rightPressed = True
        elif key == arcade.key.LSHIFT:
            self.showInfected = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.spacePressed = False
        elif key == arcade.key.LEFT:
            self.leftPressed = False
        elif key == arcade.key.RIGHT:
            self.rightPressed = False
        elif key == arcade.key.LSHIFT:
            self.showInfected = False