# Comparing two tuples

'''
*how python compare two tuples??

While comparing two tuple:

    t1[0] == t2[0] -> passed ELSE not passed
    t1[1] == t2[1] ->   --    --   -    --
    t1[2] == t2[2] ->   --    --   -    --

if all these items matched one aginst another 
then they are equal.

'''

t1 = (2, 3, 4)
t2 = (1, 2, 3)
t3 = (2, 3, 4)

if t1 == t2:
    print("Matched")

elif t1 == t3:
    print('Matched')

else:
    print('Not Matched')
