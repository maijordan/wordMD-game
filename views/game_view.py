import arcade
from letter_list import LetterList
import views.game_end_view
from constants import BKGRD_COLOR, BULLET_IMG, BULLET_IMG_SCALE, BULLET_SPEED,FONT_NAME,BULLET_DMG,LEFT_BARRIER, NUM_LIVES,RIGHT_BARRIER,PLAYER_SPEED,BKGRD_SCROLL_SPEED,LETTER_SPEED,PLAYER_IMG,PLAYER_IMG_SCALE,GUN_SOUND,CORRECT_SOUND,INCORRECT_SOUND,ROAD_IMG,INFECTED_COUNT_COLOR,GUN_SOUND_VOL,PT_MULT

class GameView(arcade.View):
    """View to show game screen"""

    def __init__(self):
        super().__init__()

        self.letterList = LetterList(self.window.width,self.window.height)
        self.bulletList = arcade.SpriteList()
        self.playerList = arcade.SpriteList()
        self.backgroundList = arcade.SpriteList()
        self.spacePressed = False
        self.rightPressed = False
        self.leftPressed = False
        self.showInfected = False

    def setup(self):
        self.playerPoints = 0;
        self.background1 = arcade.Sprite(ROAD_IMG)
        self.background1.width = self.window.width
        self.background1.height = self.window.height
        self.background1.center_x = self.window.width / 2
        self.background1.change_y = BKGRD_SCROLL_SPEED
        self.backgroundList.append(self.background1)

        self.background2 = arcade.Sprite(ROAD_IMG)
        self.background2.width = self.window.width
        self.background2.height = self.window.height
        self.background2.center_y = self.window.height
        self.background2.center_x = self.window.width / 2
        self.background2.change_y = BKGRD_SCROLL_SPEED
        self.backgroundList.append(self.background2)
        #DW about this
        # self.secret = arcade.Sprite("resources/secret.png", 0.1)
        # self.secret.center_x = 985
        # self.secret.center_y = 3600
        # self.secret.change_y = -15
        
        self.playerModel = arcade.Sprite(PLAYER_IMG, PLAYER_IMG_SCALE)
        self.playerModel.center_x = self.window.width / 2
        self.playerModel.center_y = 50
        self.playerList.append(self.playerModel)
        
        self.lives = NUM_LIVES
        

    def on_show(self):
        self.setup()


    def on_draw(self):
        self.clear()

        self.backgroundList.draw()
        self.bulletList.draw()
        self.playerList.draw()

        self.letterList.letters.draw()
        for letter in self.letterList.letters:
            #letter move down speed
            letter.center_y += LETTER_SPEED
            letter.currentHealthBar()
                        
        arcade.draw_lrtb_rectangle_filled(self.window.width - 130, self.window.width - 42, self.window.height - 10, self.window.height - 80, BKGRD_COLOR);
        arcade.draw_lrtb_rectangle_outline(self.window.width - 130, self.window.width - 42, self.window.height - 10, self.window.height - 80, arcade.csscolor.WHITE, 3);

        arcade.draw_text(
            "Lives",
            self.window.width - 86,
            self.window.height - 45,
            arcade.csscolor.WHITE,
            font_size=26,
            anchor_x="center",
            font_name=FONT_NAME
        )

        arcade.draw_text(
            "\u2665 " * self.lives,
            self.window.width - 86,
            self.window.height - 70,
            arcade.csscolor.LIGHT_PINK,
            font_size=12,
            anchor_x="center",
        )
        
        arcade.draw_lrtb_rectangle_filled(42, 130, self.window.height - 10, self.window.height - 80, BKGRD_COLOR);
        arcade.draw_lrtb_rectangle_outline(42, 130, self.window.height - 10, self.window.height - 80, arcade.csscolor.WHITE, 3);

        arcade.draw_text(
            "Points",
            86,
            self.window.height - 45,
            arcade.csscolor.WHITE,
            font_size=26,
            anchor_x="center",
            font_name=FONT_NAME
        )

        arcade.draw_text(
            self.playerPoints,
            86,
            self.window.height - 67,
            arcade.csscolor.WHITE_SMOKE,
            font_size=18,
            anchor_x="center",
            font_name=FONT_NAME
        )
        
        if self.showInfected:
            arcade.draw_text(
                "REMAINING",
                self.window.width / 2,
                self.window.height / 2 + 70,
                INFECTED_COUNT_COLOR,
                font_size=36,
                anchor_x="center",
                font_name=FONT_NAME
            )
            
            arcade.draw_text(
                self.letterList.infectedCount,
                self.window.width / 2,
                self.window.height / 2 - 100,
                INFECTED_COUNT_COLOR,
                font_size=200,
                anchor_x="center",
                font_name=FONT_NAME
            )

    def on_update(self, delta_time):
        # self.secret.update()
        # if self.secret.top <=0:
        #     self.secret.center_y = 4000
        self.bulletList.update()
        if self.spacePressed:
            bullet = self.createBullet()
            self.bulletList.append(bullet)
            arcade.play_sound(GUN_SOUND, GUN_SOUND_VOL)
        if self.leftPressed:
            if (self.playerModel.center_x - self.playerModel.width/2) - PLAYER_SPEED >= LEFT_BARRIER:
                self.playerModel.center_x += -PLAYER_SPEED
        if self.rightPressed:
            if (self.playerModel.center_x + self.playerModel.width/2) + PLAYER_SPEED <= RIGHT_BARRIER:
                self.playerModel.center_x += PLAYER_SPEED
        
        #for loop to check for when letter reaches the player height
        for letter in self.letterList.letters:
            if(letter.bottom < self.playerModel.center_y + self.playerModel.height/2):
                self.letterList.genWord()
                arcade.play_sound(INCORRECT_SOUND)
                self.die()
                break
                
        for bullet in self.bulletList:
            hitList = arcade.check_for_collision_with_list(
                bullet, self.letterList.letters
            )
            if len(hitList) > 0:
                bullet.remove_from_sprite_lists()
                for letter in hitList:
                    letter.currentHealth += BULLET_DMG
                if letter.currentHealth <= 0:
                    self.letterList.remove(letter)
                    #add points 
                    self.playerPoints += (self.letterList.points * PT_MULT)
                    if(self.letterList.points > 0):
                        arcade.play_sound(CORRECT_SOUND)
                    if(self.letterList.isWrong):
                        arcade.play_sound(INCORRECT_SOUND)
                        self.die()
                      
                    
            if bullet.bottom > self.window.height:
                bullet.remove_from_sprite_lists()

        self.backgroundList.update()
        if self.background1.bottom <= -self.window.height:
            self.background1.center_y = self.window.height + self.background1.height / 2

        if self.background2.bottom <= -self.window.height:
            self.background2.center_y = self.window.height + self.background2.height / 2

    def die(self):
        self.lives -= 1
        if self.lives == 0:
            self.window.show_view(views.game_end_view.GameEndView())

    def createBullet(self):
        bullet = arcade.Sprite(BULLET_IMG, BULLET_IMG_SCALE)
        bullet.change_y = BULLET_SPEED
        bullet.center_x = self.playerModel.center_x
        bullet.bottom = self.playerModel.center_y + 4

        return bullet

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