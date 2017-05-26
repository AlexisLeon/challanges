# https://www.codewars.com/kata/52a382ee44408cea2500074c/train/python
def minor(matrix,i):
    """Returns the Minor M_0i of matrix"""
    minor = matrix
    del minor[0] #Delete first row
    #for b in list(range(len(matrix))): #Delete column i
    for b in list(range(len(minor))): 
        del minor[b][i]
    return minor

def determinant(A):
    """Recursive function to find determinant"""
    if len(A) == 1: #Base case on which recursion ends
        return A[0][0]
    else:
        determinant = 0
        for x in list(range(len(A))): #Iterates along first row finding cofactors
            print("A:", A)
            determinant += A[0][x] * (-1)**(2+x) * determinant(minor(A,x)) #Adds successive elements times their cofactors
            print("determinant:", determinant)
        return determinant

m1 = [ [1, 3], [2,5]]
m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]

print determinant([[1]]) # 1
print determinant(m1) # -1
print determinant(m2) # -20