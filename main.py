import re as r;from thefuzz import fuzz as f;from nltk.tokenize import WordPunctTokenizer as t;from string import punctuation as p
with open("i.txt",'r',-1,"utf-8")as i,open("o.txt",'w',-1,"utf-8")as o:
    d=[w.strip()for w in open("d.txt",'r',-1,"utf-8")];e=o.write
    for v in i.readlines(): [[e(' '+max([[c,f.ratio(w,c)]for c in d],key=lambda x:x[1])[0])if w not in set(p)else e(w)for w in t().tokenize(r.sub(r"\S?/\S?",'',r.sub(r'\.\w','.',v)))], e('\n')]

    #for v in i.readlines():
    #    for w in t().tokenize(r.sub(r"\S?/\S?",'',r.sub(r'\.\w','.',v))):
    #        if w not in set(p):w=' '+max([[c,f.ratio(w,c)]for c in d],key=lambda x:x[1])[0]
    #        e(w)
    #    e('\n')