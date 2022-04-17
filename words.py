from english_words import english_words_lower_alpha_set as wordsSet
import pandas as pd
from random import randint


class WordObject:
    def __init__(self, word):
        self.__ogWord = word
        self.__letters = [l for l in word]
        self.__numInfected = 0

    def infect(self, lower, upper):
        numToInfect = randint(lower, upper)
        self.__numInfected += numToInfect
        for _ in range(numToInfect):
            idx = randint(0, len(self.__letters))
            letter = chr(randint(0, 25) + ord("a"))
            self.__letters.insert(idx, letter)

    def __str__(self):
        return (
            self.__ogWord
            + "("
            + str(self.__numInfected)
            + ")"
            + " -> "
            + "".join(self.__letters)
        )


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
    words = wg.generateWords(20, 3, 10, 1, 2)
    for w in words:
        print(w)


if __name__ == "__main__":
    main()