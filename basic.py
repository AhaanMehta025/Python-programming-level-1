# name = "Ahaan"
# rollno = "35"
# r = 35
# print(name,rollno)

# print (type(name))
# print(type(rollno))
# print(type(r))# r is integer 


# # name = input("Enter your name: ")
# # print("Hi,",name)

# print(10%3)

#------loop -----------
# for i in range(10):
#     if i==5:
#         continue
#     print(i)

# j = 1
# while j<11 :
#     if j==5:
#         continue
#     print(j)
#     j+=1

#--------------module_-----------------
# import math


# from random import randint
# print(randint(1,10))

#-------------dictionary------------
# a = 'Ths is a sentence.'
# a = ['This is sentence 1','This is sentence 2']
# if 'This is sentence 1' in a:
#     print('yes')

d = {
    'name': 'ahaan',
    'is':'okay',
    'type':{'1':'sad','2':'happy'}


}
for a,d in d['type'].items():
    print(a,'is',d)
# # print(d['type'][1])

# print(d.keys())
# print(d.values())
# print(d.items())

# for a,d in d.items():
#     print(a,'is',d)

 #----------string sclicing----------------

# a='this'

# print(a[1:3])