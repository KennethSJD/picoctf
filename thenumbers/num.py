input = [16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]

infile = open("numbers.txt","r")

num = infile.read()
infile.close()

num = num.replace("}","",1).replace("{","",1)
num = num.split(" ")

num = list(filter(None, num))

numb = []
for digit in num:
    numb.append(int(digit))

ans = []
for dig in numb:
    ans.append(chr(dig + 96))

print(type(numb))
print(type(dig))
print(ans.join(','))