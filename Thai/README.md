This Python project focuses on linguistic analysis of Thai text, with an emphasis on tokenization, transliteration, part-of-speech tagging, and glossing. Thai, being an isolating language, presents unique challenges in processing due to the absence of word boundaries in its orthography.

**Project Tasks:**
1. Reading the Dictionary from a File:
- Function: `read_file_to_dict(input_file)`
  - Reads the contents of an input file, retrieving columns 2, 3, and 4 based on unique values in column 1.
  - Returns a dictionary.
2. Simple Tokenization:
- Function: `simple_tokenizer(th_dict, sentence)`
  - Combines simple tokenizer, transliterator, part-of-speech tagger, and glosser.
  - Analyzes a Thai sentence based on the dictionary data, looking for the shortest possible chunk.
  - Returns tokenized, transliterated, POS-tagged, and glossed results.
3. Greedy Tokenization:
- Function: `greedy_tokenizer(th_dict, sentence)`
  - Combines greedy tokenizer, transliterator, part-of-speech tagger, and glosser.
  - Analyzes a Thai sentence based on the dictionary data, finding the longest chunk.
  - Returns tokenized, transliterated, POS-tagged, and glossed results.

**Functions:**
- `th_tokens(th_dict, sentence)`: Gets tokens using simple tokenization.
- `th_translit(th_dict, sentence)`: Gets transliterations using simple tokenization.
- `th_pos(th_dict, sentence)`: Gets part-of-speech tags using simple tokenization.
- `th_glosses(th_dict, sentence)`: Gets English glosses using simple tokenization.
- `th_tokens_greedy(th_dict, sentence)`: Gets tokens using greedy tokenization.
- `th_translit_greedy(th_dict, sentence)`: Gets transliterations using greedy tokenization.
- `th_pos_greedy(th_dict, sentence)`: Gets part-of-speech tags using greedy tokenization.
- `th_glosses_greedy(th_dict, sentence)`: Gets English glosses using greedy tokenization.
  
**Usage:**
1. Load the dictionary using read_file_to_dict.
2. Use simple or greedy tokenization functions for your task.
3. Get the tokenized results, transliterations, part-of-speech tags, and English glosses for a given Thai sentence.
4. Additionally, use the unittest file to verify the functionality.
