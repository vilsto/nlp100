#21. カテゴリ名を含む行を抽出Permalink
import pandas as pd
def chap03_readJsonl(chap03_filename):
    return pd.read_json(chap03_filename, lines= True, compression='infer')

def main():
    chap03_filename= 'jawiki-country.json.gz'
    df_021= chap03_readJsonl(chap03_filename)
    #クエリで抽出
    df_UK= df_020.query("title == 'イギリス'")

    

if __name__ == "__main__":
    main()