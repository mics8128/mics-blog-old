Title: Laravel Installer 安裝與使用
Date: 2015-12-06 02:12
Slug: laravel-installer-basic
tags: php, composer, laravel

在這邊介紹使用 laravel installer 來初始化 laravel 專案，並使用 php 附帶的 http server 執行測試伺服器。

<!-- SUMMARY_END -->

```Bash
$ composer global require laravel/installer
```

此指令的 global 意思是安裝在家目錄下，通常使用 global 的時候是安裝一些指令列工具，這一行的作用是安裝 laravel installer。

Laravel installer 的好處是創新專案的時候比較快一點，因為正常使用 composer 時，他會去處理相依性問題，會分別下載所有的相依套件。使用此程式則有一個伺服器負責天天處理好相依性問題並打包成單一壓縮檔案。在執行安裝時直接下載該檔案來解壓縮，會比分別下載快很多。

安裝完成後執行 `laravel --version` 確定是否安裝正確

```Bash
$ laravel --version
Laravel Installer version 1.2.2
```

在這邊僅測試過 MAC 環境，請 Windows 環境使用者測試看看。

假如無法找到 laravel 指令在這邊回報一下，我之後能測試 Windows 環境的時候會加上作法。

接下來就可以使用 laravel installer 創建新專案，在指令列執行 `laravel new laravel-new-project` ，最後面的 `laravel-new-project` 是專案名稱，可以隨意更改。

(提示說找不到laravel指令的可以先用 composer 直接創建專案 `composer create-project laravel/laravel laravel-new-project`)

```Bash
$ laravel new laravel-new-project
Crafting application...
> php -r "copy('.env.example', '.env');"
> php artisan clear-compiled
> php artisan optimize
Generating optimized class loader
> php artisan key:generate
Application key [myD1M6xsWMjkdMYBampWwW7EBwogtzxN] set successfully.
Application ready! Build something amazing.
```

就會在當下目錄看到一個laravel-new-project的資料夾，讓我們進去裡面並且看看有什麼檔案

```Bash
$ cd laravel-new-project
```

在這邊先只介紹幾個重要檔案，其他的部分會在後續慢慢瞭解。

* app - 最重要的部分，你即將寫程式的檔案位置。
* artisan - laravel的命令列工具，下面即將會用到這個工具建立簡易的伺服器來測試我們的第一個laravel app
* composer.json - composer篇已經說過的，套件相依的檔案
* composer.lock - composer篇已經說過的，套件相依的檔案
* public - 靜態檔案請放在這邊( css, js ..等等 )
* vendor - composer篇已經介紹過，第三方套件的放置處
 

接下來執行 `php artisan serve`

```Bash
$ php artisan serve
Laravel development server started on http://localhost:8000/
```

然後連到 [http://localhost:8000/](http://localhost:8000/)

就會看到 Laravel 5 在畫面中央，恭喜你成功創建了一個什麼功能都沒有的 Laravel App。

最後後回到指令列 Ctrl + C 結束測試伺服器
