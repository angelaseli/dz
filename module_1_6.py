dict = {'Angela': 1992, 'Seva': 1996, 'Marat': 1990, 'Maga': 1996}
print ('Dict:', dict)
print ('Existing value:', dict ['Seva'])
print ('Not existing value:',dict.get ('Masha'))
dict.update({'Lera':1991, 'Ira':1993})
print (dict)
print('Deleted value:',dict.pop('Ira'))
print ('Modified dictionary:', dict)

set_1 = {1, 'манго', 555.888,'манго', 1, 'манго'}
print ('Set:', set_1)
set_1.update ({(33.66, 6768.99)})
set_1.discard(555.888)
print ('Modified set:', set_1)
