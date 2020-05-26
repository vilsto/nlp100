#03. 円周率
import re

str_003 ="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
ans_003 = []

split_003 = (re.sub('[.,]', '', str_003)).split()

for l_word in split_003:
    ans_003 += [len(l_word)]

print(ans_003)