Title: 使用chocolatey升級Windows7下的Powershell到最新版本
Date: 2015-12-01 20:28
Slug: upgrade-windows7-powershell-to-new-version-by-chocolatey
tags: windows, chocolatey, powersehll

因為安裝 scoop 需要 PowerShell 3.0 以上版本, 但是 Windows 7 內建的 PowerShell 的版本號是 2.0，安裝時會遇到一些問題，在這邊附上使用 chocolatey 在 windows 7 上安裝 Powershell 4.0 的方法

假如你已經是 windows 8 或以上 powershell 版本應該已經足夠安裝 scoop 了, 但是 chocolatey 是一套套件管理程式 也可以用來安裝軟體(ex. FileZilla, Notepad++, virtualBox 等)，更多詳細資料可以參考[官方網站](https://chocolatey.org/packages)，在這邊開始教學。

<!-- SUMMARY_END -->

* 首先以**系統管理員**模式開啟cmd.exe

![開啟cmd.exe]({filename}/images/2015-12-01/1.png)

* 然後執行以下指令

```
@powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
```

* 此指令的作用是安裝choco這個套件管理系統
* 我在測試時會看到一些警告訊息, 但是不影響使用, 所以可以繼續以下步驟.
* 接下來關閉 cmd.exe 然後以**系統管理員**模式打開 powershell (不要開錯了喔, 是 powershell 不是 cmd.exe )

![開啟powershell]({filename}/images/2015-12-01/2.png)

* 然後執行以下指令

```
choco install powershell -y
```

* 此指令會幫你完成安裝 powershell 所需要做的動作
* 但是因為 powershell 是 windows 系統元件所以務必要重新開機
* 接下來務必要記得需要 **重開機**
* 不要忘記 **重開機**
* 記得 **要重開機**

#重開機之後
#重開機之後
#重開機之後

* 很重要所以寫三遍
* 接下來確認 powershell 是否成功的更新了
* 確認方法: 打開 powershell (不需要管理權限)後執行

```
$PSVersionTable.PSVersion
```

* 最後會看到以下訊息就是正確升級了

```
Major  Minor  Build  Revision
-----  -----  -----  --------
4      0      -1     -1
```
