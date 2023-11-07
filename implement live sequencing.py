arr = [
    ['a', 2, 100],
    ['b', 2, 20],
    ['c', 1, 40],
    ['d', 3, 35],
    ['e', 1, 25]
]

arr.sort(key=lambda x: x[2], reverse=True)

t = 3

result = [False] * t

job = ['-1'] * t

for i in range(len(arr)):

    for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
      
        if result[j] is False:
            result[j] = True
            job[j] = arr[i][0]
            break


print("Following is the maximum profit sequence of Jobs: ")
print(job)
