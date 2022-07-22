[ほぼこれと同じ](https://www.raspberrypi.com/documentation/computers/configuration.html#setting-up-a-routed-wireless-access-point)
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

`wpa_passphrase 'ネットワーク名' 'パスフレーズ'`を実行することで、
パスフレーズを暗号化できる

```:/etc/dhcpd.conf
(略)
interface wlan0
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant

interface wlan1
    env wpa_supplicant_conf=/etc/wpa_supplicant/wpa_supplicant-wlan1.conf

interface eth0
        static ip_address=192.168.5.1/24
```

```:/etc/sysctl.d/routed-ap.conf
# Enable IPv4 routing
net.ipv4.ip_forward=1
```

外付けWi-FiモジュールからIPマスカレードして出ていくように設定
```bash
sudo iptables -t nat -A POSTROUTING -o wlan1 -j MASQUERADE
```

よくわからないけどなんかうまくいったファイルの中身
```:/etc/dnsmasq.conf
interface=wlan0
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
domain=wlan
address=/gw.wlan/192.168.4.1

interface=eth0
dhcp-range=192.168.5.2,192.168.5.20,255.255.255.0,24h
domain=eth
address=/gw.eth/192.168.5.1
```
