def last_digit(n1, n2):
    #if n2 == 0 : return 1
    #if str(n1)[-1] == '0': return 0
    #position = mod(n2, 4)
    position = n2%4
    positions = [str(pow(n1,0))[-1], str(pow(n1,1))[-1], str(pow(n1,2))[-1], str(pow(n1,3))[-1],str(pow(n1,4))[-1] ]
    return int(positions[position+1])
    return positions

def mod(a,b):
    c=a/b
    d=c*b
    modulo=a-d
    return int(round(modulo))

"""
for x in range(0,10):
    print( last_digit(2, x) )
"""
print( last_digit(4, 1) ) #4
#print( last_digit(4, 2) ) #6
#print( last_digit(9, 7) ) #9
#print( last_digit(10, 10 ** 10) ) #0
#print( last_digit(2 ** 200, 2 ** 300) ) #6
#print( last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651) ) #7