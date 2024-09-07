tuple_ = 1, 2, 'a','b'
tuple_name = "Immutable tuple:"
print(tuple_name, tuple_)
#tuple_[0] [0]= 3
# tuple_ [0] не изменился, так как переменная tuple_ не изменятся, если нет [] внутри кортежа

#Mutable
tuple_list = ([1], [ 2 ], [3], ['a'], ['b'])
print (tuple_list)
name = 'Mutable list:'
tuple_list [ 0 ] [ 0 ] = 5
print (tuple_list )
print (tuple_name, tuple_)
print (name, tuple_list)
