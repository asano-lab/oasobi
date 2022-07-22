# 環境
- ラズパイ3B+
- wifiモジュール

# ラズパイ

hostapdのインストール
```bash
sudo apt install hostapd
```

# Wi-Fi (子機側) の設定
```:/etc/wpa_supplicant/wpa_supplicant-wlan1.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=JP

network={
        ssid="ネットワーク名"
        psk="パスフレーズ"
}
```
