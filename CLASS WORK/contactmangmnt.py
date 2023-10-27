userinfo = []
student = {}
def storeinfo():
    name = input("Enter user name:" )
    reg = input("Take reg. no. :" )
    phonenum = input("Take phone no. :" )
    student['Name'] = name
    student['Regno.'] = reg
    student['Phoneno.'] = phonenum
    userinfo.append(student)

storeinfo()

# To add more user details
def addinfo():
    student[input('')] = input()
    student[input('')] = input()
    print(student)
addinfo()



