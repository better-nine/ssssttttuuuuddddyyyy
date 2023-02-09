from random import randint
import time

# 10,000개의 정수
array = []
for _ in range(10000):
    array.append(randint(1, 100))  # 1부터 100까지의 랜덤한 정수

# 선택정렬
start_time = time.time()  # 측정시작

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
        array[i], array[min_index] = array[min_index], array[i]  # 스와피

end_time = time.time()  # 측정종료
print("time : ", end_time - start_time)

# 초기화
array = []
for _ in range(10000):
    array.append(randint(1, 100))


# 기본 정렬 라이브러리
start_time = time.time()

array.sort()

end_time = time.time()
print("time : ", end_time - start_time)
