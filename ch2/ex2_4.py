############################################################################
# Exercise 4
# Read in the texts of the State of the Union addresses, using the state_union corpus reader. Count occurrences of men, women, and  people in each document. What has happened to the usage of these words over time?
############################################################################

# import the corpus
import nltk
from nltk.corpus import inaugural

# count occurences of men, woman and people in each document
cfd = nltk.ConditionalFreqDist(
    (target,fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['men','women','people']
    if w.lower() == target
)
cfd.tabulate()
cfd.plot()
