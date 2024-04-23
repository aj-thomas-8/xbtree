import nltk

from nltk.corpus import brown
from nltk.tag import pos_tag

def get_tense(verb_pair):
    match verb_pair[1]:
        case "VBD":
            return ("[PAST]", "T")
        case _:
            return ("[PRES]", T)

def simplify(pair):
    match pair[1]:
        case "NNP" | "NN" | "NNS" | "PRP":
            return (pair[0], "N")
        case "VBD":
            return (pair[0], "V")
        case "RB":
            return (pair[0], "Adv")
        case "DT" | "PRP$":
            return (pair[0], "D")
        case "IN":
            return (pair[0], "P")
        case _:
            # treaiing default as noun
            return (pair[0], "Unk")

def simplify_tags(tagged_sent):
    simplified_sent = []
    updated_tense = 0

    for i in range(0, len(tagged_sent)):
        # use regular expressions to match verb tags here
        if tagged_sent[i][1] == "VBD":
            tense = get_tense(tagged_sent[i])
            for j in range(updated_tense, len(simplified_sent)):
                if (simplified_sent[j][1] == "Adv"):
                    simplified_sent.insert(j, tense)
                    updated_tense = len(simplified_sent) + 1
                    # Important: do not add more than 1 tense term per verb
                    break

            if (updated_tense < len(simplified_sent)):
                simplified_sent.append(tense)
                updated_tense = len(simplified_sent) + 1

        simplified_sent.append(simplify(tagged_sent[i]))

    return simplified_sent

def write_csv(xbar_tagged_sent):
    with open("new_sentence.csv", "w") as file:
        for item in xbar_tagged_sent:
            file.write(str(item[0]) + "," + str(item[1]) +  "\n")

def tag(sent):
    #Train Unigram Tagger on Brown Corpus
    #brown_tagged_sents = brown.tagged_sents(categories='news')

    #some predefined sentence 'sent'

    #setup the unigram tagger
    #unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)

    #do all the steps necessary to get the tagger working here (training etc)
    tokens = nltk.word_tokenize(sent)

    #use the tagger on the sentence 'sent'
    tagged_sent = pos_tag(tokens)

    simpl_tags = simplify_tags(tagged_sent)
    
    # Write to CSV file
    write_csv(simpl_tags)

    #print 'sent'
    return simpl_tags

#print(tag("I kicked an elephant in my pajamas"))
print(tag("John suddenly hit a car"))
