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

```:/etc/dhcpd.conf
(略)
interface wlan0
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant

interface wlan1
    env wpa_supplicant_conf=/etc/wpa_supplicant/wpa_supplicant-wlan1.conf
```

```:/etc/sysctl.d/routed-ap.conf
# Enable IPv4 routing
net.ipv4.ip_forward=1
```

外付けWi-FiモジュールからIPマスカレードして出ていくように設定
```bash
sudo iptables -t nat -A POSTROUTING -o wlan1 -j MASQUERADE
```

```:/etc/dnsmasq.conf
# Listening interface
interface=wlan0

# Pool of IP addresses served via DHCP
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h

# Local wireless DNS domain
domain=wlan

# Alias for this router
address=/gw.wlan/192.168.4.1
```
