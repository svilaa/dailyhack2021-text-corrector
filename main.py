# -*- coding: utf-8 -*-

import re
from thefuzz import fuzz
from nltk.tokenize import WordPunctTokenizer
import ftfy

def get_dictionary_words():
    word_list = []
    with open("dictionary.txt", 'r', encoding="utf-8") as f:
        for value in f.readlines():
            word_list.append(value.strip())
    return word_list

def get_text_words():
    word_list = []
    with open("original.txt", 'r', encoding="utf-8") as f:
        for value in f.readlines():
            for v in value.split():
                word_list.append(v.strip(" ,."))
    return word_list

def get_original_string():
    with open('original.txt', 'r') as file:
        return file.read()

def check_words(original_text, dictionary):
    correct = 0
    error = 0
    corrections = {}
    for word in original_text:
        word_data = []
        for dict_word in dictionary:
            score = fuzz.ratio(word, dict_word)
            word_data.append([dict_word, score])
        word_data = sorted(word_data, key=lambda x: x[1], reverse=True)
        if word_data[0][1] == 100:
            print(word, "OK")
            correct += 1
        else:
            print(word, "->", [x[0] for x in word_data[:3]])
            corrections[word] = word_data[0][0]
            error += 1
    print(correct/(error+correct)*100)
    return corrections

def get_corrected_text(original_string, corrections):
    for error_word, correct_word in corrections.items():
        original_string = original_string.replace(error_word, correct_word)
    return original_string

def similar_words_in_original():
    pass

def first_proposal():
    corrections = check_words(original_text, dictionary)
    corrected_text = get_corrected_text(original_string, corrections)
    with open('fixed.txt', 'w') as file:
        file.write(corrected_text)

def second_proposal(original_string, dictionary):
    tokenizer = TweetTokenizer()
    words = tokenizer.tokenize(original_string)
    for word in words:
        print(word)

def third_proposal(original_string, dictionary):
    words = PT().tokenize(original_string)
    for word in words:
        print(ftfy.fix_text(word))

def fouth_proposal(original_string, dictionary):
    avoid_tokens = [",", ".", ":", ";"]
    with open("original.txt", 'r', encoding="utf-8") as input_file:
        with open("fixed4.txt", 'w', encoding="utf-8") as output_file:
            for value in input_file.readlines():
                words = WordPunctTokenizer().tokenize(re.sub(r'\S?/\S?', "", re.sub(r'\.\w', ".", value)))
                print(words)
                for word in words:
                    if word not in avoid_tokens:
                        print(" ", end="")
                        output_file.write(" ")
                        word = get_corrected_word(word, dictionary)
                    print(word, end="")
                    output_file.write(word)
                print("")
                output_file.write("\n")

def old_get_corrected_word(word, dictionary):
    word_data = []
    for dict_word in dictionary:
        score = fuzz.ratio(word, dict_word)
        word_data.append([dict_word, score])
    word_data = sorted(word_data, key=lambda x: x[1], reverse=True)
    return word_data[0][0]

def old2_get_corrected_word(word, dictionary):
    word_data = []
    for dict_word in dictionary:
        score = fuzz.ratio(word, dict_word)
        word_data.append([dict_word, score])
    return max(word_data, key=lambda x:x[1])[0]

def get_corrected_word(word, dictionary):
    return max([[dict_word, fuzz.ratio(word, dict_word)] for dict_word in dictionary], key=lambda x:x[1])[0]

def cleaned_fouth_proposal():
    dictionary = get_dictionary_words()
    avoid_tokens = [",", ".", ":", ";"]
    with open("original.txt", 'r', encoding="utf-8") as input_file:
        with open("fixed4.txt", 'w', encoding="utf-8") as output_file:
            for value in input_file.readlines():
                words = WordPunctTokenizer().tokenize(re.sub(r'\S?/\S?', "", re.sub(r'\.\w', ".", value)))
                for word in words:
                    if word not in avoid_tokens:
                        output_file.write(" ")
                        word = max([[dict_word, fuzz.ratio(word, dict_word)] for dict_word in dictionary], key=lambda x:x[1])[0]
                    output_file.write(word)
                output_file.write("\n")

if __name__=="__main__":
    cleaned_fouth_proposal()
    