================================================================================
Overview
================================================================================

This module supplies a function for calculating observed/expected values for pairs of segments in a word list.

The word list is in a .txt file, and it should be formulated as in Hayes and Wilson's UCLA Phonotactic Learner: one word per line with spaces separating individual segments. Segments can consist of arbitrarily long sequences of letters. Unicode is supported.

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
"t, tʃ"
```

The output is a table of segments (first in row, second in column), with O/E numbers rounded to the value specified by you.

Example use from command line:

```$ oecalc /home/yourname/yourdatafolder/LearningData.txt "a e i o u"```

Output to your terminal:

```
	a	e	i	o	u
a	0.31	0.12	0.23	0.14	0.18
e	0.39	1.06	0.23	1.21	0.15
i	0.2	0.0	0.38	0.01	0.22
o	0.28	1.14	0.16	1.54	0.2
u	0.18	0.0	0.27	0.0	0.43
```

This means that, on a tier consisting of only "a, e, i, o, u" segments, the pair "a e" had an O/E of 0.12, and the pair "a i" had an O/E of 0.23. Every pair of vowels in a word gets counted separately, so in the word "p a t e k a b e", the sequences "a e", "e a", "a e" will be counted.


================================================================================
Requirements
================================================================================

Requires python3. Go to http://python.org to install.

If you want to run it from python3, navigate to wherever you keep your custom modules and do the following:

```
>>> from oecalc import OE
>>> OE(filepath="filename.txt", segs="k q K Q", rounded=3)
```

================================================================================
Installation for command line use
================================================================================


You can make this a command line utility as follows. (Instructions assume a Linux-like operating environment)

1. Copy or move the oecalc file to the directory where you keep your scripts. For example, start Terminal and do this at the bash prompt:

```
$ cp /home/yourname/downloads/oecalc /home/yourname/bin/
$ touch __init__.py
```

2. Add the following line to your ```/home/yourname/.bashrc``` or ```.bash_profile```:

```
export PYTHONPATH="${PYTHONPATH}:/home/yourname/bin"
```
and then

```
$ source /home/yourname/.bashrc
```

This will allow python to recognize scripts inside ```/home/yourname/bin``` as executables.

3. You can invoke it from Terminal/bash like this:

```$ oecalc /home/yourname/pathtosomefile.txt "a e i o u"```

and it will print out a nice O/E table for you right in terminal.

Comments? Suggestions? Complaints? Write to your Congressional Representative.
