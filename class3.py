#LIST METHOD
color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(color_list.index('Red'))

print('Welcome to the Astroverse!!')

# choice = input('Enter your favourite color\n>')
# position = int(input('Enter the Position\n>'))

# color_list.append(choice)

# color_list.insert(position, choice)

# data = input('Enter your colors seperated by space:\n')
# cleaned_data = data.split()

#cleaned_data.extend(color_list) <-INTERCHANGEABLE TO BRING ANYONE TO THE FRONT
# color_list.extend(cleaned_data)
# print(color_list) 

#To pop
# li = [0, 2, 9, 8]
# a = li.pop(1)
# li.append(a)
# print(li)

#to copy
# a=[1,5,7,2]
# b = a
# c = a.copy()
#d = a.find(2) <-- For Strings
# e = a.index(5)
# print(c)
#print(d)
# print(e)

# my_tuple = 1, 2, 3, 4, 5, 6
# print(my_tuple)

# a = {1, 2, 4, 6}
# b = {2, 4, 1, 5}

# c = a.difference(b)
#b.intersection_update(a)
# c = a.symmetric_difference(b)
# print(c)

english = input('Enter roll number for english students:\n>')
french = input('Enter roll number for french students:\n>')

english_list = english.split()
french_list = french.split()

english_set = set(english_list)
french_set = set(french_list)

# total = english_set.symmetric_difference(french_set)
total = english_set.union(french_set)


print(len(total))






