dict_of_words = {}
list_of_words = []
with open("src/wchain.in.txt", "r", encoding="utf-8") as wchain_in:
    num_of_word = int(wchain_in.readline())
    for _ in range(num_of_word):
        word = wchain_in.readline()
        dict_of_words[word.strip()] = 1
        list_of_words.append(word.strip())
list_of_words.sort(key=len)


def check_if_one_word_in_another(shorter_word: str, longer_word: str):
    longer_word_idx = 0
    for i in range(len(shorter_word)):
        if longer_word_idx == i - 1 and i != 0:
            longer_word_idx = i
        if shorter_word[i] != longer_word[longer_word_idx]:
            longer_word_idx += 1
            if shorter_word[i] != longer_word[longer_word_idx]:
                return False
    return True


def find_max_sequence_words(words_dict: dict[str:int], word_list: list[str]):
    for short_word in word_list:
        for long_word in word_list:
            if len(long_word) == len(short_word) + 1:
                if check_if_one_word_in_another(short_word, long_word):
                    words_dict[long_word] = words_dict[short_word] + 1
    return max(words_dict.values())


with open("src/wchain.out.txt", "w", encoding="utf-8") as wchain_out:
    wchain_out.write(str(find_max_sequence_words(dict_of_words, list_of_words)))
