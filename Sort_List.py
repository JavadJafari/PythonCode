#sort_list
print( "                         welcome                      ")
print ( "                        by   jey                      ")
nums = []
while True:
    while True:
        n = input("Enter numbers for your list and the next enter'print': ")
        if n == 'print':
            break
        nums.append(int(n))
        sorted_nums = sorted(nums)
    print("Your List Is " , sorted_nums)
