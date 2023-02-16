from nltk.corpus import wordnet as wn
import random

#YO MAMA GENERATOR - takes around 5 seconds, oh well

# Generates nouns for the impending joke
all_nouns = []
for synset in wn.all_synsets('n'):
    all_nouns.extend(synset.lemma_names())

# Generates an adjective
all_adj = []
for synset in list(wn.all_synsets(wn.ADJ)):
    all_adj.extend(synset.lemma_names())

adj = random.choice(all_adj).replace('_', ' ')
noun_one = random.choice(all_nouns).replace('_', ' ')
noun_two = random.choice(all_nouns).replace('_', ' ')
compendium = [adj, noun_one, noun_two]


print(f'Yo Mama so {adj}, she thought {noun_one} was {noun_two}')
