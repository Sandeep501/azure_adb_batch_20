# print even numbers
# 2, 4, 6, 8

# for i in range(2, 21):
#     if i % 2 == 0:
#         print(i, end=" ")
             
even = []
odd = []

for i in range(1, 21):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

# print(even)
# print(odd)

city = "Nellore"
vowels = ['a', 'e', 'i', 'o', 'u']
c = 0

for i in city:
    if i in vowels:
        c += 1

print("no.of vowel letters in", city, "is", c)
        
