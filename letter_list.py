import arcade

from words import WordGenerator
from letter_health import LetterHealth

class LetterList:
    def __init__(self, win_width):
        self.__init_height = 600
        self.__points = 0
        self.__isWrong = False
        self.__tile_spacing = 55
        self.__win_width = win_width

        self.__wg = WordGenerator()
        self.gen_word()
        
    def clear(self):
        self.__points = 0
        self.__isWrong = False
        self.gen_word()

    def gen_word(self):
        self.__letters = arcade.SpriteList()
        self.__word = self.__wg.generateWords(1, 3, 5, 1, 2)[0]
        start = (
            self.__win_width / 2 - (self.__word.length() - 1) * self.__tile_spacing / 2
        )
        offset = 0
        for l in self.__word.letters:
            letter = LetterHealth("resources/letters/zombie_outline_thick/" + l + ".png", 0.25)
            letter.center_x = start + offset
            offset += self.__tile_spacing
            letter.center_y = self.__init_height
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

    def adjust_space(self):
        start = (
            self.__win_width / 2 - (self.__word.length() - 1) * self.__tile_spacing / 2
        )
        offset = 0
        for letter in self.__letters:
            letter.center_x = start + offset
            offset += self.__tile_spacing
            letter.center_y = self.__init_height

    def remove(self, letter):
        self.__points = 0
        self.__isWrong = False
        for i in range(len(self.__letters)):
            if letter == self.__letters[i]:
                self.__word.hitLetter(i)
                check = self.__word.check()
                if check == -1:
                    letter.remove_from_sprite_lists()
                    # self.adjust_space() #recenters letters
                else:
                    if check == 1:
                        print("CORRECT")
                        self.__points = self.__word.getPoints
                        
                    else:
                        print("WRONG")
                        self.__isWrong = True
                    self.gen_word()
                break
     

