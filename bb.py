def bubbleSort(arr):
    n = len(arr)

    for num in range(n - 1):
        for j in range(0, n - num - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

list = [5,2,8,1,3,6,9,0,4]
bubbleSort(list)

print(f"Bubble sort: {list}")





a = [1,4,3,2,5,8,6,7,9,0]
a.sort()
print(f'Binary search : {a}')

value = int(input())

mid = len(a) // 2
low = 0
high = len(a) - 1

while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No value")
