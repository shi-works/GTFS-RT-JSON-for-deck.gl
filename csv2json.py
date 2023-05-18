import pandas as pd
import json

# CSVファイルからデータを読み込む
df = pd.read_csv('ToeiBus_VehiclePosition.csv')

# 空白行を削除する
df = df.dropna(how='all')

# データをtrip_idでグループ化し、timestampでソートする
grouped = df.sort_values('timestamp').groupby('trip_id')

# 結果となるリスト
result = []

# 各グループに対して処理を行う
for name, group in grouped:
    path = group[['longitude', 'latitude']].values.tolist()
    timestamps = group['timestamp'].values.tolist()

    # データを辞書形式で格納し、リストに追加する
    result.append({
        "vendor": 0, 
        "path": path, 
        "timestamps": timestamps
    })

# 結果をJSON形式に変換し、新しいファイルに書き出す
with open('ToeiBus_VehiclePosition.json', 'w') as f:
    json.dump(result, f, indent=2)
