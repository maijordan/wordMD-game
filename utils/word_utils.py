from enum import Enum
from english_words import english_words_lower_alpha_set as wordsSet
import pandas as pd
from random import randint
class Status(Enum):
    """Enum for status of a word obj"""

    NOT_DONE = -1 #indicates that there are still infected letters to remove
    CORRECT = 1 #indicates that the remaining letters form a valid word
    INCORRECT = 0 #indicates that the remaining letters form an invalid word

class WordObject:
    """Holds original word, current letters, number of remaining infected letters, and number of points possible"""
    
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
        """Inserts x infected letters into the current word; x randomly chosen from the inclusive range [lower,upper]"""
        numToInfect = randint(lower, upper)
        self.__points += numToInfect #keeps track of max num of infected letters
        self.__numInfected += numToInfect #keeps track of cur num of infected letters (this will decrement when letters are removed)
        for _ in range(numToInfect):
            idx = randint(0, len(self.__letters))
            letter = chr(randint(0, 25) + ord("a"))
            self.__letters.insert(idx, letter)

    def info(self): #for debugging
        return (
            self.__ogWord
            + "("
            + str(self.__numInfected)
            + ")"
            + " -> "
            + "".join(self.__letters)
        )

    def __str__(self): #for debugging
        return "".join(self.__letters) + "(" + str(self.__numInfected) + ")"

    @property
    def length(self):
        return len(self.__letters)

    def check(self):
        """Returns status of word (see Status Enum)"""
        if self.__numInfected > 0:
            return Status.NOT_DONE
        return Status.CORRECT if "".join(self.__letters) in wordsSet else Status.INCORRECT

    def hitLetter(self, i):
        """Removes letter at index i if possible, else returns false"""
        if self.__numInfected >= 1:
            self.__letters.pop(i)
            self.__numInfected -= 1
            return True
        return False


class WordGenerator:
    """Generates infected words"""

    def __init__(self):
        #inserts all words into database so they can be sampled based on length
        words = [w for w in wordsSet if w.isalpha()]
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
        """Returns array of WordObjects of len numWords, each with [shortestLen,longestLen] original letters and [smallestInfected,largestInfected] infected letters"""

        #query database for words of appropriate length
        cleanWords = self.words[self.words.Length.between(shortestLen, longestLen)][
            "Word"
        ].sample(numWords) 
        
        infectedWords = []
        for cw in cleanWords:
            #create WordObject and insert infected letters
            word = WordObject(cw)
            word.infect(smallestInfected, largestInfected)
            infectedWords.append(word)
            
        return infectedWords