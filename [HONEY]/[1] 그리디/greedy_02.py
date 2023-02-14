# 실전 문제 | 숫자 카드 게임
# 시간 제한 1초 | 메모리 제한 128MB
n, m = map(int, input().split())
min_list = list()

for i in range(n):
    num_list = list(map(int, input().split()))
    num_list.sort()
    min_list.append(num_list[0])

min_list.sort()
print(min_list[n-1])

# 문제 풀이 시간  || 15분 13초
# 시간 측정 결과  || 7.9초 (입력시간 포함)
