from lab06 import *
# adder1 = make_adder_inc(5)
# adder2 = make_adder_inc(6)
# print(adder1(2))
# print(adder1(2))

# 内层函数不能修改外层函数的值，除非值为非本地变量nonlocal
# def make_withdraw(balance):
#     def withdraw(amount):
#         nonlocal balance
#         if amount > balance:
#             return 'Insufficient funds'
#         balance = balance - amount
#         return balance
#     return withdraw

# fib = make_fib()
# print(fib())
# print(fib())
# print(fib())
# print(fib())
# print(fib())
# test_lst = [1, 5, 8, 5, 2, 3]
# new_lst = insert_items(test_lst, 5, 5)
# print(new_lst)
# test_lst.index(5)
