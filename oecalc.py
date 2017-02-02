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

For additional options, from python3, type "help(oecalc)" or "help(OE, oecalc)"

'''

# LICENSE: Released under the FreeBSD license. 
# http://www.freebsd.org/copyright/freebsd-license.html




from itertools import product


# make a dictionary of pairs of segs and collect their O/E values into it

def pairOEcalc(filepath, segs):
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
	the function will return unrounded OE, as well as a value rounded to the parameter given by the "rounded" argument.
	Defaults to 2, so an O/E value of 1.3432 will be printed as 1.34.
	'''
	try:
		words = open(filepath, 'r', encoding='utf-8').readlines()
	except FileNotFoundError:
		print("please make sure there is a file to read at the location.")
		pass
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
		seg1,seg2 = pair[0],pair[1]
		pairs[pair]['expected'] = segs[seg1]*segs[seg2]/paircount
		pairs[pair]['OE'] = pairs[pair]['observed']/pairs[pair]['expected']
		pairs[pair]['OErnd']=round(pairs[pair]['OE'],3)
	return(pairs)

# make the dictionary printable   

def makeOETable(pairsdic, segs, rounded=True):
	'''
	arranges the O/E values and sorts them into a table for display.
	the input should be the dictionary that's returned by pairOEcalc()
	output is a list of tab-separated lines that, if printed, looks like a table
	'''
	seglist = segs.strip().split(' ')
	header = '\t'+'\t'.join(seglist)
	rows = [header]
	for seg in seglist:
		row = [seg]
		for otherseg in seglist:
			pair = seg+otherseg
			if rounded:
				row.append(str(pairsdic[pair]['OErnd']))
			else:
				row.append(str(pairsdic[pair]['OE']))
		outrow = '\t'.join(row)
		rows.append(outrow)
	return(rows)

# printable observed and expected values (as opposed to ratio) for each pair

def makeCountTable(pairsdic, segs):
        '''
        print how often each segment in a pair was observed and how often it was expected

        '''
        seglist = segs.strip().split(' ')
        header = '\t'+'\t'.join(seglist)
        rows = [header]
        for seg in seglist:
                row1 = [seg+' observed']
                row2 = [seg+' expected']
                for otherseg in seglist:
                        pair = seg+otherseg
                        row1.append(str(pairsdic[pair]['observed']))
                        row2.append(str(pairsdic[pair]['expected']))
                outrow1 = '\t'.join(row1)
                outrow2 = '\t'.join(row2)
                rows.append(outrow1)
                rows.append(outrow2)
        return(rows)

#a convenience function that combines OE collection and printing
def OE(filepath, segs):
	'''
	filepath is where your wordlist is located. Absolute path might be best here
	segs is the list of segments, space-separated, over which you want O/E calculated
	'''
	pairsdic = pairOEcalc(filepath, segs)
	out=makeOETable(pairsdic, segs)
	for line in out:
		print(line)
	return(out)


#saves OE table to file
def writeOE(filepath, segs, outfilepath, rounded=True):
        '''
        filepath is where your wordlist is located
        segs is the list of segments, space-separated, over which you want O/E calculated
        outfilepath is for recording the results
        if rounded is True, the output will be rounded to 3 decimals (otherwise it's Python3's default for integers, which is unreadably long)
        '''
        pairsdic = pairOEcalc(filepath, segs)
        out = makeOETable(pairsdic, segs, rounded)
        f = open(outfilepath, 'w', encoding='utf-8')
        for row in out:
            f.write(row+'\n')
        f.close()


#if you want to run it from command line--just to print table of OE values to screen
if __name__ == "__main__":
	import sys
	if len(sys.argv)==1:
		print("you need to supply some arguments to oecalc. please see the README.md on http://github.com/gouskova/oecalc for help and use instructions.")
	elif len(sys.argv)>1:
		filepath=sys.argv[1]
		segs = sys.argv[2]
		OE(filepath, segs)
