This Python project demonstrates the relationship between the Spanish copulas "ser" and "estar" and their commonly associated adjectives. The aim is to see how the choice of copula affects and mirrors the meaning implied by the adjective.

**Project Tasks:**

1. Data Loading and Preprocessing:

- `load_sentences(input_file)`: Reads tagged sentences from a file, representing each sentence as a list of word-tag pairs.
- `lemmatize(es_form)`: Converts Spanish adjective forms to their base form based on simplified rules.

2. Copula and Adjective Analysis:

- `count_occurrences(sentences, conj_ser, conj_estar)`: Analyzes each sentence in the corpus, identifies instances of copulas followed by adjectives, and categorizes them based on the copula ("ser" or "estar"). Builds dictionaries to record the frequency of each adjective-copula combination.

3. Adjective Set Generation:

- `get_occurrence_sets(freq_ser, freq_estar)`: Processes the frequency data to identify adjectives that:
  - Mostly occur with "ser" (classified in the `ser` set)
  - Mostly occur with "estar" (classified in the `estar` set)
  - Mostly occur with both copulas (classified in the `both` set)

**Functions:**

- `load_sentences(input_file)`: Reads tagged sentences from a file.
- `lemmatize(es_form)`: Converts Spanish adjective forms to their base form.
- `count_occurrences(sentences, conj_ser, conj_estar)`: Analyzes copula-adjective occurrences and builds frequency dictionaries.
- `get_occurrence_sets(freq_ser, freq_estar)`: Generates sets of adjectives based on their compatibility with a copula.

**Usage:**

1. Load the pre-tagged Spanish corpus file.
2. Analyze the corpus using the provided functions.
3. The program outputs sets containing adjectives categorized according to their copula usage:
  - `ser`: Adjectives mostly used with "ser".
  - `estar`: Adjectives mostly used with "estar".
  - `both`: Adjectives used with both copulas significantly.
4. Additionally, you can use the test file to verify that the code works properly.
