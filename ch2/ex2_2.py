###############################################################################
# Exercise
# Use the corpus module to explore austen-persuasion.txt.
# How many word tokens does this book have?
# How many word types?
###############################################################################

# import the corpus containing austen-persuasion.txt
from nltk.corpus import gutenberg

# read the text
text = gutenberg.words('austen-persuasion.txt')

# determine how many word tokens there are
num_tokens = len(text)

# determine how many types (i.e. unique tokens) there are
num_types = len(set(text))

# present the outcome
print('austen-persuasion.txt: tokens=',num_tokens,'types=',num_types)
