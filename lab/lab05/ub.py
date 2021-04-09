from lab05 import *


berkeley = make_city('Berkeley', 37.87, 112.26)
stanford = make_city('Stanford', 34.05, 118.25)
# print(closer_city(38.33, 121.44, berkeley, stanford))
# print(type(tree('berry')))
scrat = tree('berry')
sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
# print(berry_finder(scrat))
# print(tree([1,2,[3]]))
t1 = tree(1, [tree(2), tree(3)])
new1 = sprout_leaves(t1, [4, 5])
print_tree(new1)
# for i in sproul:
#     # print(i)
#     if type(i) == list:
#         for j in i:
#             if type(j) == list:
#                 for k in j:
#                     print(k)

