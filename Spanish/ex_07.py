"""
Python 2023 Assignment 07
"""

# IMPORTANT: assign the parts of your name and your student ID to these variables!
first_name = "Dmitry"
family_name = "Sukhotin"
student_id = "6688071"

# all inflected forms of 'ser'
conj_ser = {"sersiendo", "sido", "sidasidos", "sidas", "soy", "eres", "sos", "es", "somos", "sois", "son", "era",
            "eras", "era", "éramos", "erais", "eran", "fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron", "seré",
            "serás", "será", "seremos", "seréis", "serán", "sería", "serías", "sería", "seríamos", "seríais", "serían",
            "sea", "seas", "sea", "seamos", "seáis", "sean", "fuera", "fueras", "fuera", "fuéramos", "fuerais",
            "fueran", "fuese", "fueses", "fuese", "fuésemos", "fueseis", "fuesen", "fuere", "fueres", "fuere",
            "fuéremos", "fuereis", "fueren", "sé", "sea", "seamos", "sed", "sean"}


# all inflected forms of 'estar'
conj_estar = {"estar", "estando", "estado", "estada", "estados", "estadas", "estoy", "estás", "está", "estamos",
              "estáis", "están", "estaba", "estabas", "estaba", "estábamos", "estabais", "estaban", "estuve",
              "estuviste", "estuvo", "estuvimos", "estuvisteis", "estuvieron", "estaré", "estarás", "estará",
              "estaremos", "estaréis", "estarán", "estaría", "estarías", "estaría", "estaríamos", "estaríais",
              "estarían", "esté", "estés", "esté", "estemos", "estéis", "estén", "estuviera", "estuvieras", "estuviera",
              "estuviéramos", "estuvierais", "estuvieran",  "estuviese", "estuvieses", "estuviese", "estuviésemos",
              "estuvieseis", "estuviesen", "estuviere", "estuvieres", "estuviere", "estuviéremos", "estuviereis",
              "estuvieren", "está", "esté", "estemos", "estad", "estén"}


def load_sentences(filename):
    """Loads sentences with POS tag from file.
    :param filename: Name of the file with the sentences, one sentence per line.
    :return: List of the sentences from the file, each represented by a list of (form,pos) tuples
    """
    sentences = []
    with open(filename, 'r') as f:
        for line in f:
            tokens_and_tags = line.strip().split()
            sentence = []
            for token_and_tag in tokens_and_tags:
                word, tag = token_and_tag.split('_')
                sentence.append((word, tag))

            sentences.append(sentence)

    return sentences
    # pass


def lemmatize(adj):
    """Naive Spanish adjective lemmatizer.
    :param adj: The adjective to be lemmatized.
    :return: The lemma form of the adjective.
    """
    if adj.endswith("o"):
        return adj  
    elif adj.endswith("os"):
        return adj[:-1]  
    elif adj.endswith("a"):
        if adj.endswith("esa"):
            return adj[:-3] + "és"
        else:
            return adj[:-1] + "o"  
    elif adj.endswith("as"):
        if adj.endswith("esas"):
            return adj[:-4] + "és"
        else:
            return adj[:-2] + "o"  


    elif adj.endswith("es"):
        if adj[-3:] in ["les", "res", "nes"]:
            if adj[-4] == "b":
                return adj[:-1]
            else:
                return adj[:-2]
        elif adj.endswith("ces"):
            return adj[:-3] + "z"
        else:
            if adj.endswith("eses"):
                return adj[:-4] + "és"
            else:
                return adj[:-1]

    return adj
    #pass


def count_occurrences(sentences):
    """Counts occurrences of adjectives as complements to forms of "ser" and "estar"
    :param sentences: A list of sentences, each represented by a list of (form,pos) tuples.
    :return: Two dictionaries (freq_ser,freq_estar) representing the counts of adjective lemmas following forms of ser and estar in the sentences.
    """
    freq_ser = {}  # Dictionary to store adjective-ser counts
    freq_estar = {}  # Dictionary to store adjective-estar counts

    for sent in sentences:
        for i in range(1, len(sent)):
            (word, tag) = sent[i]
            previous_word, previous_tag = sent[i - 1]
            
            if tag == "ADJ" and previous_tag == "AUX" and (previous_word in conj_ser or previous_word in conj_estar):
        
                lemma = lemmatize(word)
                if lemma not in freq_ser or lemma not in freq_estar:
                    freq_ser[lemma] = 0
                    freq_estar[lemma] = 0
                    
                if lemma in freq_ser and previous_word in conj_ser:
                    freq_ser[lemma] += 1

                elif lemma in freq_estar and previous_word in conj_estar:
                    freq_estar[lemma] += 1


    return freq_ser, freq_estar
    # pass


def get_occurrence_sets(freq_ser, freq_estar):
    """Extracts a partition of adjectives by well-attested co-occurrence with "ser" and "estar"
    :param freq_ser: A dictionary mapping adjective lemmas into the number of times each adjective occurred after forms of "ser".
    :param freq_estar: A dictionary mapping adjective lemmas into the number of times each adjective occurred after forms of "ser".
    :return: Tuple of three sets (ser, estar, both) partitioning the adjectives with frequency >= 10 into the copulas they are attested with more than once.
    """
    ser_set = set()
    estar_set = set()
    both_set = set()

    for adjective, count_ser in freq_ser.items():
        count_estar = freq_estar.get(adjective, 0)

        total_occurrences = count_ser + count_estar

        
        if total_occurrences >= 10:
            if count_ser >= 2 and count_estar >= 2:
                both_set.add(adjective)
            elif count_ser >= 2:
                ser_set.add(adjective)
            elif count_estar >= 2:
                estar_set.add(adjective)

    return ser_set, estar_set, both_set
    pass


if __name__ == '__main__':
    #sentences = load_sentences("spanish-tagged-spacy.txt")
    #freq_ser, freq_estar = count_occurrences(sentences)
    #ser, estar, both = get_occurrence_sets(freq_ser, freq_estar)
    #print("ser:\n====\n" + "\n".join(sorted(ser)) + "\n")
    #print("estar:\n====\n" + "\n".join(sorted(estar)) + "\n")
    #print("both:\n====\n" + "\n".join(sorted(both)) + "\n")
    pass


# filename = "/Users/dmitrijsuhotin/Desktop/hw7/spanish-tagged-spacy.txt"


