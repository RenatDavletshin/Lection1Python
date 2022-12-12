'''
text = 'съешь ещё этих мягких французских булок'
print(len(text))
print('ещё' in text)
print(text.isdigit())
print(text.islower())
print(text.replase('ещё', 'ЕЩЁ'))

for c in text:
    print(c)
    '''

numbers = [1, 2, 3,  4, 5]
print(numbers)
ran = range(1, 6)
print(type(ran))

numbers = list(ran) # приведение типа range к типу list
print(type(numbers))
print(numbers)
numbers[0] = 10
print(f'{len(numbers)} len')
print(numbers)
for i in numbers:
    i *= 2
    print(i)
print(numbers)