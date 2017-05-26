def is_valid_IP(strng):
    elements = strng.split('.')
    if len(elements) != 4 : return False
    lenght = 0
    for e in elements:
        if not e.isdigit(): return False
        if e[0] == '0': return False
        lenght += len(e)
    if lenght <= 7: return False
    return True # if all it's ok, return True

print(is_valid_IP('12.255.56.1'))     #True
print(is_valid_IP('71.97.8.157'))     #True
print(is_valid_IP(''))                #False
print(is_valid_IP('abc.def.ghi.jkl')) #False
print(is_valid_IP('123.456.789.0'))   #False
print(is_valid_IP('12.34.56'))        #False
print(is_valid_IP('12.34.56 .1'))     #False
print(is_valid_IP('12.34.56.-1'))     #False
print(is_valid_IP('123.045.067.089')) #False