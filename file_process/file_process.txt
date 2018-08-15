name_string = 'sam, brad, alex, cameron, toby, gwen, jenn, connor'
names = name_string.split(',')
print names
for a in names:
    print a
    
parts = name_string.split('toby')
print parts
for b in parts:
    print b
    
word_list = ['my', 'name', 'is', 'warren']

string = ' '.join(word_list)
print string

long_string = 'test'.join(word_list)
print long_string

string1 = 'Hello'
string2 = string1.lower()
print string2 
string3 = string1.upper()
print string3


test_string = 'there are many blank symbols after this sentence.      '
print test_string
got_string = test_string.strip()
print got_string, ',blank symbols were deleted'
test = 'Lidongde'
got = test.strip('de')
print test, '\t', got, '\t changed'

find_string = 'frankenstein'
if find_string.endswith('tein'):
    print 'end with the "tein"'
    
if not find_string.endswith('a'):
    print 'no end with the "a"'
    
if find_string.startswith('fran'):
    print 'start with the "fran"'
    
if not find_string.startswith('ran'):
    print "no start with the 'ran'"

addr1 = '657 Maple Lane'
if 'Maple' in addr1: 
    print "That address has 'maple' in it."
    position = addr1.index('Maple')
    print 'found "Maple" at index', position