import arcade

from words import WordGenerator
from letter_health import LetterHealth

class LetterList:
    def __init__(self, winWidth):
        self.__height = 600
        self.__points = 0
        self.__isWrong = False
        self.__tileSpacing = 55
        self.__winWidth = winWidth

        self.__wg = WordGenerator()
        self.genWord()

    def genWord(self):
        self.__letters = arcade.SpriteList()
        self.__word = self.__wg.generateWords(1, 3, 5, 1, 2)[0]
        start = (
            self.__winWidth / 2 - (self.__word.length() - 1) * self.__tileSpacing / 2
        )
        offset = 0
        for l in self.__word.letters:
            letter = LetterHealth("resources/letters/zombie/" + l + ".png", 0.25)
            letter.center_x = start + offset
            offset += self.__tileSpacing
            letter.center_y = self.__height
            self.__letters.append(letter)
    
    @property
    def letters(self):
        return self.__letters
    
    @property
    def infectedCount(self):
        return self.__word.numInfected
    
    @property
    def getPoints(self):
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
                if check == -1:
                    letter.remove_from_sprite_lists()
                else:
                    if check == 1:
                        self.__points = self.__word.getPoints
                        
                    else:
                        self.__isWrong = True
                    self.genWord()
                break
     

