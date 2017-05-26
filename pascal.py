def triangle(n):
    arr = [[1],[1,1]]
    for i in range(1,n):
        line = []
        [line.extend([ arr[i][j] + arr[i][j+1] ]) for j in range(0,len(arr[i])-1)]
        arr.append([1] + line + [1])
    return arr

def diagonal(n, p):
    return sum([x[p] for x in triangle(n) if p <= len(x)-1])


print( 'result: ', diagonal(20, 4), '20349' )
print( 'result: ', diagonal(20, 5), '54264' )
print( 'result: ', diagonal(20, 15), '20349' )