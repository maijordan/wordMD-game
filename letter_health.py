import arcade

#change to change max health of the letters
maxHealth = 50

class LetterHealth(arcade.Sprite):

    def __init__(self, image, scale):
        super().__init__(image, scale)
        
        self.currentHealth = maxHealth
     
        
    def currentHealthBar(self):
        if self.currentHealth < maxHealth:
            arcade.draw_rectangle_filled(center_x=self.center_x, center_y=self.center_y + 25, width = maxHealth, height = 7, color = arcade.color.RED)
        
        #current bar = (current/max) * maxHealth to get percentage health left
        currentBar = maxHealth * (self.currentHealth/maxHealth)
        
                                    #honestly don't know how -.5 * (maxHealth - currentBar) works
        arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (maxHealth - currentBar), center_y=self.center_y + 25, width = currentBar, height = 7, color = arcade.color.GREEN)