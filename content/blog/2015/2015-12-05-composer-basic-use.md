Title: Composer基本用法 Part I
Date: 2015-12-05 12:14
Slug: composer-basic-use-part-1
tags: php, composer

Composer 是 PHP 的一個依賴管理工具。它允許你簡單申明項目所依賴的程式庫，就可以幫你在專案中自動的安裝他們。

### 前置作業
* 請先安裝php以及composer，[這篇文章]({filename}/blog/2015-12-03-develop-laravel-training-plan.md)的環境建立部分有安裝方法。

<!-- SUMMARY_END -->


### 實作開始

* 首先建立專案資料夾並開啟命令列 ( Mac 下的 Termial , Windows 下的 Power Shell )
* 再來執行以下指令 並根據提示回答適當的答案


```Bash
$ composer init

Package name (<vendor>/<name>) [mics/t1]: mics8128/test1 
# mics8128請改為你的 Github 名稱，如果沒有，去註冊一個。 
# test1為專案名稱，可以照這邊填寫test2

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
$ composer validate
```

* 你會看到他提示你沒有 license ，在這邊先忽視，反正這個專案沒有要發布


* 接下來執行`composer install`

```Bash
$ composer install
Loading composer repositories with package information
Installing dependencies (including require-dev)
  - Installing psr/log (1.0.0)
    Loading from cache

  - Installing monolog/monolog (1.17.2)
    Loading from cache

... # 這邊一大串是建議安裝套件，我們這邊並不需要

Writing lock file
Generating autoload files
```

* `composer install`這動作 會先檢查有沒有composer.lock，如果沒有就會根據composer.json裡面的版本敘述來安裝相關套件。
* 像是我們要求安裝monolog/monolog，但是他卻多安裝了一個psr/log，這就是因為monolog/monolog需要psr/log，他就會自動找相關的相依套件去下載。
* 然後現在已經把monolog安裝完成了，如何使用呢？
* Composer提供一個自動載入器，只需要在專案內加上一行 `require __DIR__ . '/vendor/autoload.php'`即可
* 在專案目錄下建立一個檔案叫做`test.php`
* 放入以下內容

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$log = new Monolog\Logger('name');
$log->pushHandler(new Monolog\Handler\StreamHandler('app.log', Monolog\Logger::WARNING));
$log->addWarning('Foo');

//end of test.php
```

* 然後執行 `php test.php`
* 會看到兩行警告，那是關於時區的東西，在這裡可以忽視。
* 接下來你會看到專案目錄下多出了一個app.log就是剛剛程式碼所新增的東西 (也就是Monolog所提供的功能)
* 打開該檔案會看到

```log
[2015-12-05 20:09:41] name.WARNING: Foo [] []
```


### 想一想 or 找一找

* 這是載入其他人開發的第三方程式庫，那自己開發的呢？
* 這裡只有安裝，萬一以後我想升級套件怎麼辦？

