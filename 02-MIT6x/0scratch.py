################################################################################
## SCRATCH PAD FOR MITx 6.001
################################################################################

# num = 10
# print(num)
# for num in range(5):
#     print(num)
# print(num)


# for variable in range(20):
#     if variable % 4 == 0:
#         print(variable)
#     if variable % 16 == 0:
#         print('Foo!')

# count = 0
# for letter in 'Snow!':
#     print('Letter # ' + str(count) + ' is ' + str(letter))
#     count += 1
#     break
# print(count)

# divisor = 2
# for num in range(0, 10, 2):
#     print(num/divisor) 



# school = 'Massachusetts Institute of Technology'
# numVowels = 0
# numCons = 0

# for char in school:
#     if char == 'a' or char == 'e' or char == 'i' \
#        or char == 'o' or char == 'u':
#         numVowels += 1
#     elif char == 'o' or char == 'M':
#         print(char)
#     else:
#         numCons -= 1

# print('numVowels is: ' + str(numVowels))
# print('numCons is: ' + str(numCons)) 



# greeting = 'Hello!'
# count = 0

# for letter in greeting:
#     count += 1
#     if count % 2 == 0:
#         print(letter)
#     print(letter)

# print('done')



# iteration = 0
# count = 0
# while iteration < 5:
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# print("!!!BREAK!!!!")


# count = 0
# phrase = "hello, world"
# for iteration in range(5):
#     count += len(phrase)
#     print("Iteration " + str(iteration) + "; count is: " + str(count))




# x = 25
# epsilon = 0.01
# step = 0.1
# guess = 0.0

# while guess <= x:
#     if abs(guess**2 -x) < epsilon:
#         break
#     else:
#         guess += step

# if abs(guess**2 - x) >= epsilon:
#     print('failed')
# else:
#     print('succeeded: ' + str(guess))




# x = 23
# epsilon = 0.01
# step = 0.1
# guess = 0.0

# while abs(guess**2-x) >= epsilon:
#     print(guess)
#     if guess <= x:
#         guess += step
#     else:
#         break

# if abs(guess**2 - x) >= epsilon:
#     print('failed')
# else:
#     print('succeeded: ' + str(guess))


# Notice how if we have two print statements                
# print("Hi")
# print("there")

# # The output will have each string on a separate line:                
# # Hi
# # there
                
# # Now try adding the following:
# print("Hi",end='')
# print("there")
# print("Hi",end='*')
# print("there")   
                



