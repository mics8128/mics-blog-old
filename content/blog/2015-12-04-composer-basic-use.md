Title: Composer基本用法
Date: 2015-12-04 16:54
Slug: composer-basic-use
tags: php, composer
Status: draft

Composer 是 PHP 的一個依賴管理工具。它允許你簡單申明項目所依賴的程式庫，就可以幫你在專案中自動的安裝他們。

### 前置作業
* 請先安裝php以及composer，[這篇文章]({filename}/blog/2015-12-03-develop-laravel-training-plan.md)的環境建立部分有安裝方法。


### 實作開始

* 首先建立專案資料夾並開啟命令列 ( Mac 下的 Termial , Windows 下的 Power Shell )
* 再來執行以下指令 並根據提示回答適當的答案


```Bash
$ composer init

Package name (<vendor>/<name>) [mics/t1]: mics8128/test1 
# mics8128請改為你的 Github 名稱，如果沒有，去註冊一個。 
# test1為專案名稱，可以照這邊填寫test1

Description []:
# 專案說明 在這邊空白即可

Author [Mics <mics.mm@gmail.com>]:
# 作者 空白或填上自己暱稱/姓名 都可以

Minimum Stability []:
Package Type []:
License []:
# 以上三個空白即可，在這邊不重要

Would you like to define your dependencies (require) interactively [yes]? no
Would you like to define your dev dependencies (require-dev) interactively [yes]? no
# 這兩個先空白，稍後手動新增

Do you confirm generation [yes]?
# 在這之前會有一大串，就是即將生成的 composer.json 檔案內容，在這邊直接按 Enter ，同意生成設定檔。
```

* 可以看到專案的跟目錄下有一個檔案 composer.json，我的 composer.json 長得像這樣。

```json
{
    "name": "mics8128/test1",
    "authors": [
        {
            "name": "Mics",
            "email": "mics.mm@gmail.com"
        }
    ],
    "require": {}
}
```

* 在這邊修改require那一行

```json
{
    "name": "mics8128/test1",
    "authors": [
        {
            "name": "Mics",
            "email": "mics.mm@gmail.com"
        }
    ],
    "require": {
        "monolog/monolog": "^1.17"
    }
}
```

* 然後執行以下指令驗證 composer.json 有沒有錯誤

```
composer validate
```

* 你會看到他提示你沒有 license ，在這邊先忽視，反正這個專案沒有要給大家使用 :P
