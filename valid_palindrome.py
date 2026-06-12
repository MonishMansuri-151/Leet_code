# s=  "A man, a plan, a canal: Panama"
s = "0P"
r = s.lower()
print(r)
alp = ""
for i in range(len(r)):
    if r[i].isalnum():
        alp += r[i]
print(alp)
left = 0
right = len(alp) - 1
flag = True
while left < right:
    if alp[left] != alp[right]:
        flag = False
        break
    left += 1
    right -= 1
if flag == True:
    print("palindrome")
else:
    print("not palindrome")
