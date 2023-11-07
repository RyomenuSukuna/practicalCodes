arr = [
    ['a', 2, 100],
    ['b', 2, 20],
    ['c', 1, 40],
    ['d', 3, 35],
    ['e', 1, 25]
]

# Sort jobs by decreasing order of profit
arr.sort(key=lambda x: x[2], reverse=True)

# Total time slots available
t = 3

# To keep track of free time slots
result = [False] * t

# To store the result (Sequence of jobs)
job = ['-1'] * t

# Iterate through all given jobs
for i in range(len(arr)):
    # Find a free slot for this job
    for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
        # Free slot found
        if result[j] is False:
            result[j] = True
            job[j] = arr[i][0]
            break

# Print the sequence
print("Following is the maximum profit sequence of Jobs: ")
print(job)
