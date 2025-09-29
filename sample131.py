import pandas as pd
import sqlite3

# DataFrameを作成
val = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df = pd.DataFrame(val, index=[0, 1, 2], columns=['a', 'b', 'c'])

# データベースとテーブル名
db_name = "F:/sample131.db"
table_name = "test"

# with文で接続し、DataFrameを保存
with sqlite3.connect(db_name) as conn:
    df.to_sql(table_name, conn, if_exists='replace', index=False)

# with文で接続し、保存されたデータを確認
with sqlite3.connect(db_name) as conn:
    print(pd.read_sql(f"SELECT * FROM {table_name}", conn))