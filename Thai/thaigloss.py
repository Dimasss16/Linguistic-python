import csv
input_file = "/Users/dmitrijsuhotin/Desktop/python_hw/Thai_transl/th-eng-dict.tsv"


def read_file_to_dict(input_file):
    """
    Read in the contents of the input file in such a way 
    that you can retrieve the contents of columns 2, 3, and 4 
    by the (unique) values in column 1.

    :param input_file: Directory of the text file which contains Thai-English 
    dictionary consisting of 4 columns which represent Thai lexicon, 
    its transcription, category and glosses
    :type input_file: str
    :return: th_eng_dict: Thai-English dictionary
    :rtype: dict{str: (str, str, str)}
    """
    thai_dict = {}
    
    with open(input_file) as fd:
        rd = csv.reader(fd, delimiter="\t", quotechar='"')
        for row in rd:
            word, translit, pos, mean = row
            thai_dict[word] = (translit, pos, mean)
        
    return thai_dict


def simple_tokenizer(th_dict, sentence):
    """
    Simple tokenizer, transliterator, part-of-speech tagger and glosser 
    that correctly analyses the example text based on the dictionary data.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of tuples of format 
    (Thai token, transliteration, POS, English glosses)
    :rtype: list[tuple(str, str, str, str)]
    """
    
    current_token = ""
    list_of_tuples = []
    for letter in sentence:
        current_token += letter
        if current_token in th_dict:
            transl, pos, mean = th_dict[current_token]
            list_of_tuples.append((current_token, transl, pos, mean))
            current_token = ""
    return list_of_tuples


def th_tokens(th_dict, sentence):
    """
    Get the tokens of the Thai sentence using simple tokenizer.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of tokens
    :rtype: list[str]
    """
    tokens = []
    for token in simple_tokenizer(th_dict , sentence):
        tokens.append(token[0])
    
    return tokens


def th_translit(th_dict, sentence):
    """
    Get the transliteration of Thai sentence tokens using simple tokenizer.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of transliterations
    :rtype: list[str]
    """
    translit = []
    for tupl in simple_tokenizer(th_dict , sentence):
        translit.append(tupl[1])
    
    return translit


def th_pos(th_dict, sentence):
    """
    Get the list of part of speech tags 
    of Thai sentence tokens using simple tokenizer.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of POS tags
    :rtype: list[str]
    """
    pos = []
    for tupl in simple_tokenizer(th_dict , sentence):
        pos.append(tupl[2])
    return pos


def th_gloss(th_dict, sentence):
    """
    Get the English glosses of Thai sentence tokens using simple tokenizer.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of English glosses
    :rtype: list[str]
    """
    gloss = []
    for tupl in simple_tokenizer(th_dict , sentence):
        gloss.append(tupl[3])
    return gloss


def greedy_tokenizer(th_dict, sentence):
    list_of_tuples = []
    found_word = False

    while len(sentence) > 0 and not found_word:
        for i in range(len(sentence), 0, -1):
            current_word = sentence[:i]
            if current_word in th_dict:
                transl, pos, mean = th_dict[current_word]
                list_of_tuples.append((current_word, transl, pos, mean))

                # Restart the loop after finding a matching word
                #found_word = True
                sentence = sentence[i:]
                break
            else:
                continue

        if sentence in th_dict:
            transl, pos, mean = th_dict[sentence]
            list_of_tuples.append((sentence, transl, pos, mean))
            found_word = True
    
    return list_of_tuples



def th_tokens_greedy(th_dict, sentence):
    """
    Get the tokens of Thai sentence using greedy tokenizer.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of tokens
    :rtype: list[str]
    """
    greedy_tokens = []
    for word in greedy_tokenizer(th_dict, sentence):
        greedy_tokens.append(word[0])
    return greedy_tokens


def th_translit_greedy(th_dict, sentence):
    """
    Get the transliteration of Thai sentence tokens using greedy tokenizer.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of transliterations
    :rtype: list[str]
    """
    greedy_translit = []
    for word in greedy_tokenizer(th_dict, sentence):
        greedy_translit.append(word[1])
    return greedy_translit


def th_pos_greedy(th_dict, sentence):
    """
    Get the part of speech tags of Thai sentence tokens using greedy tokenizer.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of POS tags
    :rtype: list[str]
    """
    greedy_pos = []
    for word in greedy_tokenizer(th_dict, sentence):
        greedy_pos.append(word[2])
    return greedy_pos


def th_gloss_greedy(th_dict, sentence):
    """
    Get the English glosses of Thai sentence tokens using greedy tokenizer.

    :param th_dict: Thai dictionary
    :type th_dict: dict
    :param sentence: Thai sentence
    :type sentence: str
    :return: list of English glosses
    :rtype: list[str]
    """
    greedy_gloss = []
    for word in greedy_tokenizer(th_dict, sentence):
        greedy_gloss.append(word[3])
    return greedy_gloss



