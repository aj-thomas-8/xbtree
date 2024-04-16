import nltk
from nltk.corpus import brown

def tag(sent):
	#Train Unigram Tagger on Brown Corpus
	brown_tagged_sents = brown.tagged_sents(categories='news')

	#some predefined sentence 'sent'

	#setup the unigram tagger
	unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)

	#do all the steps necessary to get the tagger working here (training etc)
	tokens = nltk.word_tokenize(sent)

	#use the tagger on the sentence 'sent'
	tagged_sent = unigram_tagger.tag(tokens)

	#print 'sent'
	return tagged_sent

# print(tag("I fought the man"))


