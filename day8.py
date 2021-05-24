# Day 8: Dictionaries and Maps
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phonebook = {}

for i in range(n):
    line = input()
    pair = line.split()
    phonebook[pair[0]] = pair[1]

while True:
    try:
        q = input()
        if q in phonebook:
            print(str(q) + "=" + str(phonebook[q]))
        else:
            print("Not found")
    except:
        break
