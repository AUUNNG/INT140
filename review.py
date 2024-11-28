# def f1(x:int, y:int):
#     if x < y:
#         return True
#     return False
# print(f1(1,2))

# def f2(x:int):
#     list = []
#     if x < 0:
#         for i in range(x, 1):
#             list.append(i)
#     for i in range(0, x+1):
#         list.append(i)
#     return list
# print(f2(-5))

# def f3(list):
#     count = 0
#     min = 0
#     for i in list:
#         if i < min:
#             min = i
#             count = 1
#         elif i == min:
#             count += 1
#     return count
#
# list = [1, -2, 3, 4, -2, -2]
# print(f3(list))

# def f(list):
#     count = 0
#     for i in range(len(list)):
#         print(list[i])
#         if list[i] == True:
#             count += 1
#     return count
# 
# def f4(list):
#     count = f(list)
#     return count
# 
# list = [True, True, False, False, False]
# print(f4(list))

# def f5(list):
#     min = float('inf')
#     minSecond = float('inf')
#     for i in list:
#         if i < min:
#             minSecond = min
#             min = i
#         elif i < minSecond and i != min:
#             minSecond = i
#         return minSecond
# list = [5,1,2,3,4,6]
# print(f5(list))
