import arcade

from words import WordGenerator


class LetterList:
    def __init__(self, win_width):
        self.__height = 600

        self.__tile_spacing = 65
        self.__win_width = win_width

        self.__wg = WordGenerator()
        self.gen_word()

    def gen_word(self):
        self.__letters = arcade.SpriteList()
        self.__word = self.__wg.generateWords(1, 3, 7, 1, 3)[0]
        start = (
            self.__win_width / 2 - (self.__word.length() - 1) * self.__tile_spacing / 2
        )
        offset = 0
        for l in self.__word.letters:
            letter = arcade.Sprite("resources/letters/" + l + ".png", 0.25)
            letter.center_x = start + offset
            offset += self.__tile_spacing
            letter.center_y = self.__height
            self.__letters.append(letter)

    @property
    def letters(self):
        return self.__letters

    def adjust_space(self):
        start = (
            self.__win_width / 2 - (self.__word.length() - 1) * self.__tile_spacing / 2
        )
        offset = 0
        for letter in self.__letters:
            letter.center_x = start + offset
            offset += self.__tile_spacing
            letter.center_y = self.__height

    def remove(self, letter):
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
                    else:
                        print("WRONG")
                    self.gen_word()
                break
