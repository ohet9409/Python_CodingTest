result = sum([1,2,3,4,5])
print(result)

print('----------------------------')
result = min(4,2,7,6,5)
print(result)

print('----------------------------')
result = max(4,2,7,6,5)
print(result)

print('----------------------------')
result = eval("(3 + 5) * 7")
print(result)

print('----------------------------')
result = sorted([9,1,8,5,4]) # 오륾차순 정렬
print(result)

result = sorted([9,1,8,5,4], reverse= True) # 내림차순 정렬
print(result)

print('------------------------------')
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key= lambda x: x[1], reverse=True)
print(result)

print('---------------------------------')
data = [9,1,8,5,4]
data.sort()
print(data)