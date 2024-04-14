import nltk
from nltk.corpus import brown

#Train Unigram Tagger on Brown Corpus
brown_tagged_sents = brown.tagged_sents(categories='news')

#some predefined sentence 'sent'
sent = "I really like cats"

#setup the unigram tagger
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)

#do all the steps necessary to get the tagger working here (training etc)
tokens = nltk.word_tokenize(sent)

#use the tagger on the sentence 'sent'
tagged_sent = unigram_tagger.tag(tokens)

#print 'sent'
print(tagged_sent)


