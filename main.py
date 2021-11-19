# -*- coding: utf-8 -*-

import re
from thefuzz import fuzz
from nltk.tokenize import WordPunctTokenizer

def correct_text():
    dictionary =[w.strip() for w in open("dictionary.txt", encoding="utf-8")]
    avoid_tokens = [",", ".", ":", ";"]
    with open("original.txt", encoding="utf-8") as input_file:
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
    correct_text()
    