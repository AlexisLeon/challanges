#matrix = [[1, 2, 3], [-3, -2, 1], [3, - 1, 2]]
#total_sum = (1 - 2 + 3) + [-(-3) + (-2) - 1] + [3 - (-1) + 2] = 2 + 0 + 6 = 8

#pos = 1, 3, -2, 3, 2     =>
#neg = 2, -3, 1, - 1      =>

def score_matrix(matrix):
    arr = []
    for x in matrix:
        total = 0
        print x
        for n in x[0::2]:
            if n > 0: total += n
            else: total -= abs(n)
            print 'two', total
        for n in x[1::2]:
            if n > 0: total += n
            else: total -= abs(n)
            print 'odd', total
        arr.append(total)

print( score_matrix([[1, 2, 3], [-3, -2, 1], [3, -1, 2]]) ) #  8
#print( score_matrix([[1, 2, 3, 4], [-3, -2, 1, 1], [3, 8, -1, 2], [20, 5, 10, -4], [10, -8, -8, 4]])) # -32
print( score_matrix([[2,3,2,3], [2,3,2,3], [2,3,2,3]]) ) # -2