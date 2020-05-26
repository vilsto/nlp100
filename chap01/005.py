#05. n-gram
import re
def n_gram(target, n):
    return [target[idx:idx+n] for idx in range(len(target)+1 -n)]

str_005 = "I am an NLPer"
print(n_gram(str_005, 2))
print(n_gram((re.sub(r'[.,]', '', str_005)).split(), 2))
