#11. タブをスペースに置換
import pandas as pd

def main():
    filename_011 = "popular-names.txt"
    outfile_011 = "outfile_011.txt"

    #タブ区切りで読み込み
    df_011 = pd.read_csv(filename_011, sep = "\t", header = None)
    #スペース区切りで出力 (indexなし)
    df_011.to_csv(outfile_011, sep = ' ', index = False, header= None)

if __name__ == "__main__":
    main()

#$ sed "s/\t/ /g" popular-names.txt > outfile_011-cmd.txt