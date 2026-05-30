def square(num):
    result = []
    for i in num:
        result.append(i*i)
    return result

my_num = square([1,2,3,4])   
print(my_num)     

📋 Expected Output: [1, 4, 9, 16]


#using Generator
def square(num):
    for i in num:
        yield (i*i)

my_num = square([1,2,3,4]) 


print(my_num)    #<generator object square at 0x7fc344b44fb0>
print(next((my_num)))  #1
print(next((my_num)))  #4
print(next((my_num)))  #9
print(next((my_num)))  #16


def square(num):
    for i in num:
        yield (i*i)

 my_num = square([1,2,3,4])

for j in my_num:
     print(j)

📋 Expected Output:  1
4
9
16

my_num = [x*x for x in [1,2,3,4]]  # using list comprehension
print(my_num)

📋 Expected Output: [1, 4, 9, 16]
