number = {0,1,2,3,4,5,6,7,8,9}
numbers = {5,8,1,0,6,9}
missing_num = set.difference(number,numbers)

#print(missing_num)
result = sum(missing_num)
print(result)