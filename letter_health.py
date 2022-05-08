import arcade

from constants import HEALTH_BAR_OFFSET, MAX_LETTER_HEALTH
class LetterHealth(arcade.Sprite):

    def __init__(self, image, scale):
        super().__init__(image, scale)
        
        self.currentHealth = MAX_LETTER_HEALTH
     
        
    def currentHealthBar(self):
        if self.currentHealth < MAX_LETTER_HEALTH:
            arcade.draw_rectangle_filled(center_x=self.center_x, center_y=self.center_y + HEALTH_BAR_OFFSET, width = MAX_LETTER_HEALTH, height = 7, color = arcade.color.RED)
        
        currentBar = MAX_LETTER_HEALTH * (self.currentHealth/MAX_LETTER_HEALTH)
        
        arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (MAX_LETTER_HEALTH - currentBar), center_y=self.center_y + HEALTH_BAR_OFFSET, width = currentBar, height = 7, color = arcade.color.GREEN)