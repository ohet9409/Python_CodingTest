# 정수형
a = 1000 # 양의 정수
print(a)

a = -7 # 음의 정수
print(a)

# 0
a = 0
print(a)

print('--------------------')
# 실수형
a = 157.93 # 양의 실수
print(a)

a = -5157.93 # 음의 실수
print(a)

a = 5. # 소수부가 0일 때 0을 생략
print(a)

a = -.7 # 정수부가 0일 때 0을 생략
print(a)
print('--------------------')

a = 1e9 # 10억의 지수 표현 방식
print(a)

a = 75.25e1 # 752.5
print(a)

a = 3954e-3 # 3.954
print(a)
print('--------------------')

a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

print('--------------------')

a = 0.3 + 0.6
print(round(a, 4))

if round(a,4) == 0.9:
    print(True)
else:
    print(False)

print("---------------")
a = 7
b = 3

# 나누기
print(a / b)

# 나머지
print(a % b)

# 몫
print(a // b)

# 거듭제곱
a = 5
b = 3
print(a ** b)