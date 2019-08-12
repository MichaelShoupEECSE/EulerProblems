#Initiate the starting points according to problem
item_1=1
item_2=2
next_item=0
total=0

#Iterate until the Fib value exceeds 4 million
while item_1 <= 4000000:
        #Sum the total of even Fib numbers
        if item_1 % 2 == 0:
                total += item_1
        #Prepare numbers for next iteration
        next_item = item_1+item_2
        item_1=item_2
        item_2=next_item
        
print(f"Total is: {total}")
