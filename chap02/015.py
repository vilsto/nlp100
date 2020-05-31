#15. 末尾のN行を出力
import sys
import pandas as pd

def main():
    filename_015 = "popular-names.txt"
    outfile_015 = "outfile_015.txt"

    if len(sys.argv) == 1:
        print("Please input number of rows")
    else:
        n_015 = int(sys.argv[1])
        #タブ区切りで読み込み
        df_015 = pd.read_csv(filename_015, sep = "\t", header = None)
        df_015.tail(n_015).to_csv(outfile_015, sep = '\t', index = False, header= None)

if __name__ == "__main__":
    main()

#$ tail popular-names.txt -n 5