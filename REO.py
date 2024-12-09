file = open('File.txt','r')
print(file.read())
file.close()

file = open('File.txt','w')
print(file.write('I am the best programmer and ethical hacker'))
file.close()

file = open('File.txt','a')
print(file.write('\nTo the next line'))