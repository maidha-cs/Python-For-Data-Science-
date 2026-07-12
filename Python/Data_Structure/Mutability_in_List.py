list1 = ["English, Science , Computer , Math "]
#list1[0] = "Computer Science"
#print(list1[0])
# " Extend Function " us mein hum ( .extend ) ka use kar ka list ko extend kar daein ga
list1.extend(["physics, Biology , Chemistry "])
print(list1)
# " Append Function "  us mein hum ( .append ) ka use kar ka list ka anda dusri list
# banai ga
list1.append([1,2,3,4,5,6,7,8])
print(list1)
# " Delete Function "
del list1[2][3]
print(list1)
print(len(list1))
 # POP
 # Remove