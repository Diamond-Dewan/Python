num_list = [1, 3, 4, 'Math', 5, 6, 7, 8]

sum = 0

for num in num_list:
    if type(num) == int:
        sum += num

print('Sum is: {sum}'.format(sum=sum))
