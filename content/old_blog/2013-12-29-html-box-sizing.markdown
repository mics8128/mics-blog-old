title: html box sizing
date: 2013-12-29 12:25:25 +0800
slug: html-box-sizing

以前在寫網頁CSS的時候下面這三個加起來，會等於你的總寬度

- border
- padding
- width

但是大家覺得數學並不好玩，所以到了新世代，應該要有新方法，以下這個方法適用於IE8以上

    * { 
         -webkit-box-sizing: border-box; /* Safari/Chrome, other WebKit */
         -moz-box-sizing: border-box;    /* Firefox, other Gecko */
         box-sizing: border-box;         /* Opera/IE 8+ */
    }

這個方法呢，會讓*內容+padding+border = 設定寬度*，多美好阿:D 


參考資料
----
[http://zh.learnlayout.com/box-sizing.html]()





