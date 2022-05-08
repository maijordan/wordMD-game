import arcade

from utils.constants import LEFT_BARRIER, PLAYER_IMG, PLAYER_IMG_SCALE, PLAYER_SPEED, RIGHT_BARRIER, SCREEN_WIDTH

class PlayerList:
    def __init__(self):
        self.__playerList = arcade.SpriteList()
        self.__playerModel = PlayerSprite()
        self.__playerList.append(self.__playerModel)
        
    @property
    def centerX(self):
        return self.__playerModel.center_x
    
    @property
    def centerY(self):
        return self.__playerModel.center_y
    
    @property
    def top(self):
        return self.__playerModel.top
        
    def draw(self):
        self.__playerList.draw()
        
    def move(self,dir):
        if LEFT_BARRIER <= (self.__playerModel.center_x + dir * self.__playerModel.width/2) + PLAYER_SPEED * dir <= RIGHT_BARRIER:
            self.__playerModel.center_x += PLAYER_SPEED * dir
        
class PlayerSprite(arcade.Sprite):
    def __init__(self):
        super().__init__(PLAYER_IMG, PLAYER_IMG_SCALE)
        
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = 50