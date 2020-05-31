#13. col1.txtとcol2.txtをマージ
import pandas as pd

def main():
    fileCol1_013 = "col1.txt"
    fileCol2_013 = "col2.txt"
    outfile_013 = "outfile_013.txt"
    
    #ファイル読み込み
    df_col1 = pd.read_csv(fileCol1_013, header= None)
    df_col2 = pd.read_csv(fileCol2_013, header= None)

    #df連結
    df_013 = pd.concat([df_col1, df_col2], axis= 1)

    #ファイル出力
    df_013.to_csv(outfile_013, sep = '\t', index = False, header= None)
    
if __name__ == "__main__":
    main()

#$ paste col1.txt col2.txt > outfile_013-cmd.txt