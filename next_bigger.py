from itertools import permutations

def next_bigger(n):
	return min([x for x in [int(''.join(perm)) for perm in permutations(str(n))] if x > n])

#print( next_bigger(12) ) # 21
#print( next_bigger(513) ) # 531
#print( next_bigger(2017) ) # 2071
#print( next_bigger(414) ) # 441
#print( next_bigger(144) ) # 414