# for i in range(4):
#     for j in range(4):
#         print("*", end="")
#     print("\r")

# for i in range(4):
#     for j in range(i+1):
#         print("*", end = "")
#     print("\r")

# for i in range(3):
#     for j in range(3-i):
#         print("-", end="")
    
#     for k in range(i+1):
#         print("*", end="") 
#     print("\r")
g=3

for i in range(4):
    for j in range(g):
        print(" ", end="")
    g=g-1
    for k in range(i+1):
        print("* ", end="") 
    print("\r")