#from HelloPkg import Hello
    
#Hello.helloWorld()

#import HelloPkg.Hello
    
#HelloPkg.Hello.helloWorld()

#lst = ['a','b','c']

#for number,item in enumerate(lst):
    #print '%s %s' %(number, item)
    

#list = range(20)
#print all(map(lambda x: x > 10, list))
#print any(map(lambda x: x > 10, list))

#def word_lengths(phrase):    
    #return map(len, phrase.split())

#print word_lengths('How long are the words in this phrase')


from collections import Counter
l = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]

print Counter(l)