import arcade
from constants import BKGRD_SCROLL_SPEED, ROAD_IMG, SCREEN_HEIGHT, SCREEN_WIDTH

class ScrollingBkgrdList:
    def __init__(self):
        self.__backgroundList = arcade.SpriteList()
        
        background1 = BackgroundSprite()
        self.__backgroundList.append(background1)

        background2 = BackgroundSprite()
        background2.center_y = SCREEN_HEIGHT
        self.__backgroundList.append(background2)
        
    def draw(self):
        self.__backgroundList.draw()
        
    def update(self):
        self.__backgroundList.update()
        
        for background in self.__backgroundList:
            if background.bottom <= -SCREEN_HEIGHT:
                background.center_y = SCREEN_HEIGHT + background.height / 2

class BackgroundSprite(arcade.Sprite):
    def __init__(self):
        super().__init__(ROAD_IMG)
        
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.center_x = SCREEN_WIDTH / 2
        self.change_y = BKGRD_SCROLL_SPEED