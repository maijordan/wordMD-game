import arcade
from letter_list import LetterList
from letter_health import LetterHealth
import views.game_end_view

bulletDamage = -1 #keep value negative
playerMovementSpeed = 5
playerModel = arcade.Sprite("resources/ambulance_01.png", .05)
gunSound = arcade.load_sound(":resources:sounds/hurt4.wav")
backgroundScrollSpeed = -5 #always negative

class GameView(arcade.View):
    """View to show game screen"""

    def __init__(self):
        super().__init__()

        self.letter_list = LetterList(self.window.width)
        self.bullet_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.spacePressed = False
        self.rightPressed = False
        self.leftPressed = False

    def setup(self):
        self.background = arcade.load_texture("resources/road_01.png")
        self.background1 = arcade.Sprite("resources/road_01.png")
        self.background1.width = self.window.width
        self.background1.height = self.window.height
        #self.background1.center_y = self.window.height / 2
        self.background1.center_x = self.window.width / 2
        self.background1.change_y = backgroundScrollSpeed
        self.background_list.append(self.background1)
        
        self.background2 = arcade.Sprite("resources/road_01.png")
        self.background2.width = self.window.width
        self.background2.height = self.window.height
        self.background2.center_y = self.window.height 
        self.background2.center_x = self.window.width / 2
        self.background2.change_y = backgroundScrollSpeed
        self.background_list.append(self.background2)

        arcade.set_background_color(arcade.csscolor.DARK_SLATE_GRAY)
    

        playerModel.center_x = self.window.width / 2
        playerModel.center_y = 50
        self.player_list.append(playerModel)

    def on_show(self):
        self.setup()

    def on_draw(self):
        self.clear()

        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.window.width, self.window.height, self.background
        )
        self.background_list.draw()
        self.bullet_list.draw()   
        self.player_list.draw()

        self.letter_list.letters.draw()
        for letter in self.letter_list.letters:
            letter.currentHealthBar()
        

    def on_update(self, delta_time):
        self.bullet_list.update()
        if self.spacePressed:
            bullet = self.create_bullet()
            # bullet.change_y = 1
            # bullet.center_x = self.player_model.center_x
            # bullet.bottom = self.player_model.center_y + 45
            #bullet sound annoying
            self.bullet_list.append(bullet)
            arcade.play_sound(gunSound)
        if self.leftPressed:
            if playerModel.center_x - playerMovementSpeed < 0:
                print("don't do it")
            else:
                playerModel.center_x += -5
        if self.rightPressed:
            if playerModel.center_x + playerMovementSpeed > self.window.width:
                print("don't do it")
            else:
                playerModel.center_x += 5
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.letter_list.letters)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                for letter in hit_list:
                    #change to change the amount of damage each syringe does
                   letter.currentHealth += bulletDamage
                if letter.currentHealth <= 0:
                    self.letter_list.remove(letter)

            if bullet.bottom > self.window.height:
                bullet.remove_from_sprite_lists()
            
                
        self.background_list.update()
        if self.background1.bottom <= -self.window.height:
            self.background1.center_y = self.window.height + self.background1.height/2 
        
        if self.background2.bottom <= -self.window.height:
            self.background2.center_y = self.window.height + self.background2.height/2
        

    def end_game(self):
        self.window.show_view(views.game_end_view.GameEndView())

    def create_bullet(self):
        bullet = arcade.Sprite("resources/syringe_01.png", .02)
        # arcade.play_sound(self.gun_sound)
        bullet.change_y = 46
        bullet.center_x = playerModel.center_x
        #print(time)
        bullet.bottom = playerModel.center_y + 4 #+40

        # bullet.change_y = 10
        # bullet.center_x = playerModel.center_x
        # bullet.bottom = playerModel.center_y + 40
        return bullet
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            print("space")
            #creation of bullet to add to bullet sprite list
            #self.bullet_list.append(self.create_bullet())
            #self.on_key_release(key,modifiers)
            self.spacePressed = True
        elif key == arcade.key.LEFT:
                self.leftPressed = True
        elif key == arcade.key.RIGHT:
                self.rightPressed = True
        # temporary way to get to end screen: type the letter d
        elif key == arcade.key.D:
            self.end_game()
            
    def on_key_release(self, key, modifiers):
        if key == arcade.key.SPACE:
            print('release')
            self.spacePressed = False
        elif (key == arcade.key.LEFT):
            self.leftPressed = False
        elif (key == arcade.key.RIGHT):
            self.rightPressed = False
