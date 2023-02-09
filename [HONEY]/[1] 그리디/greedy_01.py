# 실전 문제 / 큰 수의 법칙
# 시간 제한 1초 / 메모리 제한 128MB

n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()
sum = 0
count = 0

for i in range(m):
    count += 1
    if k <= count:
        count = 0
        sum += num_list[n - 2]
    else:
        sum += num_list[n - 1]

print(sum)

# 문제 풀이 시간 12분 50초
# 시간 측정 결과 0.0초 (입력 시간 제외)
