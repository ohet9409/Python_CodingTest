# 제어문

a = 1
if (a < 5):
  print("맞음")
else:
  print("틀림")

title = "삼성전자 왜 떨어져??"
a = "삼성전자" in title
print(a);

if a > 6:
  print("맞음")
elif a == 1:
  print("1이구만")
else:
  print ("다 틀렸어")

# 반복문
a = [1,2,3]
for tmp1 in a:
  print(tmp1)

range(100)
for tmp in range(5):
  print("시작")
  print(tmp)

for tmp in range(50,56):
  print(tmp)


# 짝수만 출력
for tmp in range(50,55, 2):
  print(tmp)

for i in range(10):
  if i == 5:
    break
  else:
    print(i)

