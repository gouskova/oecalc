#!/usr/bin/env python3 
'''
Supplies a function for calculating Observed/Expected values over pairwise combinations of segments.

Input format for the data file:

p a t a
p i k u b e
s a mb u k i
k a tʃ o
...

Input format for the segment list:

"seg1 seg2 seg3"

(e.g., "a e i o u" or "ph t tʃ")

The OE() function will print a table of pairwise OE calculations in Terminal or save it to a file in the location you specify; see doc entry for "OE" for details.

Example use:

OE("LearningData.txt", "p k t")
'''

# LICENSE: Released under the FreeBSD license. 
#		  http://www.freebsd.org/copyright/freebsd-license.html





from itertools import product
 
def pairOEcalc(filepath, segs, rounded=2):
	'''
		filepath is a path to the file you want to calculate O/E over.
		formatting: same as the input to Hayes and Wilson's UCLA Phonotactic Learner, only this can deal with Unicode

	p a t a 
	p i k u b e
	s a mb u k i
	
		segs is the list of segbols you want to evaluate for Observed/Expected. separate it by spaces and surround by quotes, "e i o"
		
	   
	O/E is calculated as follows:
	Expected: N(S1) * N(S2)/ N of all pairs
	Observed: N(S1S2)
		the function will return unrounded OE, as well as a value rounded to the parameter given by the "rounded" argument. Defaults to 2, so an O/E value of 1.3432 will be printed as 1.34.
	
	'''
	words = open(filepath, 'r', encoding='utf-8').readlines()
	seglist = segs.strip().split(' ')
	wordlist = [x.strip().split() for x in words]
	pairs = {}.fromkeys(''.join(list(x)) for x in product(seglist, repeat=2)) #creates a dictionary with S1,S2 pairs from seglist, every possible combination
	segs = {}.fromkeys(seglist, 0)
	for x in pairs:
		pairs[x] = {'observed':0, 'expected':0}
	paircount = 0
	for word in wordlist:
		word = [x for x in word if x in seglist]
		if len(word)<2:
			continue
		else:
			segpairsinword = [word[x]+word[x+1] for x in range(0, len(word)-1)] #a list of 2-seg pairs in the word
			paircount += len(segpairsinword)
			for pair in segpairsinword:
				joined = ''.join(pair)
				pairs[joined]['observed']+=1
			for seg in word:
				segs[seg] += 1
	for pair in pairs:
		seg1 = pair[0]
		seg2 = pair[1]
		pairs[pair]['expected'] = segs[seg1]*segs[seg2]/paircount
		pairs[pair]['OE'] = pairs[pair]['observed']/pairs[pair]['expected']
		pairs[pair]['OErnd']=round(pairs[pair]['OE'],rounded)
	return(pairs)

def makeOETable(pairsdic, segs, rounded, prnt=True, outfile="None"):
	'''
	arranges the O/E values and sorts them into a table for display.
	"prnt" defaults to "True"; the function will print the results to screen.
	the default rounding paramter is 2. If you want to see raw unrounded values, pass "False" to 'rounded'
	'''
	seglist = segs.strip().split(' ')
	header = '\t'+'\t'.join(seglist)
	if outfile!="None":
		f = open(outfile, 'w', encoding="utf-8")
	rows = [header]
	for seg in seglist:
		row = [seg]
		rndrow = [seg]
		for otherseg in seglist:
			pair = seg+otherseg
			row.append(str(pairsdic[pair]['OE']))
			rndrow.append(str(pairsdic[pair]['OErnd']))
		if rounded == False:
			outrow = '\t'.join(row)
		else:
			outrow = '\t'.join(rndrow)
		rows.append(outrow)
	if print:
            for row in rows:
                print(row)
	if outfile!="None":
		f.write([row+'\n' for row in rows])
		outfile.close()

def OE(filepath, segs, prnt=True, outfile="None", rounded=2):
    pairsdic = pairOEcalc(filepath, segs, rounded=2)
    makeOETable(pairsdic, segs, rounded, prnt, outfile)


#path = 'shona/hayes_wilson_files/LearningData.txt' 
#segset = 'a e i o u'

#OE(filepath=path, segs=segset)


if __name__ == "__main__":
	import sys
	OE(filepath=sys.argv[1], segs=sys.argv[2], rounded=2, prnt=True)
