#14. 先頭からN行を出力
import sys
import pandas as pd

def main():
    filename_014 = "popular-names.txt"
    outfile_014 = "outfile_014.txt"

    if len(sys.argv) == 1:
        print("Please input number of rows")
    else:
        n_014 = int(sys.argv[1])
        #タブ区切りで読み込み
        df_014 = pd.read_csv(filename_014, sep = "\t", header = None)
        df_014.head(n_014).to_csv(outfile_014, sep = '\t', index = False, header= None)

if __name__ == "__main__":
    main()

#$ head popular-names.txt -n 5