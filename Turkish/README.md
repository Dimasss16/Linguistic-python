This Python project focuses on generating noun paradigms for Turkish, and addresses linguistic phenomena specific to this language. The noun paradigm is generated using a set of functions, each catering to specific linguistic rules.

The project follows these steps:
1. Defining functions for identifying vowel and consonant properties:
- `is_vowel(letter)`: Determines if a given letter is a vowel.
- `vowel_ending(word)`: Identifies the vowel ending of a word.
- `extract_last_vowel(word)`: Extracts the last vowel from a word.
- `is_voiced(consonant)`: Checks if a consonant is voiced.
2. Implementing vowel harmony rules:
- `i_type_harmony(vowel)`: Returns the appropriate vowel based on I-type harmony rules.
- `a_type_harmony(vowel)`: Returns the appropriate vowel based on A-type harmony rules.
3. Implementing consonant harmony:
- `consonant_harmony(noun)`: Determines the appropriate consonant ending ("d" or "t") based on the noun's final sound.
4. Noun inflection:
- `inflect_noun(lemma, case, number)`: Inflects a given noun lemma according to the specified case and number, considering relevant morphological rules.
5. Generating the paradigm:
- `print_paradigm(lemma)`: Prints the full noun paradigm for the given lemma, encompassing all cases and both singular and plural forms.
