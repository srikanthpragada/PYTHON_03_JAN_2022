# Take a file and display unique words in sorted order

filename = input("Enter filename : ")
f = open(filename, "rt")
contents = f.read()

words = contents.split(" ")

for w in sorted(set(words)):
    print(w)
