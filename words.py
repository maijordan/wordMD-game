from english_words import english_words_lower_alpha_set as words_set
import pandas as pd

# creating data frame
words = []
lengths = []
for w in words_set:
    words.append(w)
    lengths.append(len(w))
words = pd.DataFrame({"Word": words, "Length": lengths})

# example of data frame use
five = words[words.Length == 5]

# to see contents of a df in VSCode: add a breakpoint below and debug, in debug console, enter the df name
print("done but not really")
