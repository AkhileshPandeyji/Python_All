#writing to a file
filename = open("Test.txt","w")
input1 = input("Enter the thing u want to write in a file:")
filename.write(input1)

# reading from a file
filename = open("Test.txt","r")
output1 = filename.read()
print(output1)

#appending to the file
filename = open("Test.txt","a")
input2 = input("Text to Append:")
filename.write(input2)

# reading from a file
filename = open("Test.txt","r")
output1 = filename.read()
print(output1)

filename.close()

