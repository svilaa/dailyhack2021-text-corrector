import re as r;from thefuzz import fuzz as f;from nltk.tokenize import WordPunctTokenizer as t;from string import punctuation as p
with open("i.txt",'r',-1,"utf-8")as i,open("o.txt",'w',-1,"utf-8")as o:
    for v in i.readlines(): [[o.write(' '+max([[c,f.ratio(w,c)]for c in [w.strip()for w in open("d.txt",'r',-1,"utf-8")]],key=lambda x:x[1])[0])if w not in set(p)else o.write(w)for w in t().tokenize(r.sub(r"\S?/\S?",'',r.sub(r'\.\w','.',v)))], o.write('\n')]
