#

abcde = ['a', 'b', 'c', 'd', 'e']
xyzwp = ['x', 'y', 'z', 'w', 'p']
numlist = ['1', '2', '3', '4', '5']

Result = tuple(map(lambda x, y , z : (x,y,z), abcde,xyzwp,numlist))

print(Result)
