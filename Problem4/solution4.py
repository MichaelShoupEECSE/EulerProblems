num_1=num_2=test_1=result=1

for i in range(100, 1000):
    for j in range(100, 1000):
        product_int = i*j
        #cast the int as a string so it is iterable (for reversing)
        product_str = str(product_int)
        product_str_rev=''
        #reverse the string
        for c in product_str[::-1]:
            product_str_rev+=c
        #check if they are palindromes
        if product_str == product_str_rev:
            if product_int < result:
                break
            test_2=product_int
            if test_2 > test_1:
                result = test_2
print(result)

