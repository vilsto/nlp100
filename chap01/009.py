#09. Typoglycemia
import random

def typoglycemia(typo):
    typo_list = typo.split()
    typo_result = []
    for l_word in typo_list:
        if len(l_word) <= 4 :
            typo_result.append(l_word)
        else:
            shuffle = ''.join(random.sample(l_word[1:-1],len(l_word)-2))
            typo_result.append(l_word[0] + shuffle + l_word[-1])
    return ' '.join(typo_result)

def main():
    str_009 = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

    print(str_009)
    print(typoglycemia(str_009))

if __name__ == "__main__":
    main()