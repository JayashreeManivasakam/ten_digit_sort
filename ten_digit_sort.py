A = list(map(int, input("Enter the array: ").split()))
sorted_array = sorted(A, key=lambda num: (num // 10) % 10)
print(sorted_array)
