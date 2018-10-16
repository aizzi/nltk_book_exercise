###############################################################################
# Exercise 5
#
# Investigate the holonym-meronym relations for some nouns. Remember that there are three kinds of holonym-meronym relation, so you need to use: member_meronyms(), part_meronyms(), substance_meronyms(), member_holonyms(), part_holonyms(), and  substance_holonyms().
###############################################################################

# import wordnet
from nltk.corpus import wordnet as wn
import nltk

while True:
    noun = input("Type a noun to research [e to exit]: ")
    if noun == 'e':
        break
    # print all possible meanings
    counter = 1
    print("")
    synsets = wn.synsets(noun)
    num_synsets = len(synsets)
    definitions = [synset.definition() for synset in synsets]
    examples = [synset.examples() for synset in synsets]
    synonims = [synset.lemma_names() for synset in synsets]
    hyponyms = [synset.hyponyms() for synset in synsets]
    hypernyms = [synset.hypernyms() for synset in synsets]
    member_meronyms = [synset.member_meronyms() for synset in synsets]
    part_meronyms = [synset.part_meronyms() for synset in synsets]
    substance_meronyms = [synset.substance_meronyms() for synset in synsets]
    member_holonyms = [synset.member_holonyms() for synset in synsets]
    part_holonyms = [synset.part_holonyms() for synset in synsets]
    substance_holonyms = [synset.substance_holonyms() for synset in synsets]
    #print(definitions, examples, synonims, hyponyms, hypernyms, sep='\n')
    for i in range(num_synsets):
        print("Synset:", synsets[i])
        print("Definition:", definitions[i])
        print("Examples:", examples[i])
        print("Synonims:", synonims[i])
        print("Hyponyms:", hyponyms[i])
        print("Hypernyms:", hypernyms[i])
        print("Member Meronyms:", member_meronyms[i])
        print("Part Meronyms:", part_meronyms[i])
        print("Substance Meronyms:", substance_meronyms[i])
        print("Member Holonyms:", member_holonyms[i])
        print("Part Holonyms:", part_holonyms[i])
        print("Substance Holonyms:", substance_holonyms[i])
        print()
    print("")
