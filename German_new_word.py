# import random


# def load_words_from_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return [line.strip() for line in file.readlines()]


# def save_words_to_file(file_path, words_list):
#     with open(file_path, 'w', encoding='utf-8') as file:
#         file.write('\n'.join(words_list))


# def get_word_translation(word_line):
#     word_parts = word_line.split()
#     if len(word_parts) >= 2:
#         return word_parts[1]
#     else:
#         return None


# def get_new_words(words_list, learned_words, num_new_words):
#     new_words = []
#     while len(new_words) < num_new_words:
#         word = random.choice(words_list)
#         word_translation = get_word_translation(word)
#         if word_translation and word_translation not in learned_words and all(word_translation not in learned_word for learned_word in learned_words):
#             new_words.append(word)
#     return new_words


# def main():
#     german_words_file = "german_words.txt"
#     learned_words_file = "learned_words.txt"
#     new_words_file = "new_german_words.txt"

#     german_words = load_words_from_file(german_words_file)
#     learned_words = set(load_words_from_file(learned_words_file))

#     print(f"Number of words in your German vocab: {len(learned_words)}")

#     num_new_words = int(
#         input("Enter the number of new words you want to learn: "))

#     new_words = get_new_words(german_words, learned_words, num_new_words)

#     for word in new_words:
#         print(word)

#     # Save new words to a new file
#     save_words_to_file(new_words_file, new_words)

#     # Load words from the new words file and remove duplicates
#     new_words = list(set(load_words_from_file(new_words_file)))
#     save_words_to_file(new_words_file, new_words)


# if __name__ == "__main__":
#     main()

import random


def load_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]


def save_words_to_file(file_path, words_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(words_list))


def get_word_translation(word_line):
    word_parts = word_line.split()
    if len(word_parts) >= 2:
        return word_parts[1]
    else:
        return None


def get_new_words(words_list, learned_words, num_new_words):
    new_words = set()  # Use a set to store unique new words
    available_words = [word for word in words_list if get_word_translation(
        word) and get_word_translation(word) not in learned_words]

    while len(new_words) < num_new_words and available_words:
        word = random.choice(available_words)
        available_words.remove(word)
        word_translation = get_word_translation(word)
        if word_translation and word_translation not in new_words and all(word_translation not in learned_word for learned_word in learned_words):
            new_words.add(word_translation)

    return [word for word in words_list if get_word_translation(word) in new_words]


def main():
    german_words_file = "german_words.txt"
    learned_words_file = "learned_words.txt"
    new_words_file = "new_german_words.txt"

    german_words = load_words_from_file(german_words_file)
    learned_words = set(load_words_from_file(learned_words_file))

    print(f"Number of words in your German vocab: {len(learned_words)}")

    num_new_words = int(
        input("Enter the number of new words you want to learn: "))

    new_words = get_new_words(german_words, learned_words, num_new_words)

    for word in new_words:
        print(word)

    # Save new words to a new file
    save_words_to_file(new_words_file, new_words)

    # Load words from the new words file and remove duplicates
    new_words = list(set(load_words_from_file(new_words_file)))
    save_words_to_file(new_words_file, new_words)


if __name__ == "__main__":
    main()
