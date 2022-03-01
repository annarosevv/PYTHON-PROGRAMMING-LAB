str1=input('Enter The String: ')
char=str1[0]
str1=str1.replace(char,'$')
str1=char+str1[1:]
print(str1)
