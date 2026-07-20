s1 = input("Enter String: ")

frequency = {}

for char in s1:
    if char == " ":
        continue
    frequency[char] = frequency.get(char, 0) + 1

l1 = s1.split(" ")
maxlen = 0
word = ""
for l in l1:
    if len(l) > maxlen:
        maxlen = len(l)
        word = l

newstr = ""
l1len = len(l1)
for j in range(0, l1len - 1):
    newstr = newstr + ((list(l1[j]))[0]) + " "
    
newstr = newstr + (l1[-1])
newstr = newstr.title()
    



print(f"Frequency of each letter is:  {frequency}")
print("")
print(f"The word of highest length is:  {word}")
print("")
print(f"The string in title case is:  {s1.title()}")
print("")
print(f"Only the initials with last word is:  {newstr}")