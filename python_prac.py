import itertools

para="Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph."
s = '*'
l = s.join(list(para.replace(' ','')))
print(l)
print(para.split('the')[0:20])
freq =[]
for i in para.split(' '):
    if para.count(i)<2:
        freq.append(i)
print(freq[0:5])
print(freq[-5:])
sd= "the,lee,the"
print(sd.rindex('the'))

k = [i for i in 'maverick' if i not in 'aeiou']
print(k)
print(sorted(k))
print(k)

s = sorted({ord(i) for i in 'apple'})
print(s)

from itertools import takewhile
def even_nos(x):
    return (x%2==0)

li =[0,2,4,6,8]
new_li = list(takewhile(even_nos,li))
print(new_li)

x = itertools.takewhile(lambda x:x<5,[1,4,6,4,1])
print(list(x))

class Person:
    'Reps a person'
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
p1 = Person('George','livingston')
print(p1.fname,'-',p1.lname)
print(help(Person.__doc__))