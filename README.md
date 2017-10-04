Overview
==

This module supplies a function for calculating observed/expected values for pairs of segments in a word list.

The word list is in a .txt file, and it should be formulated as in Hayes and Wilson's UCLA Phonotactic Learner: one word per line with spaces separating individual segments. Segments can consist of arbitrarily long sequences of letters. The file must be in Unicode (utf-8).

```
p a t a
p i k u b e
s a mb u k i
k a tʃ o
...
```

The segments over which O/E is calculated are passed to the function as a space-separated list, as follows: 

```
"a e i o u"
```

or

```
"t tʃ"
```

The output is a table of segments (first in row, second in column), with O/E numbers rounded to 3 decimals. 

Example use from command line:

```$ oecalc /home/yourname/yourdatafolder/LearningData.txt "a e i o u"```

Output you see in your terminal:

```
	a	e	i	o	u
a	0.311	0.12	0.233	0.914	0.128
e	0.393	1.066	0.232	1.921	0.151
i	0.271	0.0	0.383	0.019	0.223
o	0.028	1.143	0.167	1.554	0.201
u	0.181	0.033	0.278	0.054	0.043
```

This means that, on a tier consisting of only "a, e, i, o, u" segments, the pair "a e" had an O/E of 0.12, and the pair "a i" had an O/E of 0.233. Every pair of vowels in a word gets counted separately, so in the word "p a t e k a b e", the sequences "a e", "e a", "a e" will be counted.


Requirements
==

Requires python3. Go to http://python.org to install.

If you want to run it from python3, navigate to wherever you keep your custom modules and do the following:

```
>>> import oecalc
help(oecalc) #to print the "documentation"

oecalc.OE('/home/yourname/pathtoryourfiles.txt', 'p q dh th')

```

Installation for command line use
==


You can make this a command line utility as follows. (Instructions assume a Linux-like operating environment)

1. Copy or move the oecalc file to the directory where you keep your scripts. For example, start Terminal and do this at the bash prompt:

```
$ cp /home/yourname/downloads/oecalc /home/yourname/bin/
$ touch __init__.py
```

2. Linux: add the following line to your ```/home/yourname/.bashrc```:

```
export PYTHONPATH="${PYTHONPATH}:/home/yourname/bin"
```

Mac: add the folllowing lines to your ```/home/yourname/.bash_profile```:

```
PATH="/Users/yourname/bin:${PATH}"
export PATH
```

and then, in terminal,

```
$ source /home/yourname/.bashrc
```

This will allow python to recognize scripts inside ```/home/yourname/bin``` as executables.

3. You can invoke it from Terminal/bash like this:

```$ oecalc /home/yourname/pathtosomefile.txt "a e i o u" local```

and it will print out a nice O/E table for you right in terminal. The filepath, segments, and local/nonlocal arguments are obligatory. "Local/nonlocal" determines whether you get calculations for adjacent segments--if "local"--(e.g., "apta" would be counted for "p t" co-occurrences, but "pata" would not) or for non-adjacent ones if "nonlocal" (i.e., both "apta" and "pata" would be counted, since the "p" and "t" would be present on a P-T projection).

The filepath and segments arguments should be given first and second.

You can also add a "raw" argument, optionally, if you want to see the raw counts for observed and the exact numbers for expected. "local" and "raw" can be given in any order.

Comments? Suggestions? Complaints? Write to your Congressional Representative.
