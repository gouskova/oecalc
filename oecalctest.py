import oecalc as oe

path = '/home/maria/git/phonotactics/test_runs/quechua/user_input_files/LearningData.txt'
vowels = 'a e i o u'
consonants = 'k q K Q g G'

voweldic = oe.pairOEcalc(path, vowels)
dorsdic = oe.pairOEcalc(path, consonants)


vtab = oe.makeOETable(voweldic, vowels)

ctab = oe.makeOETable(dorsdic, consonants)


print('vowel OE values in quechua')
for pair in vtab:
    print(pair)


print('dorsal OE values in quechua')
for pair in ctab:
    print(pair)

vtab = oe.makeCountTable(voweldic, vowels)
ctab = oe.makeCountTable(dorsdic, consonants)

print('vowel counts in quechua')
for pair in vtab:
    print(pair)


print('dorsal counts in quechua')
for pair in ctab:
    print(pair)


oe.writeOE(path, vowels, '/home/maria/Desktop/quech_vowel_OE.txt')


oe.writeOE(path, consonants, '/home/maria/Desktop/quech_cons_OE.txt')
