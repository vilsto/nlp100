#04. 元素記号Permalink
import re
str_004="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
list_004=[1, 5, 6, 7, 8, 9, 15, 16, 19]
ans_004={}

split_004 = (re.sub(r'[,.]', '', str_004)).split()

for i, l_word in enumerate(split_004):
    i += 1 
    if i in list_004:
        ans_004[i] = l_word[0:1]
    else:
        ans_004[i] = l_word[0:2]

print(ans_004)