#.append is used to add an element at the end of the list

friends=["Rolf","Bob","Jen","Anne","Charlie","Kat",2.5,20]
print(friends)

friends.append("mohan")
print(friends)


# .sort is used to sort the list in ascending order
numbers=[5,2,9,1,5,6]
print(numbers)  
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]

# .reverse is used to reverse the order of the list

numbers1=[5,2,9,1,5,6]
print(numbers1)
numbers1.reverse()
print(numbers1)  # Output: [6, 5, 1, 9, 2, 5]


# .insert is used to insert an element at a specific index
fruits=["apple","banana","cherry"]
fruits.insert(2,"orange")  # Inserting 'orange' at index 2
print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry']

# .remove is used to remove a specific element from the list
fruits1=["apple","banana","cherry","banana"]
fruits1.remove("banana")  # Removing the first occurrence of 'banana'
print(fruits1)  # Output: ['apple', 'cherry', 'banana']

# .pop is used to remove an element at a specific index and return it
fruits2=["apple","banana","cherry"]
removed_fruit=fruits2.pop(1)  # Removing the element at index 1
print(removed_fruit)  # Output: banana 
print(fruits2)  # Output: ['apple', 'cherry']


numbers5=[5,2,9,1,5,6]

print(numbers5.pop(2)) # Output: 9
print(numbers5)        # Output: [5, 2, 1, 5, 6]

# .clear is used to remove all elements from the list
numbers6=[5,2,9,1,5,6]
numbers6.clear()
print(numbers6)  # Output: []

# .count is used to count the occurrences of a specific element in the list
numbers7=[5,2,9,1,5,6,5]
count_5=numbers7.count(5)
print(count_5)  # Output: 3

# .extend is used to add elements from another list (or any iterable) to the end of the list
numbers8=[1,2,3]
numbers8.extend([4,5,6])
print(numbers8)  # Output: [1, 2, 3, 4, 5, 6]

# You can also use .extend with strings, tuples, or sets
numbers9=[1,2,3]
numbers9.extend("45")
print(numbers9)  # Output: [1, 2, 3, '4', '5']

# .index is used to find the index of the first occurrence of a specific element in the list
numbers10=[5,2,9,1,5,6]
index_5=numbers10.index(5)
print(index_5)  # Output: 0

# .copy is used to create a shallow copy of the list
numbers11=[5,2,9,1,5,6]
numbers11_copy=numbers11.copy()
print(numbers11_copy)  # Output: [5, 2, 9, 1, 5, 6]


       



