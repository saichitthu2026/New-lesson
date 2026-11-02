# # # i = 1 
# # # while i < 6:
# # #     print(i)
# # #     i = i+1

# # value = "not exit"
# # while value.lower() !="shutdown":
# #     value= input("Do You wnat to exit? type 'shutdown'")




# subject=["eng","mya","math","phy","chem"]
# marks=[]
# loop = 0

# while loop<len(subject):
#     mark = int(input(f"how many marks?{subject[loop]}\n"))
#     marks.append(mark)
#     loop = loop+1
# print(marks)


# subject=["eng","mya","math","phy","chem"]
# marks=[]
# loop = 0
# while loop<len(subject):
#     mark = int(input(f"how many marks?{subject[loop]}\n"))
#     if mark>=80:
#         marks.append("A")
#     elif mark>=70:
#         marks.append("B")
#     elif mark>=60:
#         marks.append("C")
#     elif mark>=40:
#         marks.append("D")
#     else:
#         marks.append("E")
    
#     loop = loop+1
# print(marks)



# subject=["eng","mya","math","phy","chem"]
# print(len(subject))


number = range(10)

for number in range(10):
    cnumber=number
    pnumber=number
    if number==0:
        pnumber=0
    else:
        pnumber=cnumber-1
    snumber=cnumber+pnumber

    print(f"Current Number {cnumber} Previous Number{pnumber} sum:{snumber}")
