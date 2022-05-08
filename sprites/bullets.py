import arcade
from utils.constants import BULLET_DMG, BULLET_IMG, BULLET_IMG_SCALE, BULLET_SPEED, GUN_SOUND, GUN_SOUND_VOL, PT_MULT, SCREEN_HEIGHT


class BulletList:
    def __init__(self):
        self.__bulletList = arcade.SpriteList()
        
    @property
    def list(self):
        return self.__bulletList
        
    def draw(self):
        self.__bulletList.draw()
        
    def update(self,letterList,handleRight,handleWrong):
        self.__bulletList.update()
        
        totPoints = 0
        
        for bullet in self.__bulletList:
            hitList = arcade.check_for_collision_with_list(
                bullet, letterList.letters
            )
            if len(hitList) > 0:
                bullet.remove_from_sprite_lists()
                for letter in hitList:
                    letter.currentHealth += BULLET_DMG
                if letter.currentHealth <= 0:
                    letterList.remove(letter)
                    #add points 
                    totPoints += (letterList.points * PT_MULT)
                    if(letterList.points > 0):
                        handleRight()
                    if(letterList.isWrong):
                        handleWrong()
                      
                    
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()
                
        return totPoints
    
    def append(self,bullet):
        self.__bulletList.append(bullet)
        
    def createBullet(self,centerX,btm):
        bullet = BulletSprite(centerX,btm)
        self.__bulletList.append(bullet)
        arcade.play_sound(GUN_SOUND, GUN_SOUND_VOL)

class BulletSprite(arcade.Sprite):
    def __init__(self,centerX,btm):
        super().__init__(BULLET_IMG, BULLET_IMG_SCALE)
        
        self.change_y = BULLET_SPEED
        self.center_x = centerX
        self.bottom = btm