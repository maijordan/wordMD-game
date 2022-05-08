import arcade
from utils.constants import BULLET_DMG, BULLET_IMG, BULLET_IMG_SCALE, BULLET_SPEED, GUN_SOUND, GUN_SOUND_VOL, PT_MULT, SCREEN_HEIGHT


class BulletList:
    """SpriteList wrapper for bullets"""
    
    def __init__(self):
        self.__bulletList = arcade.SpriteList()
        
    @property
    def list(self):
        return self.__bulletList
        
    def draw(self):
        self.__bulletList.draw()
        
    def update(self,letterList,handleRight,handleWrong):
        """Returns total number of points scored by the current bullets"""
        
        self.__bulletList.update()
        
        totPoints = 0
        
        for bullet in self.__bulletList:
            #generate list of all letters that collided with this bullet
            hitList = arcade.check_for_collision_with_list(
                bullet, letterList.letters
            )
            
            if len(hitList) > 0: #check if a collision occured
                bullet.remove_from_sprite_lists()
                for letter in hitList:
                    letter.currentHealth += BULLET_DMG #decrement the letter's health (BULLET_DMG is a neg const)
                if letter.currentHealth <= 0: #check if this letter is dead
                    letterList.remove(letter)
                     
                    totPoints += (letterList.points * PT_MULT) #add points scored
                    
                    #call appropriate handler if current word was finished
                    if(letterList.points > 0):
                        handleRight()
                    if(letterList.isWrong):
                        handleWrong()
                      
            #remove bullet if it moves off screen
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()
                
        return totPoints
    
    def append(self,bullet):
        self.__bulletList.append(bullet)
        
    def createBullet(self,centerX,btm):
        """Creates a bullet at the given center_x and bottom coordinates"""
        bullet = BulletSprite(centerX,btm)
        self.__bulletList.append(bullet)
        arcade.play_sound(GUN_SOUND, GUN_SOUND_VOL)

class BulletSprite(arcade.Sprite):
    """Sprite for bullet img configuration"""
    
    def __init__(self,centerX,btm):
        super().__init__(BULLET_IMG, BULLET_IMG_SCALE)
        
        self.change_y = BULLET_SPEED
        self.center_x = centerX
        self.bottom = btm