#Matthew Choi
#CS 100 2022F Section 009
#HW 05, Oct 02, 2022

list_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
for months in list_months :
    print(months)


print(' ')

list_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
for months in list_months :
    if months[0] == 'J':
        print(months)

print(' ')
for numbers in range(0,100):
    print(numbers)

print(' ')
for numbers in range(0,100):
    if int(numbers)%2 == 0 and int(numbers)%5 == 0:
        print(numbers)


horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for vowel in horton:
    if vowel in vowels[0:9]: 
        print(vowel)
