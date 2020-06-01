#18. 各行を3コラム目の数値の降順にソート
import pandas as pd

def main():
    filename_018= "popular-names.txt"

    df_018= pd.read_csv(filename_018, sep= "\t", header= None)
    #ソート
    print(df_018.sort_values(2, ascending= False))

if __name__ == "__main__":
    main()

#$ sort -r -k 3 popular-names.txt