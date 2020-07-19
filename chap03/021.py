#21. カテゴリ名を含む行を抽出Permalink
import pandas as pd
def chap03_readJsonl(chap03_filename):
    return pd.read_json(chap03_filename, lines= True, compression='infer')

def main():
    chap03_filename= 'jawiki-country.json.gz'
    df_021= chap03_readJsonl(chap03_filename)
    #クエリで抽出
    UK_Text= df_021.query("title == 'イギリス'")['text'].values[0]
 #   print(UK_Text)

    UK_TextList = UK_Text.split('\n')
#    print(UK_TextList)

    #リスト内包表記
    UK_TextCate = [x for x in UK_TextList if 'Category:' in x]
    print(UK_TextCate)

if __name__ == "__main__":
    main()