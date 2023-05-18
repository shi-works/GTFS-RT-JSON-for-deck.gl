# GTFS-RT-JSON-for-deck.gl
本プログラムは、公共交通オープンデータセンターが公開している、[東京都交通局バスロケーション情報（GTFS-RT）](https://ckan.odpt.org/dataset/b_bus_gtfs_rt-toei)の取得及び加工を行うプログラムになります。
なお、データの加工は、[deck.glのTripsLayer](https://deck.gl/docs/api-reference/geo-layers/trips-layer)で使用可能なJSON形式への変換になります。

## データの取得(gtfs_realtime_pb2.py)
- [gtfs-realtime-binding](https://developers.google.com/transit/gtfs-realtime/examples/python-sample?hl=ja)を使用して、[公共交通オープンデータセンターのサイト](https://ckan.odpt.org/dataset/b_bus_gtfs_rt-toei)よりGTFS-RTを取得して、取得したGTFS-RTをCSV形式に変換するプログラムです。

- 取得結果  
`https://github.com/shi-works/GTFS-RT-csv2json-for-deck.gl/blob/main/ToeiBus_VehiclePosition.csv`

## データの加工(csv2json.py)
- 上記で取得したCSV形式のGTFS-RTをdeck.glのTripsLayerで使用可能なJSON形式へ変換するプログラムです。

- 変換結果  
`https://raw.githubusercontent.com/shi-works/GTFS-RT-csv2json-for-deck.gl/main/ToeiBus_VehiclePosition.json`
