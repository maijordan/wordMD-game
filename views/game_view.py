import arcade
from arcade import gui
from letter_list import LetterList
import views.game_end_view
import views.game_start_view
from style import Style

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

        self.letter_list = LetterList(self.window.width)
        self.bullet_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()

    def setup(self):
        self.letter_list.clear()
        self.bullet_list.clear()
        self.player_list.clear()
        self.background_list.clear()
        
        self.spacePressed = False
        self.rightPressed = False
        self.leftPressed = False
        self.show_infected = False
        self.paused = False
        self.player_points = 0;
        self.background1 = arcade.Sprite("resources/road_01.png")
        self.background1.width = self.window.width
        self.background1.height = self.window.height
        # self.background1.center_y = self.window.height / 2
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
        #DW about this
        # self.secret = arcade.Sprite("resources/secret.png", 0.1)
        # self.secret.center_x = 985
        # self.secret.center_y = 3600
        # self.secret.change_y = -15
        

        playerModel.center_x = self.window.width / 2
        playerModel.center_y = 50
        self.player_list.append(playerModel)
        
        self.lives = 3
        
        self.manager = gui.UIManager()
        self.menu_grp = gui.UIBoxLayout()
        
        resume_btn = gui.UIFlatButton(
            text="Resume", width=200, style=Style.primary_btn
        )
        self.menu_grp.add(resume_btn.with_space_around(bottom=20))
        resume_btn.on_click = self.resume

        restart_btn = gui.UIFlatButton(
            text="Restart", width=200, style=Style.secondary_btn
        )
        self.menu_grp.add(restart_btn.with_space_around(bottom=20))
        restart_btn.on_click = self.restart

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
        
        
    def resume(self,event):
        self.paused = not self.paused
        
    def restart(self,event):
        self.setup()
    
    def open_start(self,event):
        self.manager.disable()
        self.window.show_view(views.game_start_view.GameStartView())
    
    def quit(self,event):
        arcade.exit()
        

    def on_show(self):
        self.setup()


    def on_draw(self):
        self.clear()

        self.background_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

        if not self.paused:
            self.letter_list.letters.draw()
            for letter in self.letter_list.letters:
                letter.currentHealthBar()
                        
        arcade.draw_lrtb_rectangle_filled(self.window.width - 130, self.window.width - 42, self.window.height - 10, self.window.height - 80, arcade.csscolor.DARK_SLATE_GRAY)
        arcade.draw_lrtb_rectangle_outline(self.window.width - 130, self.window.width - 42, self.window.height - 10, self.window.height - 80, arcade.csscolor.WHITE, 3)

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
        
        arcade.draw_lrtb_rectangle_filled(42, 130, self.window.height - 10, self.window.height - 80, arcade.csscolor.DARK_SLATE_GRAY)
        arcade.draw_lrtb_rectangle_outline(42, 130, self.window.height - 10, self.window.height - 80, arcade.csscolor.WHITE, 3)

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
            self.player_points,
            86,
            self.window.height - 67,
            arcade.csscolor.WHITE_SMOKE,
            font_size=18,
            anchor_x="center",
            font_name="Kenney High"
        )
        
        if not self.paused and self.show_infected:
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
                self.letter_list.infectedCount,
                self.window.width / 2,
                self.window.height / 2 - 100,
                arcade.make_transparent_color(arcade.color.ARSENIC, 200),
                font_size=200,
                anchor_x="center",
                font_name="Kenney High"
            )
            
        if self.paused:
            arcade.draw_lrtb_rectangle_filled(0, self.window.width, self.window.height, 0, arcade.make_transparent_color(arcade.csscolor.DARK_SLATE_GRAY, 100))
            self.manager.enable()
            self.manager.draw()
        else:
            self.manager.disable()
            
            

    def on_update(self, delta_time):
        if self.paused:
            return
        # self.secret.update()
        # if self.secret.top <=0:
        #     self.secret.center_y = 4000
        self.bullet_list.update()
        if self.spacePressed:
            bullet = self.create_bullet()
            # bullet.change_y = 1
            # bullet.center_x = self.player_model.center_x
            # bullet.bottom = self.player_model.center_y + 45
            # bullet sound annoying
            self.bullet_list.append(bullet)
            arcade.play_sound(gunSound, 0.25)
        if self.leftPressed:
            if (playerModel.center_x - playerModel.width/2) - playerMovementSpeed < leftBarrier:
                #play sound
                print("don't do it")
            else:
                playerModel.center_x += -playerMovementSpeed
        if self.rightPressed:
            if (playerModel.center_x + playerModel.width/2) + playerMovementSpeed > rightBarrier:
                #play sound
                print("don't do it")
            else:
                playerModel.center_x += playerMovementSpeed
                
        for letter in self.letter_list.letters:
            #letter move down speed
            letter.center_y += letterMovementSpeed
        
        #for loop to check for when letter reaches the player height
        for letter in self.letter_list.letters:
            if(letter.bottom < playerModel.center_y + playerModel.height/2):
                #self.letter_list.remove(letter)
                self.letter_list.gen_word()
                arcade.play_sound(incorrectSound)
                self.die()
                break
                
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(
                bullet, self.letter_list.letters
            )
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                for letter in hit_list:
                    # change to change the amount of damage each syringe does
                    letter.currentHealth += bulletDamage
                if letter.currentHealth <= 0:
                    self.letter_list.remove(letter)
                    #add points 
                    self.player_points += (self.letter_list.getPoints * 100)
                    if(self.letter_list.getPoints > 0):
                        arcade.play_sound(correctSound)
                    if(self.letter_list.isWrong):
                        arcade.play_sound(incorrectSound)
                        self.die()
                      
                    

            if bullet.bottom > self.window.height:
                bullet.remove_from_sprite_lists()

        self.background_list.update()
        if self.background1.bottom <= -self.window.height:
            self.background1.center_y = self.window.height + self.background1.height / 2

        if self.background2.bottom <= -self.window.height:
            self.background2.center_y = self.window.height + self.background2.height / 2

    def die(self):
        self.lives -= 1
        if self.lives == 0:
            file = open("scores.txt", "a")
            file.write(str(self.player_points) + ",")
            file.close()
            self.window.show_view(views.game_end_view.GameEndView())

    def create_bullet(self):
        bullet = arcade.Sprite("resources/syringe_01.png", 0.02)
        # arcade.play_sound(self.gun_sound)
        bullet.change_y = 46
        bullet.center_x = playerModel.center_x
        # print(time)
        bullet.bottom = playerModel.center_y + 4  # +40

        # bullet.change_y = 10
        # bullet.center_x = playerModel.center_x
        # bullet.bottom = playerModel.center_y + 40
        return bullet

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.paused = not self.paused
            self.spacePressed = False
            self.leftPressed = False
            self.rightPressed = False
            self.show_infected = False
        elif key == arcade.key.SPACE:
            #creation of bullet to add to bullet sprite list
            #self.bullet_list.append(self.create_bullet())
            #self.on_key_release(key,modifiers)
            self.spacePressed = True
        elif key == arcade.key.LEFT:
            self.leftPressed = True
        elif key == arcade.key.RIGHT:
            self.rightPressed = True
        elif key == arcade.key.LSHIFT:
            self.show_infected = True

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
            self.show_infected = False
    
  