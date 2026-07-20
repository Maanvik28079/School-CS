s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
len1 = len(s1)

prefix = s2[:len1]
postfix = s2[-len1:]

if s1 == prefix:
    print("Output: Prefix")
    
elif s1 == postfix:
    print("Output: Postfix")
    
else:
    print("Neither prefix nor postfix")