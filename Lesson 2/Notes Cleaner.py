file=open("bucket-list.txt", "w")
file.write("1. Visit the Eiffel Tower\n")
file.write("2. Learn to play the guitar\n")
file.write("3. Code my own game\n")
file.close()

n=int(input("How many characters to preview? : "))
file=open("bucket-list.txt","r")
print(file.read(n))
print()

file=open("bucket-list.txt","r")
lines=file.readlines()
file.close()
print("Total lines : ",len(lines))
for i in range (len(lines)):
    print(i+1,"->",lines[i].strip())
print()

word=input("Skip lines starting with : ")
file=open("bucket-list.txt","r")
for line in file:
    if line.startswith(word):
        print("Skip -> ",line.strip())
    else:
        print("Keep -> ",line.strip())
file.close()
print()

file=open("bucket-list.txt","r")
line=file.readlines()
out=open("Odd-lines.txt","w")
for i in range (0,len(line),2):
    out.write(lines[i])
out.close()
print("Odd lines laved to Odd-lines.txt")