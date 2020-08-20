# room-management

Nature Remo APIを使用したスマート家電の効率化

## Run

### 必要なもの

- Docker
- Nature Remo
- Nature Remo API token
- (Python 3.~)

### ライトのIDを取得する

- Pythonが必要

1. user.jsonの`token`にNature Remo APIのTokenを入力
2. 以下のコマンドを入力

```bash
sh get_data.sh
```

3. output.jsonが生成されるのでその中からライトONのIDとOFFのIDを取得

<details>
<summary>出力ファイル例</summary>

```json
[
    {
        "id": "[id]",
        "device": {
            "name": "[name]",
            "id": "[id]",
            "created_at": "2020-08-17T09:19:34Z",
            "updated_at": "2020-08-20T12:07:33Z",
            "mac_address": "[mac_address]",
            "bt_mac_address": "[bt_mac_address]",
            "serial_number": "[serial_number]",
            "firmware_version": "Remo/1.0.27",
            "temperature_offset": 0,
            "humidity_offset": 0
        },
        "model": null,
        "type": "IR",
        "nickname": "照明",
        "image": "ico_light",
        "settings": null,
        "aircon": null,
        "signals": [
            {
                "id": "[ ここがONのID ]",
                "name": "オン",
                "image": "ico_on"
            },
            {
                "id": "[ ここがOFFのID ]",
                "name": "オフ",
                "image": "ico_off"
            }
        ]
    }
    ...
]
```

</details>

4. user.jsonの`light_id_on`、`light_id_off`に入力
5. LINE notifyのアクセストークンをuser.jsonの`line_token`に入力
6. Docker起動

```bash
docker-compose up -d
```

## ライセンス

MIT
