#TASK 1
file1 = open('sample.txt','r')
readingfile = file1.read()
print(readingfile)
file1.close()

try:
   file1=open('sample.txt','r')

except FileNotFoundError:
    print("The file 'sample.txt' was not found.")

finally:
    print('continue with the following code')

#TASK 2

file = open('output.txt','w+')
user_input = input("Enter text to write to the file: ")
#writingfile = file.write("Hello Python")
writingfile = file.write(user_input+'\n')
#apprendingfile = file.write("Learning file handling in PYTHON.")

print(writingfile)
file.close()

file = open('output.txt','a')
user_input = input("Enter text to write to the file: ")
apprendingfile = file.write(user_input+'\n')
print(apprendingfile)
file.close()