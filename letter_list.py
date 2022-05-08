import arcade
from constants import CORRECT, LETTER_IMG_FOLDER, LETTER_IMG_SCALE, LETTER_SPACING, LETTER_SPAWN_HEIGHT, MAX_INFECTED, MAX_LETTERS, MIN_INFECTED, MIN_LETTERS, NOT_DONE

from words import WordGenerator
from letter_health import LetterHealth

class LetterList:
    def __init__(self, winWidth, winHeight):
        self.__points = 0
        self.__isWrong = False
        self.__winWidth = winWidth
        self.__winHeight = winHeight

        self.__wg = WordGenerator()
        self.genWord()

    def genWord(self):
        self.__letters = arcade.SpriteList()
        self.__word = self.__wg.generateWords(1, MIN_LETTERS, MAX_LETTERS, MIN_INFECTED, MAX_INFECTED)[0]
        start = (
            self.__winWidth / 2 - (self.__word.length() - 1) * LETTER_SPACING / 2
        )
        offset = 0
        for l in self.__word.letters:
            letter = LetterHealth(LETTER_IMG_FOLDER + l + ".png", LETTER_IMG_SCALE)
            letter.center_x = start + offset
            offset += LETTER_SPACING
            letter.center_y = self.__winHeight - LETTER_SPAWN_HEIGHT
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

    def remove(self, letter):
        self.__points = 0
        self.__isWrong = False
        for i in range(len(self.__letters)):
            if letter == self.__letters[i]:
                self.__word.hitLetter(i)
                check = self.__word.check()
                if check == NOT_DONE:
                    letter.remove_from_sprite_lists()
                else:
                    if check == CORRECT:
                        self.__points = self.__word.points
                        
                    else:
                        self.__isWrong = True
                    self.genWord()
                break
     

