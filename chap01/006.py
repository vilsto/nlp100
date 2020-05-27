#06. 集合
def n_gram(target, n):
    return [target[idx:idx+n] for idx in range(len(target)+1 -n)]

def main():
    str_X = "paraparaparadise"
    str_Y = "paragraph"

    bi_X = set(n_gram(str_X, 2))
    bi_Y = set(n_gram(str_Y, 2))

    union = bi_X | bi_Y
    inter = bi_X & bi_Y
    comp = bi_X - bi_Y

    print(bi_X, bi_Y)
    print(union, inter, comp)

    if "se" in bi_X:
        print("bi_X in se")
    else:
        print("bi_X not in se")
    if "se" in bi_Y:
        print("bi_Y in se")
    else:
        print("bi_Y not in se")

if __name__ == "__main__":
    main()