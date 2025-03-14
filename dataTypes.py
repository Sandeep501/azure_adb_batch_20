# 1. List
# 2. tuple
# 3. set
# 4. dictionary

"""
program to demo datatypes
in python
"""

my_str = 'This is my string variable'
my_str = "This is my string variable"

my_str = """adfbdjnbvdsv nscvbsdjvjsdbvjdsn
ngjfnsgjfsgnfjgnfjngjsvnvvmn  nsfvvsbfvfbv
vnsnvjsnvjsfnvjfjfngfg"""

my_str = '''adfbdjnbvdsv nscvbsdjvjsdbvjdsn
ngjfnsgjfsgnfjgnfjngjsvnvvmn  nsfvvsbfvfbv
vnsnvjsnvjsfnvjfjfngfg'''

# Lists

# defining lists
my_list = [1, 2, 3, 'Kiran', 'Teja', True, 12.34]
# print(my_list)

# insert values into the list
my_list.append(100)
# print(my_list)

# delete elements
my_list.pop()
# print(my_list)

# delete a specific element from the list
my_list.remove('Kiran')
# print(my_list)

my_list.clear()
# print(my_list)

my_nums = [10, 20, 30, 40, 50, 100]
# print(my_nums[4])
# print(my_nums[:4])
# print(my_nums)
# my_nums.append(30000)
# print(my_nums)
# print(my_nums[::2])

# print(my_nums[-1])
# print(my_nums[-2])

# print(my_nums.index(40))

# [start: stop: step=1]


# tuples

my_tuple = (1, 2, 3, 4, 'Vishnu', "Alekya")
# print(my_tuple)
# print(my_tuple[4])
# print(my_tuple.)
# my_tuple[6] = "Sandeep"
# print(my_tuple)

# sets

# define set
my_set = {1, 2, 1, 2, 'Dany', 3, 4, 5}
print(my_set)

# add element
my_set.add(1000)
print(my_set)


# dictionary

# define dict
my_dict = {"name": "Teja", "age": 25, "city": "Nellore"}
print(my_dict["city"])
print(my_dict.get("name"))

my_dict["country"] = "India"
print(my_dict)

my_dict["city"] = "Tirupati"
print(my_dict)
