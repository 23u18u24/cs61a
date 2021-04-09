from hw05 import *
v = VendingMachine('candy', 10)
print(v.vend())
#'Inventory empty. Restocking required.'
print(v.add_funds(15))
#'Inventory empty. Restocking required. Here is your $15.'
print(v.restock(2))
#'Current candy stock: 2'
print(v.vend())
#'You must add $10 more funds.'
print(v.add_funds(7))
#'Current balance: $7'
print(v.vend())
#'You must add $3 more funds.'
print(v.add_funds(5))

