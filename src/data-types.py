#

'''
Numeric - int, float, complex
String - str
Sequence - list, tuple, range
Binary - bytes, bytearray, memoryview
Mapping - dict
Boolean - bool
Set - set, frozenset
None - NoneType

'''

age = 20
percentage = 67.67
name = "Abhishek"
isValid = True

# List is similar to Array defined with [] and can be accessed by [0] or :
list = ['abcd', 786, 2.23, 'john', 70.2]
# tuple is similar to List which can be updated or modified. It can be read only.
tuple = ('abcd', 786, 2.23, 'john', 70.2)  # it is readonly list

# range(start, stop, step)
for i in range(5):
    print(i)

# Python dictionaries are kind of hash table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs.

dict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(dict)
print(dict['name'])
print(dict['code'])
print(dict['dept'])
