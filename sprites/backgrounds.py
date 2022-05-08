import arcade
from utils.constants import BKGRD_SCROLL_SPEED, ROAD_IMG, SCREEN_HEIGHT, SCREEN_WIDTH

class ScrollingBkgrdList:
    """SpriteList wrapper for road scrolling animation"""

    def __init__(self):
        self.__backgroundList = arcade.SpriteList()
        
        background1 = BackgroundSprite()
        self.__backgroundList.append(background1)

        background2 = BackgroundSprite()
        background2.center_y = SCREEN_HEIGHT #start second background at halfway position to simulate continuous scroll
        self.__backgroundList.append(background2)
        
    def draw(self):
        self.__backgroundList.draw()
        
    def update(self):
        self.__backgroundList.update()
        
        for background in self.__backgroundList:
            #if background sprite has scrolled all the way to the bottom, reset it to the top
            if background.bottom <= -SCREEN_HEIGHT:
                background.bottom = SCREEN_HEIGHT

class BackgroundSprite(arcade.Sprite):
    """Sprite for road background img configuration"""
    
    def __init__(self):
        super().__init__(ROAD_IMG)
        
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.center_x = SCREEN_WIDTH / 2
        self.change_y = BKGRD_SCROLL_SPEED