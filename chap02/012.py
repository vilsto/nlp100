#1列目をcol1.txtに，2列目をcol2.txtに保存
import pandas as pd

def main():
    filename_012 = "popular-names.txt"
    outfile_col1 = "col1.txt"
    outfile_col2 = "col2.txt"

    #タブ区切りで読み込み
    df_012 = pd.read_csv(filename_012, sep = "\t", header = None)

    #指定列をファイル出力
    df_012.to_csv(outfile_col1, columns= [0], index= None, header= None)
    df_012.to_csv(outfile_col2, columns= [1], index= None, header= None)

if __name__ == "__main__":
    main()


#$ cut -f 1 popular-names.txt > col1-cmd.txt
#$ cut -f 2 popular-names.txt > col2-cmd.txt