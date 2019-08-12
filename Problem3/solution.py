test_str = input("What number are you testing? ")
test_num = int(test_str)
result = 2
#finds the highest prime factor
while test_num > result:
    if test_num % result == 0:
        test_num = test_num / result
    else:
        result += 1
print(result)
