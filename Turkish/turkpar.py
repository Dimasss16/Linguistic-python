"""
Python 2023 Assignment 02
"""

# IMPORTANT: assign the parts of your name and your student ID to these variables!
first_name = "Dmitry"
family_name = "Sukhotin"
student_id = "6688071"

# print(student_id)

def is_vowel(letter):
    """
    Checks whether the letter is a vowel.
    """
    
    vowels = 'E, e, Ö, ö, A, a, O, o, I ̇, i, Ü, ü, I, ı, U, u'
    return letter in vowels
    pass


def ends_in_vowel(word):
    """
    Checks whether the words ends with a vowel sound.
    """
    return is_vowel(word[-1])
    pass


def get_last_vowel(word):
    """
    Returns the last vowel in a word.
    """
    if not word:
        return None
    else:
        if ends_in_vowel(word):
            return word[-1]
        else:
            if is_vowel(word[-2]):
                return word[-2]
            elif is_vowel(word[-3]):
                return word[-3]
            else:
                return None
    pass


def is_voiced(consonant):
    """
    Checks whether the consonant is voiced.
    """
    voiced = "bdgğlmnrvz"
    
    
    if is_vowel(consonant):
        return False
    else:
        return consonant in voiced
    pass


def i_type_harmony(vowel):
    if not is_vowel(vowel):
        return None
    else:
        if vowel in "öü":
            return "ü"
        elif vowel in "ou":
            return "u"
        elif vowel in "ei":
            return "i"
        elif vowel in "aı":
            return "ı"
    pass


def a_type_harmony(vowel):
    if not is_vowel(vowel):
        return None
    else:
        if vowel in "eiöü":
            return "e"
        elif vowel in "aıou":
            return "a"
    pass


def consonant_harmony(noun):
    last_letter = noun[-1]
    if is_voiced(last_letter) or is_vowel(last_letter):
        return "d"
    else:
        return "t"
    pass


def inflect_noun(lemma, case, number):
    """
    Inflect the given lemma using the morphological rules of Turkish.
    """
    '''
    Step 1: define the plural suffix
    '''
    if number == "plural":
        if a_type_harmony(get_last_vowel(lemma)) in "eiöü":
            plural_suffix = "ler"
        else:
            plural_suffix = "lar"
            
    '''
    Step 2: appenging a glide
    '''
    if number == "singular" and ends_in_vowel(lemma) and case in ["ACC", "GEN", "DAT"]:
        lemma += "y"
    pass

    '''
    Step 3: Cases
    '''
    if number == "singular":
        if case == "NOM":
            form = lemma
        elif case == "ACC":
            form = lemma + i_type_harmony(get_last_vowel(lemma))
        elif case == "GEN":
            form = lemma + i_type_harmony(get_last_vowel(lemma)) + "n"
        elif case == "DAT":
            form = lemma + a_type_harmony(get_last_vowel(lemma))
        elif case == "LOC":
            vowel = a_type_harmony(get_last_vowel(lemma))
            cons = consonant_harmony(lemma) 
            form = lemma + cons + vowel
        elif case == "ABL":
            vowel = a_type_harmony(get_last_vowel(lemma))
            cons = consonant_harmony(lemma)
            form = lemma + cons + vowel + "n"
            
    elif number == "plural":
        plural_suffix = "l" + a_type_harmony(get_last_vowel(lemma)) + "r"
        form = lemma + plural_suffix
        
        
        if case == "NOM":
            form = form
        elif case == "ACC":
            form += i_type_harmony(get_last_vowel(form))
        elif case == "GEN":
            form += i_type_harmony(get_last_vowel(lemma)) + "n"
        elif case == "DAT":
            form += a_type_harmony(get_last_vowel(lemma))
            
            
        elif case == "LOC":
            vowel = a_type_harmony(get_last_vowel(form))
            cons = consonant_harmony(form) 
            form += cons + vowel
        elif case == "ABL":
            vowel = a_type_harmony(get_last_vowel(form))
            cons = consonant_harmony(form)
            form += cons + vowel + "n"
    return form
            
        
def print_paradigm(lemma):
    """
    Bonus task: print the full singular and plural paradigm of a Turkish noun to the console.
    """
    print("Singular")
    cases = ['NOM', "ACC", "GEN", "DAT", "LOC", "ABL"]
    sing_number = "singular"
    for case in cases:
        print(case + " " + inflect_noun(lemma, case, sing_number))
        
    print("Plural")
    plur_number = 'plural'
    for case in cases:
        print(case + " " + inflect_noun(lemma, case, plur_number))
    return ""
    pass

lemma = "kola"
print(print_paradigm(lemma))
# if __name__ == '__main__':
#     pass
