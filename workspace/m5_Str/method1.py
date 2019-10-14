s1 = 'abc'
s2 = '123'
s3 = 'abc123'

print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())
print(s1.isalpha())
print(s2.isalpha())
print(s3.isalpha())
print(s1.isdigit())
print(s2.isdigit())
print(s3.isdigit())

print(s1.isidentifier())
print(s2.isidentifier())
print(s3.isidentifier())
print('a-1'.isidentifier())
print('_a'.isidentifier())
print(s1.islower())
print(s1.isupper())
print('ABC'.isupper())
print('AbC'.isupper())
print('isspace()')
print('AbC'.isspace())
print(''.isspace())
print(' '.isspace())
print('\n'.isspace())
print('\t'.isspace())