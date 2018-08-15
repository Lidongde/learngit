from PIL import Image
import codecs

try:
    f = open('file_process.txt', 'r')
    print f.read()
finally:
    if f:
        f.close()
        
with open('file_process.txt', 'r') as file:
    for line in file.readlines():
        print (line.strip())
        
with Image.open('first.jpg') as binary:
    print binary.show()
    
try:
    file2 = open('gbk_test.txt', 'rb')   # must open it with 'rb' mode since it isn't coded in ascII
    print file2.read().decode('gbk')
finally:
    if file2:
        file2.close()

with codecs.open('gbk_test.txt', 'r', 'gbk') as f2:
    print f2.read() # if use this skill, remeber to import the module "codecs"
    
with open('gbk_test.txt', 'a') as write:
    write.write('\n Hello, world')

with codecs.open('gbk_test.txt', 'r', 'gbk') as wr:
    print wr.read()