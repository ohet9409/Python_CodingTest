# 선택 정렬과 기본정렬 라이브러리 수행 시간 비교
from random import randint
import time

# 배열에 10000개의 정수를 삽입
array = []
for _ in range(10000):
    array.append(randint(1, 100)) # 1 부터 100 사이의 랜덤한 정숴

print("배열 초기화: ", array)
# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

end_time = time.time() # 측정 종료
print("정렬 확인: ", array)
print("선택 정렬 성능 측정: ", end_time - start_time) # 수행 시간 출력

# 배열을 다시 무작위 데이터로 초기화
array2 = []
for _ in range(10000):
    array2.append(randint(1,100)) # 1부터 100 사이의 랜덤한 정수
print("배열 초기화: ", array2)
# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array2.sort()

end_time = time.time() # 측정 종료
print("정렬 확인: ", array2)
print("기본 정렬 라이브러리 성능 측정:" , end_time - start_time) # 수행 시간 측정