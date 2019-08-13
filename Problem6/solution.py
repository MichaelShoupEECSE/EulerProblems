#sum of the squares
sum_of_sq = 0
for m in range(1,101):
    sum_of_sq += (m*m)
print(f"The sum of the squares is {sum_of_sq}")

#square of the sum
sq_of_sum = j = 0
for i in range(1,101):
    j += i
sq_of_sum = j*j
print(f"The square of the sum is {sq_of_sum}")
diff = sq_of_sum - sum_of_sq
print(f"The difference is {diff}")
