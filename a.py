def stock_list(listOfArt, listOfCat):
	l_books = dict([b.split() for b in listOfArt])
	elements = [x for x in dict([b.split() for b in listOfArt]) if x[0] in listOfCat]
	r = [x[0] + y for x, y in l_books.items() if x in elements]
	print r
	print r.count('A')

	print l_books
	print elements

stock_list(["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B"])
#espected: "(A : 200) - (B : 1140)"