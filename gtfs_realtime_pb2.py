from google.transit import gtfs_realtime_pb2
import requests
import csv
import datetime
import time
from collections import OrderedDict

# 出力するCSVファイルのパスを定義
output_csvfile = "./ToeiBus_VehiclePosition.csv"

# 出力ファイルを'追加モード'で開き、エンコーディングをUTF-8に設定
with open(output_csvfile, 'a', encoding='utf-8') as f:

    # CSVファイルのヘッダー行を定義
    fieldnames = ['id', 'trip_id', 'schedule_relationship',
                  'route_id', 'direction_id', 'longitude', 'latitude', 'current_stop_sequence', 'timestamp', 'timestamp_date', 'stop_id', 'vehicle_id', 'vehicle_label']

    # CSVファイルへの書き込みオブジェクトを作成
    csvfile_writer = csv.DictWriter(
        f, fieldnames=fieldnames, lineterminator='\n')

    # ヘッダー行を出力
    csvfile_writer.writeheader()

    # 開始時間と終了時間を指定
    start_time = datetime.time(12, 5, 0)  # 11:20:00
    end_time = datetime.time(15, 0, 0)  # 15:00:00

    # 1440回のデータ取得を行う
    for num in range(1440):

        # 現在時刻を取得
        now_time = datetime.datetime.now().time()

        # 現在時刻が開始時間と終了時間の範囲内であればデータ取得を行う
        if start_time <= now_time <= end_time:

            # GTFSリアルタイムデータを取得するためのURLからデータフィードをダウンロード
            feed = gtfs_realtime_pb2.FeedMessage()
            try:
                response = requests.get(
                    'https://api-public.odpt.org/api/v4/gtfs/realtime/ToeiBus')
                response.raise_for_status()  # レスポンスがエラーであれば例外を発生させます
            except requests.exceptions.RequestException as err:
                print("データ取得失敗:", err)
                continue  # データ取得に失敗したら次のループへ進みます

            # レスポンス内容をパース
            feed.ParseFromString(response.content)

            # デバッグ情報の出力
            print(feed, 5)

            # フィード内の各エンティティに対する処理
            for entity in feed.entity:

                # タイムスタンプをdatetime型に変換
                dt = datetime.datetime.fromtimestamp(entity.vehicle.timestamp)

                # 各エンティティの情報をCSVファイルに書き込み
                csvfile_writer.writerow({
                    'id': entity.id,
                    'trip_id': entity.vehicle.trip.trip_id,
                    'schedule_relationship': entity.vehicle.trip.schedule_relationship,
                    'route_id': entity.vehicle.trip.route_id,
                    'direction_id': entity.vehicle.trip.direction_id,
                    'longitude': entity.vehicle.position.longitude,
                    'latitude': entity.vehicle.position.latitude,
                    'current_stop_sequence': entity.vehicle.current_stop_sequence,
                    'timestamp': entity.vehicle.timestamp,
                    'timestamp_date': dt,
                    'stop_id': entity.vehicle.stop_id,
                    'vehicle_id': entity.vehicle.vehicle.id,
                    'vehicle_label': entity.vehicle.vehicle.label
                })

        # 次のデータ取得まで1分間の待機
        time.sleep(60)

    print(u'処理終了')
