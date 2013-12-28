---
layout: post
title: "Ubuntu 13.10 字體優化 & OpenJDK font patch"
date: 2013-12-28 20:16:22 +0800
comments: true
categories: 
- ubuntu
- font
- linux
---

最近在公司開發php的專案，使用Netbeans來作開發，但是字體有夠詭異的，所以就開始上網找解決方案了。


教學: 

在Netbean中的設定檔 ./netbeans-7.x/etc/netbeans.conf 裡面找到

    netbeans_default_options="-J-xxxx -J-xxxx"

然後在這段的最後雙引號(")前 加上

    -J-Dswing.aatext=true -J-Dawt.useSystemAAFontSettings=lcd

看起來會像這樣

    netbeans_default_options="-J-client -J-Xss2m -J-Xms32m -J-XX:PermSize=32m -J -Dapple.laf.useScreenMenuBar=true -J-Dapple.awt.graphics.UseQuartz=true -J-D sun.java2d.noddraw=true -J-Dsun.java2d.dpiaware=true -J-Dsun.zip.disableMemo ryMapping=true -J-Dswing.aatext=true -J-Dawt.useSystemAAFontSettings=lcd"


教學文章
----
然後參考以下安裝font Rendering 和 openJDK patch 就完成了!!

* [Better Font Rendering In Linux With Infinality] [1]
* [Install OpenJDK Patched With Font Fixes (ubuntu ppa)] [2]

PPA
----
如果懂ppa可以直接安裝XD

* ppa:no1wantdthisname/ppa
* ppa:no1wantdthisname/openjdk-fontfix

程式設計師用等寬字型
----

* https://github.com/adobe/source-code-pro
* http://openfontlibrary.org/font/consolamono

找了這麼久，結果最後用文泉驛等寬微米黑，因為Netbeans需要字體內有中文才能顯示中文 :/


參考資料
----

* [NetBeans IDE 字型美化 on Ubuntu Linux][3]




[1]:http://www.webupd8.org/2013/06/better-font-rendering-in-linux-with.html
[2]:http://www.webupd8.org/2013/06/install-openjdk-patched-with-font-fixes.html
[3]:http://blog.lyhdev.com/2013/11/netbeans-ide-on-ubuntu-linux.html]
