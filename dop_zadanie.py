students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron' ]
print (sorted(students))
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
journal = {'Aaron': [5, 3, 3, 5, 4],'Bilbo': [2, 2, 2, 3], 'Johnny': [4, 5, 5, 2], 'Khendrik': [4, 4, 3], 'Steve': [5, 5, 5, 4, 5] }
print (journal)
average_A = sum(journal['Aaron']) / len(journal ['Aaron'])
average_B = sum(journal['Bilbo']) / len (journal['Bilbo'])
average_J = sum (journal ['Johnny']) / len (journal['Johnny'])
average_K = sum (journal['Khendrik']) / len (journal['Khendrik'])
average_S = sum(journal ['Steve']) / len (journal['Steve'])

print (average_A, average_B, average_J,  average_K, average_S)
journal.update({'Aaron': average_A})
journal.update({'Bilbo': average_B})
journal.update({'Johnny': average_J})
journal.update({'Khendrik': average_K})
journal.update({'Steve':average_S})
print(journal)