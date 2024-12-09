file = open('File.txt','r')
print(file.read())
file.close()

file = open('File.txt','w')
print(file.write('I am the best programmer and ethical hacker'))
file.close()

file = open('File.txt','a')
print(file.write('\nTo the next line'))

file = open('File.txt','a+')
file2 = open('App.txt','r')
file.write(file2.read())

file.seek(0)
file2.seek(0)

file.close()
file2.close()
