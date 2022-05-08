import arcade
from utils.constants import LETTER_SPEED,HEALTH_BAR_OFFSET, MAX_LETTER_HEALTH,LETTER_IMG_FOLDER, LETTER_IMG_SCALE, LETTER_SPACING, LETTER_SPAWN_HEIGHT, MAX_INFECTED, MAX_LETTERS, MIN_INFECTED, MIN_LETTERS, SCREEN_HEIGHT, SCREEN_WIDTH
from utils.word_utils import WordGenerator, Status

class LetterList:
    """SpriteList wrapper for letters"""
    
    def __init__(self):
        self.__points = 0
        self.__isWrong = False

        self.__wg = WordGenerator()
        self.genWord()

    def genWord(self):
        """Generates a new word (list of letters) and resets the word's position"""
        
        self.__letters = arcade.SpriteList()
        self.__word = self.__wg.generateWords(1, MIN_LETTERS, MAX_LETTERS, MIN_INFECTED, MAX_INFECTED)[0] #gets an single word
        
        #calculate position of first letter in the infected word (all positions will ref this)
        start = SCREEN_WIDTH / 2 - (self.__word.length - 1) * LETTER_SPACING / 2
        offset = 0
        
        #gen a sprite for each letter of the word (in the correct position)
        for l in self.__word.letters:
            letter = LetterSprite(LETTER_IMG_FOLDER + l + ".png",start + offset)
            offset += LETTER_SPACING
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
        #for loop used because can't index into a spritelist
        for letter in self.__letters:
            return letter.bottom
    
    def draw(self):
        #draw letters
        self.__letters.draw()
        for letter in self.__letters:
            #move letters down
            letter.center_y += LETTER_SPEED
            
            #draw letter health bars
            letter.drawHealthBar()

    def remove(self, letter):
        """Removes the given letter from the list and checks if the word is done and correct"""
        
        self.__points = 0
        self.__isWrong = False
        
        #loop to find target letter
        for i in range(len(self.__letters)):
            if letter == self.__letters[i]:
                self.__word.hitLetter(i) #removes letter from underlying word obj
                check = self.__word.check() #get status of underlying word obj
                if check == Status.NOT_DONE:
                    #if there are still letters to remove, just remove this letter and continue
                    letter.remove_from_sprite_lists()
                else:
                    #if the word is done, award points or indicate an incorrect configuration
                    if check == Status.CORRECT:
                        self.__points = self.__word.points
                    else:
                        self.__isWrong = True
                break
     
class LetterSprite(arcade.Sprite):
    """Sprite for letter img configuration and health bar info"""
    
    def __init__(self, image,centerX):
        super().__init__(image, LETTER_IMG_SCALE)
        
        self.center_x = centerX
        self.center_y = SCREEN_HEIGHT - LETTER_SPAWN_HEIGHT
        
        self.__currentHealth = MAX_LETTER_HEALTH
     
    @property
    def currentHealth(self):
        return self.__currentHealth
    
    @currentHealth.setter
    def currentHealth(self,newHealth):
        self.__currentHealth = newHealth
        
    def drawHealthBar(self):
        #if damage has been done, draw a red background rectangle
        if self.__currentHealth < MAX_LETTER_HEALTH:
            arcade.draw_rectangle_filled(center_x=self.center_x, center_y=self.center_y + HEALTH_BAR_OFFSET, width = MAX_LETTER_HEALTH, height = 7, color = arcade.color.RED)
        
        #draw the current health percentage as a green foreground rectangle
        currentBar = MAX_LETTER_HEALTH * (self.__currentHealth/MAX_LETTER_HEALTH)
        arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (MAX_LETTER_HEALTH - currentBar), center_y=self.center_y + HEALTH_BAR_OFFSET, width = currentBar, height = 7, color = arcade.color.GREEN)