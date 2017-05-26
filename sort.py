def example_sort(arr, example_arr):
	tmp = []
	[tmp.append(x) for x in example_arr for y in arr if y == x]
	return tmp


#print example_sort([1,2,3,4,5],[2,3,4,1,5])
#print example_sort([1,2,3,3,3,4,5],[2,3,4,1,5]) #[2,3,3,3,4,1,5]
#example_sort([1,2,3,3,3,5],[2,3,4,1,5]),[2,3,3,3,1,5]
#example_sort([1,2,3,3,3,5],[3,4,5,6,9,11,12,13,1,7,8,2,10]),[3,3,3,5,1,2]
#example_sort(["a","a","b","f","d","a"],["c","a","d","b","e","f"]),["a","a","a","d","b","f"]
#example_sort(["Alice","Bryan","Chad","Darrell","Ellie","Fiona"],["Alice","Bryan","Chad","Darrell","Ellie","Fiona"])
#["Alice","Bryan","Chad","Darrell","Ellie","Fiona"]