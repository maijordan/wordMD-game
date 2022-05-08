import arcade
from letter_list import LetterList
import views.game_end_view

bulletDamage = -1  # keep value negative
playerMovementSpeed = 5
playerModel = arcade.Sprite("resources/ambulance_01.png", 0.05)
gunSound = arcade.load_sound(":resources:sounds/hurt4.wav")
correctSound = arcade.load_sound("resources/sounds/correct.mp3")
incorrectSound = arcade.load_sound(":resources:sounds/hurt3.wav")
backgroundScrollSpeed = -5 #always negative
leftBarrier = 155
rightBarrier = 845
letterMovementSpeed = -1 #always negative

class GameView(arcade.View):
    """View to show game screen"""

    def __init__(self):
        super().__init__()

        self.letterList = LetterList(self.window.width)
        self.bulletList = arcade.SpriteList()
        self.playerList = arcade.SpriteList()
        self.backgroundList = arcade.SpriteList()
        self.spacePressed = False
        self.rightPressed = False
        self.leftPressed = False
        self.showInfected = False

    def setup(self):
        self.playerPoints = 0;
        self.background1 = arcade.Sprite("resources/road_01.png")
        self.background1.width = self.window.width
        self.background1.height = self.window.height
        self.background1.center_x = self.window.width / 2
        self.background1.change_y = backgroundScrollSpeed
        self.backgroundList.append(self.background1)

        self.background2 = arcade.Sprite("resources/road_01.png")
        self.background2.width = self.window.width
        self.background2.height = self.window.height
        self.background2.center_y = self.window.height
        self.background2.center_x = self.window.width / 2
        self.background2.change_y = backgroundScrollSpeed
        self.backgroundList.append(self.background2)
        #DW about this
        # self.secret = arcade.Sprite("resources/secret.png", 0.1)
        # self.secret.center_x = 985
        # self.secret.center_y = 3600
        # self.secret.change_y = -15
        

        playerModel.center_x = self.window.width / 2
        playerModel.center_y = 50
        self.playerList.append(playerModel)
        
        self.lives = 5
        

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
            letter.center_y += letterMovementSpeed
            letter.currentHealthBar()
                        
        arcade.draw_lrtb_rectangle_filled(self.window.width - 130, self.window.width - 42, self.window.height - 10, self.window.height - 80, arcade.csscolor.DARK_SLATE_GRAY);
        arcade.draw_lrtb_rectangle_outline(self.window.width - 130, self.window.width - 42, self.window.height - 10, self.window.height - 80, arcade.csscolor.WHITE, 3);

        arcade.draw_text(
            "Lives",
            self.window.width - 86,
            self.window.height - 45,
            arcade.csscolor.WHITE,
            font_size=26,
            anchor_x="center",
            font_name="Kenney High"
        )

        arcade.draw_text(
            "\u2665 " * self.lives,
            self.window.width - 86,
            self.window.height - 70,
            arcade.csscolor.LIGHT_PINK,
            font_size=12,
            anchor_x="center",
        )
        
        arcade.draw_lrtb_rectangle_filled(42, 130, self.window.height - 10, self.window.height - 80, arcade.csscolor.DARK_SLATE_GRAY);
        arcade.draw_lrtb_rectangle_outline(42, 130, self.window.height - 10, self.window.height - 80, arcade.csscolor.WHITE, 3);

        arcade.draw_text(
            "Points",
            86,
            self.window.height - 45,
            arcade.csscolor.WHITE,
            font_size=26,
            anchor_x="center",
            font_name="Kenney High"
        )

        arcade.draw_text(
            self.playerPoints,
            86,
            self.window.height - 67,
            arcade.csscolor.WHITE_SMOKE,
            font_size=18,
            anchor_x="center",
            font_name="Kenney High"
        )
        
        if self.showInfected:
            arcade.draw_text(
                "REMAINING",
                self.window.width / 2,
                self.window.height / 2 + 70,
                arcade.make_transparent_color(arcade.color.ARSENIC, 200),
                font_size=36,
                anchor_x="center",
                font_name="Kenney High"
            )
            
            arcade.draw_text(
                self.letterList.infectedCount,
                self.window.width / 2,
                self.window.height / 2 - 100,
                arcade.make_transparent_color(arcade.color.ARSENIC, 200),
                font_size=200,
                anchor_x="center",
                font_name="Kenney High"
            )

    def on_update(self, delta_time):
        # self.secret.update()
        # if self.secret.top <=0:
        #     self.secret.center_y = 4000
        self.bulletList.update()
        if self.spacePressed:
            bullet = self.createBullet()
            self.bulletList.append(bullet)
            arcade.play_sound(gunSound, 0.25)
        if self.leftPressed:
            if (playerModel.center_x - playerModel.width/2) - playerMovementSpeed >= leftBarrier:
                playerModel.center_x += -playerMovementSpeed
        if self.rightPressed:
            if (playerModel.center_x + playerModel.width/2) + playerMovementSpeed <= rightBarrier:
                playerModel.center_x += playerMovementSpeed
        
        #for loop to check for when letter reaches the player height
        for letter in self.letterList.letters:
            if(letter.bottom < playerModel.center_y + playerModel.height/2):
                self.letterList.genWord()
                arcade.play_sound(incorrectSound)
                self.die()
                break
                
        for bullet in self.bulletList:
            hitList = arcade.check_for_collision_with_list(
                bullet, self.letterList.letters
            )
            if len(hitList) > 0:
                bullet.remove_from_sprite_lists()
                for letter in hitList:
                    letter.currentHealth += bulletDamage
                if letter.currentHealth <= 0:
                    self.letterList.remove(letter)
                    #add points 
                    self.playerPoints += (self.letterList.getPoints * 100)
                    if(self.letterList.getPoints > 0):
                        arcade.play_sound(correctSound)
                    if(self.letterList.isWrong):
                        arcade.play_sound(incorrectSound)
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
        bullet = arcade.Sprite("resources/syringe_01.png", 0.02)
        bullet.change_y = 46
        bullet.center_x = playerModel.center_x
        bullet.bottom = playerModel.center_y + 4

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