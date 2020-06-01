#19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
import pandas as pd

def main():
    filename_019= "popular-names.txt"

    df_019= pd.read_csv(filename_019, sep= "\t", header= None)
    #1列目の要素と要素数
    print(df_019[0].value_counts())

if __name__ == "__main__":
    main()

#$ 