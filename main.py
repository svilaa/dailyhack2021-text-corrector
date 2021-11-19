import re as r;from thefuzz import fuzz as f;from nltk.tokenize import WordPunctTokenizer as t
d = [w.strip() for w in open("dictionary.txt", encoding="utf-8")]
with open("original.txt", encoding="utf-8") as i, open("corrected.txt", 'w', encoding="utf-8") as o:
    for v in i.readlines():
        for w in t().tokenize(r.sub(r'\S?/\S?', "", r.sub(r'\.\w', ".", v))):
            if w not in [",", ".", ":", ";"]: w = " " + max([[c, f.ratio(w, c)] for c in d], key=lambda x:x[1])[0]
            o.write(w)
        o.write("\n")