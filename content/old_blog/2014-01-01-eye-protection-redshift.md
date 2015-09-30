title: 保護眼睛? Redshift
date: 2014-01-01 06:50 +0800
slug: eye-protection-redshift

今天回老家的時候，我跟跟我推薦了一個保護眼睛的軟體，叫做[f.lux](http://justgetflux.com/)，不過他用在ubuntu會有一些莫名其妙的小問題，我也解決不了只好找替代軟體了，上網搜尋了一下找到[Redshift](http://jonls.dk/redshift/)這套軟體，於是就把他裝上去了。

詳細安裝方法請繼續閱讀
<!-- more -->

因為Ubuntu 13.10套件庫內已經有了，所以直接安裝即可

    sudo apt-get install gtk-redshift redshift python-appindicator
    gtk-redshift

以上為安裝和執行
如果要自訂設定請下以下指令

    vim ~/.config/redshift.conf

(如果有其他編輯器請把vim替換 ex.gedit nano)

貼上
```ini redshift.conf
; Global settings for redshift
[redshift]
; Set the day and night screen temperatures
temp-day=5700
temp-night=3500

; Enable/Disable a smooth transition between day and night
; 0 will cause a direct change from day to night screen temperature. 
; 1 will gradually increase or decrease the screen temperature
transition=1

; Set the screen brightness. Default is 1.0
;brightness=0.9
; It is also possible to use different settings for day and night since version 1.8.
;brightness-day=0.7
;brightness-night=0.4
; Set the screen gamma (for all colors, or each color channel individually)
gamma=0.8
;gamma=0.8:0.7:0.8

; Set the location-provider: 'geoclue', 'gnome-clock', 'manual'
; type 'redshift -l list' to see possible values
; The location provider settings are in a different section.
location-provider=manual

; Set the adjustment-method: 'randr', 'vidmode'
; type 'redshift -m list' to see all possible values
; 'randr' is the preferred method, 'vidmode' is an older API
; but works in some cases when 'randr' does not.
; The adjustment method settings are in a different section.
adjustment-method=randr

; Configuration of the location-provider:
; type 'redshift -l PROVIDER:help' to see the settings
; ex: 'redshift -l manual:help'
[manual]
lat=23.50
lon=121.00
;hawaii :D
; lat=21.28
; lon=157.81

```
這是我的設定檔，給大家參考參考


如果想要自動執行

    vim ~/.config/autostart/redshift.desktop

貼上
```desktop redshift.desktop
[Desktop Entry]
Type=Application
Exec=/usr/bin/gtk-redshift
Icon=
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=GTK-Redshift
GenericName=gtk-redshift
X-GNOME-FullName=Redshift
Comment=good redshift :D
```