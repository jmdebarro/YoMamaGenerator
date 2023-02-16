from nltk.corpus import wordnet as wn

#Creates pages with list of nouns and adjectives, just have to write
#the function and the []

# Generates nouns for the impending joke
all_nouns = []
for synset in wn.all_synsets('n'):
    all_nouns.extend(synset.lemma_names())
file_noun = open('nouns.py', 'w')

#Write the nouns files
file_noun.write("import random\ndef noun(): \n\treturn random.choice(nouns).replace('_', ' ')"
                "\n\nnouns = [")
for word in all_nouns[:-1]:
    file_noun.write(f'"{word}", ')
file_noun.write(f'"{all_nouns[-1]}"]')
file_noun.close()

# Generates an adjective
all_adj = []
for synset in list(wn.all_synsets(wn.ADJ)):
    all_adj.extend(synset.lemma_names())
file_adj = open('adjs.py', 'w')

file_adj.write("import random\ndef adjective(): \n\treturn random.choice(adjs).replace('_', ' ')"
                "\n\nadjs = [")
for word in all_adj[:-1]:
    file_adj.write(f'"{word}", ')
file_adj.write(f'"{all_adj[-1]}"]')
file_adj.close()