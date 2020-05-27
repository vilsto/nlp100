#07. テンプレートによる文生成
def temp_template(x, y, z):
    return f'{x}時の{y}は{z}です'   #f文字列

def main():
    x_007 = 12
    y_007 = "気温"
    z_007 = 22.4

    print(temp_template(x_007, y_007, z_007))

if __name__ == "__main__":
    main()
