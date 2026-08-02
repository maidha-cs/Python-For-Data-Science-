list1 = ["Maidha " ,"blcs/2k24/40" , 56.6]
print(type(list1))
print(len(list1))
print(list1)
print(list1[1])
# now we use Nested List
List2 = [ " hello" ,["how , are , yo"]]
print(List2[1])
new_list= List2[1]
print(List2)
# List Concat
list1 = [1,2,3,4]
list2 = [5,6,7,8 ]
list3= list1 + list2
print(list3)
# Adding to an existing List
list4 = [1,3,5,7,9]
add = list4 + [11,13,15,17]
print(add)
# Membership in list
# ya show kare ga jo no hum da rahaa hein woh us list mein hai ya nh
print(2 in add)
print(3 in add)
# Mutability
Sub_List = ["Sci , Eng , Math , Biology" " "]
Sub_List[2] = " Computer Science"
print(Sub_List)