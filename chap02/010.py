#10. 行数のカウント
import pandas as pd

def main():
    filename_010 = "popular-names.txt"

    #タブ区切りで読み込み
    df_010 = pd.read_csv(filename_010, sep = "\t", header = None)
    #列名を設定
    df_010.columns = ["Name","Sex","Num","Year"]

    print(df_010)
    print(len(df_010))

if __name__ == "__main__":
    main()

#$ wc -l