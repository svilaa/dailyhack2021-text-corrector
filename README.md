# Text corrector
S'ha intentat reduïr al màxim la mida del codi a costa del rendiment, per exemple, per cada paraula es llegeix el fitxer de paraules, així s'estalvia una assignació.
Es tracten els cassos especials de backslash amb caràcters pròxims (\) i es mantenen la resta de signes de puntuació. 

# Requeriments
 - Python 3.8.10, Ubuntu 20.04
 - pip install nltk==3.6.5
 - pip install thefuzz==0.19.0
 - (opcional) pip install python-Levenshtein==0.12.2

# Instruccions
cat original.txt | python main.py > output.txt
