import arcade
from constants import LETTER_SPEED,HEALTH_BAR_OFFSET, MAX_LETTER_HEALTH,LETTER_IMG_FOLDER, LETTER_IMG_SCALE, LETTER_SPACING, LETTER_SPAWN_HEIGHT, MAX_INFECTED, MAX_LETTERS, MIN_INFECTED, MIN_LETTERS, SCREEN_HEIGHT, SCREEN_WIDTH
from words import WordGenerator, Status

class LetterList:
    def __init__(self):
        self.__points = 0
        self.__isWrong = False

        self.__wg = WordGenerator()
        self.genWord()

    def genWord(self):
        self.__letters = arcade.SpriteList()
        self.__word = self.__wg.generateWords(1, MIN_LETTERS, MAX_LETTERS, MIN_INFECTED, MAX_INFECTED)[0]
        start = (
            SCREEN_WIDTH / 2 - (self.__word.length() - 1) * LETTER_SPACING / 2
        )
        offset = 0
        for l in self.__word.letters:
            letter = LetterSprite(LETTER_IMG_FOLDER + l + ".png")
            letter.center_x = start + offset
            offset += LETTER_SPACING
            letter.center_y = SCREEN_HEIGHT - LETTER_SPAWN_HEIGHT
            self.__letters.append(letter)
    
    @property
    def letters(self):
        return self.__letters
    
    @property
    def infectedCount(self):
        return self.__word.numInfected
    
    @property
    def points(self):
        return self.__points
    
    @property
    def isWrong(self):
        return self.__isWrong
    
    @property
    def bottom(self):
        for letter in self.__letters:
            return letter.bottom
    
    def draw(self):
        self.__letters.draw()
        for letter in self.__letters:
            #letter move down speed
            letter.center_y += LETTER_SPEED
            letter.drawHealthBar()

    def remove(self, letter):
        self.__points = 0
        self.__isWrong = False
        for i in range(len(self.__letters)):
            if letter == self.__letters[i]:
                self.__word.hitLetter(i)
                check = self.__word.check()
                if check == Status.NOT_DONE:
                    letter.remove_from_sprite_lists()
                else:
                    if check == Status.CORRECT:
                        self.__points = self.__word.points
                    else:
                        self.__isWrong = True
                break
     
class LetterSprite(arcade.Sprite):
    def __init__(self, image):
        super().__init__(image, LETTER_IMG_SCALE)
        
        self.__currentHealth = MAX_LETTER_HEALTH
     
    @property
    def currentHealth(self):
        return self.__currentHealth
    
    @currentHealth.setter
    def currentHealth(self,newHealth):
        self.__currentHealth = newHealth
        
    def drawHealthBar(self):
        if self.__currentHealth < MAX_LETTER_HEALTH:
            arcade.draw_rectangle_filled(center_x=self.center_x, center_y=self.center_y + HEALTH_BAR_OFFSET, width = MAX_LETTER_HEALTH, height = 7, color = arcade.color.RED)
        
        currentBar = MAX_LETTER_HEALTH * (self.__currentHealth/MAX_LETTER_HEALTH)
        
        arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (MAX_LETTER_HEALTH - currentBar), center_y=self.center_y + HEALTH_BAR_OFFSET, width = currentBar, height = 7, color = arcade.color.GREEN)