# German_noun_chooser
Simple Way to get nouns to learn each day for IGCSE German test

Learning German vocabulary?
This is a simple python code that provides you germna vocabs for you to learn, it has been populated with 500 + basic A2 German vocabs for you to learn words each day. 

`german_words.txt`:
Description: This text file contains a list of German words along with their English translations. Each line in the file follows the format "German word (English translation)". This file serves as a database of German vocabulary.

How to Use: You can add or edit German words and their translations in this file. It is recommended to maintain the format "German word (English translation)" for consistency. This file provides the vocabulary from which the program selects new words for you to learn.

`learned_words.txt`:
Description: This text file keeps track of the German words that you have already learned. Each line in the file contains a German word that you have mastered.

How to Use: The content of this file is managed by you. As you learn new German words, you can add them to this file manually. The program will use this file to check if new words overlap with the words you have already learned, ensuring unique new word selections.

`new_german_words.txt`:
Description: This text file stores the randomly selected German words that you should learn. The program generates this list based on the "german_words.txt" file and avoids any overlap with the words in the "learned_words.txt" file.

How to Use: The program automatically creates and updates this file with randomly selected new words. You should not edit this file manually, as it will be overwritten each time the program runs.

`German_new_word.py`:
Description: This Python script helps you improve your German vocabulary skills. It selects a specified number of new German words from the "german_words.txt" file, ensuring they are not already present in the "learned_words.txt" file, and saves them in the "new_german_words.txt" file. The script prevents duplicates and ensures unique word selections for learning.

`Magic_prompt_for_Chatgpt.txt`
Description: A prompt you can give to chatgpt for it to generate you more words under the workable format of the python code, you can populate the new words into the `german_words.txt`.

How to Use: You can run this Python script in your preferred Python environment. Upon execution, the script will prompt you to enter the number of new words you want to learn. The script will then randomly select unique new words and save them in the "new_german_words.txt" file. You can continue running the script to select additional new words whenever you desire to expand your German vocabulary.

