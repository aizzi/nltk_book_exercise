###############################################################################
# Exercise 2.3
# Use the Brown corpus reader nltk.corpus.brown.words() or the Web text corpus reader nltk.corpus.webtext.words() to access some sample text in two different genres.
###############################################################################

# import the brown corpus
from nltk.corpus import brown

# List all generes in the corpus
categories = brown.categories()

while True:
    print("\nAvailable Categories")
    n=0
    for cat in categories:
        print(str(n)+')',cat)
        n = n+1
    print("CTRL-C to exit")
    cat = input("Choose a category: ")
    category = categories[int(cat)]
    print("Chosen category:",category)
    sentence = brown.sents(categories=category)[0]
    print(' '.join(sentence))
