from english_words import english_words_lower_alpha_set as wordsSet
import pandas as pd
from random import randint


class WordObject:
    def __init__(self, word):
        self.__ogWord = word
        self.__letters = [l for l in word]
        self.__numInfected = 0
        
    @property
    def letters(self):
        return self.__letters

    def infect(self, lower, upper):
        numToInfect = randint(lower, upper)
        self.__numInfected += numToInfect
        for _ in range(numToInfect):
            idx = randint(0, len(self.__letters))
            letter = chr(randint(0, 25) + ord("a"))
            self.__letters.insert(idx, letter)

    def info(self):
        return (
            self.__ogWord
            + "("
            + str(self.__numInfected)
            + ")"
            + " -> "
            + "".join(self.__letters)
        )

    def __str__(self):
        return "".join(self.__letters) + "(" + str(self.__numInfected) + ")"

    def length(self):
        return len(self.__letters)

    def check(self):
        "returns 1 if is a valid word, 0 if is not a valid word, or -1 if there are still infected letters"
        if self.__numInfected > 0:
            return -1
        return "".join(self.__letters) in wordsSet

    def hitLetter(self, i):
        "removes letter at index i if possible, else returns False"
        if self.__numInfected >= 1:
            self.__letters.pop(i)
            self.__numInfected -= 1
            return True
        return False


class WordGenerator:
    def __init__(self):
        words = list(wordsSet)
        lengths = [len(w) for w in words]
        self.words = pd.DataFrame({"Word": words, "Length": lengths})

    def generateWords(
        self,
        numWords=1,
        shortestLen=3,
        longestLen=5,
        smallestInfected=1,
        largestInfected=1,
    ):
        cleanWords = self.words[self.words.Length.between(shortestLen, longestLen)][
            "Word"
        ].sample(numWords)
        infectedWords = []
        for cw in cleanWords:
            word = WordObject(cw)
            word.infect(smallestInfected, largestInfected)
            infectedWords.append(word)
        return infectedWords


def main():
    """ Main function (for testing) """

    wg = WordGenerator()
    # words = wg.generateWords(20, 3, 10, 1, 2)
    # for w in words:
    #     print(w.info())

    while True:
        word = wg.generateWords(1, 3, 7, 1, 3)[0]
        print("".join(list(map(str, range(word.length())))))
        print(word)

        while word.check() == -1:
            i = int(input())
            word.hitLetter(i)
            print("".join(list(map(str, range(word.length())))))
            print(word)

        print("CORRECT" if word.check() == 1 else "WRONG")
        print()


if __name__ == "__main__":
    main()