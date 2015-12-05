Title: 快速部署laravel到heroku
Date: 2015-10-01 00:07 -0500
Slug: fast-deploy-laravel-to-heroku
Tags: php, laravel

環境需求

* PHP
* Composer
* [Heroku toolbelt](https://toolbelt.heroku.com/)

Windows使用者前兩個可以參考我的前一篇文章[Laravel 開發環境 on Windows7]({filename}../old_blog/2014-05-06-laravel-development-environment-on-windows7.md)，不過本篇是以Unix like系統為角度撰寫，Windows使用者可能需要自行變通

<!-- SUMMARY_END -->

登入並在heroku創建專案

    :::bash
    $ heroku login
    Enter your Heroku credentials.
    Email: yout@email.address
    Password (typing will be hidden):
    $ heroku create
    Creating mighty-scrubland-5244... done, stack is cedar-14
    https://mighty-scrubland-5244.herokuapp.com/ | https://git.heroku.com/mighty-scrubland-5244.gi

把專案名稱記下來，在這裡是*mighty-scrubland-5244*，**<font color=red>後面請都將此字串取代為你自己的專案名稱</font>**。

在本機使用composer創造一個新專案

    :::bash
    $ composer create-project laravel/laravel laravel-heroku

    # 進入Project資料夾
    $ cd laravel-heroku

增加Procfile

    :::bash
    $ echo web: vendor/bin/heroku-php-apache2 public > Procfile
    # 此檔案用意是告訴http server我們的根目錄是public

Windows下可以直接把以下內容複製到Procfile裡面

    web: vendor/bin/heroku-php-apache2 public

初始化git

    :::bash
    $ git init
    $ git add .
    $ git commit -am "init"

    # 增加remote端
    $ heroku git:remote -a mighty-scrubland-5244

    # 設定此app為php app
    $ heroku buildpacks:set https://github.com/heroku/heroku-buildpack-php

    # 把本地端的master推送到heroku
    $ git push heroku master

然後到 http://mighty-scrubland-5244.herokuapp.com 觀看 (請記得改成你自己得專案名稱)

你會看到

    Whoops, looks like something went wrong.

會出現的原因是環境參數沒有設定

    :::bash
    # 觀看環境參數
    $ cat .env
    APP_ENV=local
    APP_DEBUG=true
    APP_KEY=ZMz9G6vGDWHT1HZAA9GNUZCsiYlAYCw9

    DB_HOST=localhost
    DB_DATABASE=homestead
    DB_USERNAME=homestead
    DB_PASSWORD=secret

    CACHE_DRIVER=file
    SESSION_DRIVER=file
    QUEUE_DRIVER=sync

    MAIL_DRIVER=smtp
    MAIL_HOST=mailtrap.io
    MAIL_PORT=2525
    MAIL_USERNAME=null
    MAIL_PASSWORD=null
    MAIL_ENCRYPTION=null

    # 設定參數 請記得把ZMz9G6.....改成自己的
    $ heroku config:set APP_KEY=ZMz9G6vGDWHT1HZAA9GNUZCsiYlAYCw9
    Setting config vars and restarting mighty-scrubland-5244... done, v6
    APP_KEY: ZMz9G6vGDWHT1HZAA9GNUZCsiYlAYCw9
    # 其他的DATABASE USERNAME也可以以同樣方法設定 這裏沒有用到就不設定了

最後再到同一個網址按下F5 就可以看到Laravel 5了~
