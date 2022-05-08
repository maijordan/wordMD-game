from enum import Enum
from english_words import english_words_lower_alpha_set as wordsSet
import pandas as pd
from random import randint
class Status(Enum):
    NOT_DONE = -1
    CORRECT = 1
    INCORRECT = 0

class WordObject:
    def __init__(self, word):
        self.__ogWord = word
        self.__letters = [l for l in word]
        self.__numInfected = 0
        self.__points = 0
        
    @property
    def points(self):
        return self.__points
        
    @property
    def letters(self):
        return self.__letters
    
    @property
    def numInfected(self):
        return self.__numInfected

    def infect(self, lower, upper):
        numToInfect = randint(lower, upper)
        self.__points += numToInfect
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
            return Status.NOT_DONE
        return Status.CORRECT if "".join(self.__letters) in wordsSet else Status.INCORRECT

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