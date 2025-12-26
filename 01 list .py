friends=["apple","banana","cherry",5,3.5,"mango","grape"]

print(friends[0])      # Output: apple

friends[0]="orange"  # Changing the first item
print(friends)        # Output: ['orange', 'banana', 'cherry', 5, True, 3.5, 'mango', 'grape']

friends[5]="pineapple"  # Changing the sixth item
print(friends)          # Output: ['orange', 'banana', 'cherry', 5, True, 'pineapple', 'mango', 'grape']

# unlike strings lists are mutable but strings are immutable


print(friends[1:4])    # Output: ['banana', 'cherry', 5]
