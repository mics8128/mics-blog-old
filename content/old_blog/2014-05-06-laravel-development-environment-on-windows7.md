title: Laravel 開發環境 on Windows7 - part I - 安裝Composer
date: 2014-05-06 09:00 +0800
slug: laravel-development-environment-on-windows7

Laravel是一個最近很熱門的一個php framework，有鑑於有同學想學可是環境都是windows，有一些環境建立的障礙，所以就想說寫一篇Laravel環境建立的教學，讓windows下的使用者也可以快樂開發Laravel  :D。

大家常用的Appserv的stable版本的php太舊了，無法直接使用composer，但是開發Laravel不用composer跟跛腳沒什麼兩樣阿...所以本篇文章以最新的php版本為主，但不使用apache2 之類的的http server，而是使用php內建的開發用server，至於MySQL不在本篇教學範圍內 :P。

<!-- more -->

## 下載php
* http://windows.php.net/download/

選擇適合自己的版本
    VC11 x64 Thread Safe (for 64位元作業系統)
    VC11 x86 Thread Safe (for 32位元作業系統)
    
解壓縮到C:\php
![Screenshot from 2014-05-06 16:16:54.png](http://user-image.logdown.io/user/6349/blog/6343/post/197377/76ADaLGkRmuQEMqekgww_Screenshot%20from%202014-05-06%2016:16:54.png)

增加php到PATH內
![Screenshot from 2014-05-06 16:17:53.png](http://user-image.logdown.io/user/6349/blog/6343/post/197377/0indF8zcS5CHBs03UhJi_Screenshot%20from%202014-05-06%2016:17:53.png)

    PATH
    C:\php
    
## 啟用php擴充套件 (安裝composer必須)
用純文字編輯程式打開C:\php\php.ini (如果沒有就從php.ini-development 複製一個)
找到

    ;extension=php_openssl.dll
    
將前面的分號去掉後存檔

然後把

    C:\php\ext\php_openssl.dll
    
複製到

    C:\php\php_openssl.dll
    
    
## 安裝composer
開啟cmd
![Screenshot from 2014-05-06 16:26:24.png](http://user-image.logdown.io/user/6349/blog/6343/post/197377/R46kxDH5QQyWYHHUgB6L_Screenshot%20from%202014-05-06%2016:26:24.png)

下達以下指令
```text
C:\Users\username>C:
C:\Users\username>cd \php
C:\php>php -r "readfile('https://getcomposer.org/installer');" | php
C:\php>echo @php "%~dp0composer.phar" %*>composer.bat
```
    
## 測試composer
開啟cmd然後下達以下指令
```
C:\Users\username>composer -V
```
如果看到(後面那一大串亂亂的可能會不同)
```
Composer version 3677c1ea6905b71daf8c3c4af716d2fe2d6f85bd 2014-05-03 07:46:50
```    
代表安裝成功 :D

以下為未出篇章 改天再來寫
Part II - 使用composer與安裝laravel
Part III - laravel Quickstart
    
## 參考文件
* http://laravel.com/docs/quick
* https://getcomposer.org/doc/00-intro.md



