#16. ファイルをN分割する
import sys
import pandas as pd

def main():
    filename_016 = "popular-names.txt"
    outfile_016 = "outfile_016-"

    if len(sys.argv) == 1:
        print("Please input number of rows")
    else:
        n_016 = int(sys.argv[1])
        #タブ区切りで読み込み
        df_016 = pd.read_csv(filename_016, sep = "\t", header = None)
        for idx in range(n_016):
            #連番ではないがN分割
            df_016[idx::n_016].to_csv(outfile_016+str(idx), sep = '\t', index = False, header= None)

if __name__ == "__main__":
    main()

#行単位のN分割ではなく、ファイルサイズ
#$ split -n l/3 -d popular-names.txt outfile_016-cmd