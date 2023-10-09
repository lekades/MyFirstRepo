###CODE ASK USER TO ENTER n NUMBER, PRINT HE LIST AND SUM OF ALL NUMBER ENTERED (Ver.1)
def add_nums():
    num_list = []
    n = int(input("how many numbers do you want to add"))
    while len(num_list) <= n-1:
        user_num = int(input('please enter a number to add:'))
        num_list.append(user_num)
    print('You have entered the following numbers: ',num_list)
    total_num_sum = 0
    for x in num_list:
        total_num_sum += x 
    print('total sum of numbers = ',total_num_sum)
add_nums()
