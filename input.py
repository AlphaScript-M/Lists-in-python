list = int(input('Enter any integer'))

integer_list = []

for  i in range(1,list +1):
    integer_list.append(i)

sum = sum(integer_list)

print('the sum of the integeers from 1 to', list, 'is:', sum)