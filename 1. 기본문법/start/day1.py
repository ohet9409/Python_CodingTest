print(1);
# 숫자형
a=1;
print(a+1);

# 리스트
alist = [90,10,62, 'abc'];
print(alist);
print(alist[3]);
print(alist[-1]);
print(alist[1:3]);
print(alist[1:]);
print(alist[-2:]);
print(type(alist));

# 튜플은 수정 불가
print("---------------------");
aTuple = (1,2);
print(aTuple);
print(type(aTuple))
print(aTuple[0])
aTuple[0] = 2;
print(aTuple(0));