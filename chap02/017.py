#17. １列目の文字列の異なり
import pandas as pd

def main():
    filename_017 = "popular-names.txt"

    df_017 = pd.read_csv(filename_017, sep = "\t", header = None)
    #重複を削除
    print(df_017[0].drop_duplicates())

if __name__ == "__main__":
    main()

#$ cut -f 1 popular-names.txt | sort | uniq -c | sort -r 