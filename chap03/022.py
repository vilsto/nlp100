#22. カテゴリ名の抽出
import pandas as pd
def chap03_readJsonl(chap03_filename):
    return pd.read_json(chap03_filename, lines= True, compression='infer')

def main():
    chap03_filename= 'jawiki-country.json.gz'
    df_022= chap03_readJsonl(chap03_filename)
    #クエリで抽出
    UK_Text= df_022.query("title == 'イギリス'")['text'].values[0]
 #   print(UK_Text)

    UK_TextList = UK_Text.split('\n')
#    print(UK_TextList)

    #リスト内包表記
    UK_Cate = [x for x in UK_TextList if 'Category:' in x]
    UK_CateName = UK_Cate
    print(UK_CateName)

if __name__ == "__main__":
    main()