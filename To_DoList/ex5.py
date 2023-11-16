file = open('members.txt', 'r')
members = file.readlines()
file.close()

user = input("Member to add: ")
members.append(user)

file = open('members.txt', 'w')
file.writelines(members)
file.close()
