my_array = ["kinga", 182, 47.5, True, (1, 2, 3)]
firstArrayLength = len(my_array)
my_array.append([5, 6, 7])
secondArrayLength = len(my_array)
print("Difference:", secondArrayLength - firstArrayLength)