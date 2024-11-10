# 문자열
str = "안녕!";
print(str);
print(str[0]);

# 딕셔너리
my_dict = {
  "123": 1,
  "23": 2,
}
print(my_dict["123"]);
print(my_dict)

# 집합 - 중복제거
a = {1,2,2,3};
a.add(4)
print(a);
b = [1,2,3, 3];
b.append(66);
print(b);

# 집합으로 변환
c = set(b);
print(c);

# 불(bool, boolean)
a = 1;
print(a == 1);
print(type(a == 1));
# and: 모두 True 일경우 True 리턴
print(True and True);
print(True and False);

# or: 하나라도 True 일 경우 True 리턴
print(True or True);
print(True or False);

# 함수
def f(a, b):
  result = a + 1;
  result = result + b;
  return result;

print(f(3,4));

# 기본값을 넣어주면 값이 없을경우 기본값 출력 (반드시 맨 뒤에 위치하도록)
def f2(a, b = 10, c = 99):
  result = a + b + c;
  return result;

print(f2(1));
print(f2(1,2));
print(f2(1,2,3));

