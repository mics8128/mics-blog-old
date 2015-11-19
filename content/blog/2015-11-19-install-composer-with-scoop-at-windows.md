Title: 在Windows中使用Scoop安裝php與Composer
Date: 2015-11-19 20:58
Slug: install-composer-with-scoop-at-windows
tags: composer, php, scoop, windows

因為我周邊的開發者都使用Windows，因此特意寫了這篇文章，給我周邊的開發者練習使用在windows下的文字介面，由於安裝scoop需要powershell 3，win7或win7以下使用者請先安裝powershell 3 (請參考[在 Lync Online 中下載並安裝 Windows PowerShell 3.0](https://technet.microsoft.com/zh-tw/library/dn362783(v=ocs.15).aspx) 沒有實測過)
<!-- PELICAN_END_SUMMARY -->

## 開始安裝Scoop
* 請先打開powershell執行


```
    set-executionpolicy unrestricted -s cu
```

* 然後按Y後按Enter

![執行原則變更]({filename}/images/2015-11-19/1.png)

* 接下來先安裝scoop然後安裝php

```
    iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
    scoop install php
```

* 靜待安裝完畢

![安裝scoop與php]({filename}/images/2015-11-19/2.png)

* 測試php是否正常執行

![測試php是否正常執行]({filename}/images/2015-11-19/3.png)

* 到``C:\Users\YOUR USER NAME\AppData\Local\scoop``

![找到scoop]({filename}/images/2015-11-19/4.png)

* 三個資料夾的功能分別是
    * apps  - 存放scoop安裝的程式的資料
    * cache - 安裝檔案暫存
    * shims - 執行檔案(安裝的時候已經加入PATH中)

* 再來進到``.\apps\php\5.6.15``中(**注意**版本號可能會不同)，找到``php.ini``

* 搜尋

```
; extension_dir = "ext"
```

* 改成 (注意 **YOUR USER NAME** 和版本號 **5.6.15**可能會不同，請自行隨機應變)

```
extension_dir = "C:\Users\YOUR USER NAME\AppData\Local\scoop\apps\php\5.6.15\ext"
```

* 再找到

```
;extension=php_openssl.dll
```

* 把前面的分號``;``去掉

* 然後存檔

* 進入執行檔目錄(composer直接安裝在這裡)

```
cd \Users\YOUR USER NAME\AppData\Local\scoop\shims
```

* 安裝composer並設定執行script

```
php -r "readfile('https://getcomposer.org/installer');" | php
wget https://gist.githubusercontent.com/mics8128/de1ea57536a56aa48673/raw/268f1c15091a728ef2e051a81a5980c4531d89af/composer.bat -OutFile composer.bat
```

* 最後測試我們的composer有沒有正常

```
composer.bat
```

![composer test]({filename}/images/2015-11-19/5.png)


# 大功告成拉~ YA

##以下是選用安裝的軟體 都只要一個指令喔^.<

* Git版本管理系統，在powershell執行``scoop install git``
* (暫時想不到其他的 隨時補充)



