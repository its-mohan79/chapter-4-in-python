a=(1,45,342,3424,False,"rohan","mohan")  #tuple creation
print(type(a))


t = (1, 2, 3)
t2 = 1, 2, 3   # parentheses optional
print(t)
print(t2)
print(t[0])
print(t2[1])
print(t[-1])  # last element
print(t2[-2])  # second last element
print(t[1:3])  # slicing



t = (5,)   # comma mandatory
print(type(t))   # <class 'tuple'>




# Accessing elements

t = (10, 20, 30)  
print(t[0])    # 10         #
print(t[-1])   # 30




# Slicing
t = (1, 2, 3, 4, 5)
print(t[1:4])   # (2, 3, 4)


# Tuple concatenation and repetition

t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)   # (1, 2, 3, 4)

# Tuple repetition
t = (1, 2)
print(t * 3)   # (1, 2, 1, 2, 1, 2)


# Membership testing

t = (10, 20, 30)
print(20 in t)      # True
print(40 not in t)  # True



# Tuple functions

t = (5, 2, 9)
print(len(t))   # 3
print(min(t))   # 2
print(max(t))   # 9
print(sum(t))   # 16


# Tuple methods

t = (1, 2, 2, 3)

print(t.count(2))   # 2
print(t.index(3))   # 3

# Immutability of tuples

t = list(t)
t[0] = 10
t = tuple(t)
print(t)   # (10, 2, 2, 3)



# Nested tuples

t = (1, (2, 3), 4)
print(t[1][0])   # 2
print(t[1][1])   # 3



# Accessing elements in nested tuples

t = (1, (2, 3), 4)

print(t[0])   # 1
print(t[1])   # (2, 3)
print(t[2])   # 4
