from cats import *

# dogs = about(['dogs', 'hounds'])
# print(dogs('Release the Hounds!'))
# print(dogs('"DOGS" stands for Department Of Geophysical Science.'))
# print(wpm("", 10))
# first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
# print(autocorrect("inside", ["idea", "inside"], first_diff, 0.5))

p = [[17, 22, 27], [1, 5, 9]]
game = time_per_word(p, ['construction', 'upbid'])
all_words(game)
print(all_times(game))


