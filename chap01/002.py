#02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
str_pat="パトカー"
str_tax="タクシー"
ans_002=""

for l_pat, l_tax in zip(str_pat, str_tax):
    ans_002 = ans_002 + l_pat + l_tax

print(ans_002)
