str1 = "welcome to dat encience masters"

str1.replace('dat', 'data').replace('encience','science')

print(str1.replace('dat', 'data').replace('encience','science'));


print(1.9999999999 in [2,4,5])


lst = [1,2,3,4,5,6,7,8]

oddSum=0
evenSum=0

for i in (lst):
    if i%2==0:
        evenSum= i+evenSum
    else:
        oddSum= i+oddSum

print(oddSum, evenSum, "sum")


evenNum = [num for num in lst if num%2==0]
print(sum(evenNum))

lst1 = [1,2,3,4,5,6,7,8]
print([num**2 for num in lst1])

cel_temp= [0,10,20,30,40,50]

print([(9/5)*temp+32 for temp in cel_temp ])

# flatten a list of lists into a single list

lists = [[1,2,3], [4,5,6], [7,8,9]]

print([num for sublist in lists for num in sublist])

#create a list of only prime no from a given list

numbers=[1,2,3,4,5,6,7,8,9,10]

# create a list of all positive combination of 2 elements from a list

numbers = [1,2,3,4,5]