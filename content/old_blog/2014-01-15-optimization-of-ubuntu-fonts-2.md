title: Ubuntu字體優化 - 去除GB 18030
date: 2014-01-15 21:01 +0800
slug: optimization-of-ubuntu

一直以來我都沒有什麼注意字體的部份，只要看的順眼，沒有鋸齒狀（上一篇文章 [Netbeans on Ubuntu字體優化](http://mics.logdown.com/posts/2013/12/28/ubuntu-fonts-optimization) 就是因為有了鋸齒所以我想要改進)，就可以接受了，但是今天在Facebook上看到了同學轉發了一篇文章([小心！GB 18030 就在你身邊](http://www.techbang.com/posts/16514))，突然驚覺我在使用的字體居然有這麼多簡體中文的成份存在，我向來是不寫簡體字的，雖然看得懂，但是書寫時仍然以繁體為主，今天看到這篇文章之後我立刻查看了Ubuntu預設的繁體中文字體，居然是簡體的格式，今天就要來把這問題修正。
<!-- PELICAN_END_SUMMARY -->
我找到的字體是教育部的標準字體--教育部宋體字形檔(Unicode碼)([教育部資料下載頁面](http://www.edu.tw/treasure/filedown.aspx?Node=1123&Index=2&WID=c5ad5187-55ef-4811-8219-e946fe04f725))，下載方式參考下圖

![螢幕擷圖存為 2014-01-16 17:37:49.png](http://user-image.logdown.io/user/6349/blog/6343/post/175873/XZ9PD84NQCKnLr1LuH3e_%E8%9E%A2%E5%B9%95%E6%93%B7%E5%9C%96%E5%AD%98%E7%82%BA%202014-01-16%2017:37:49.png)



##安裝方法

**<font color=red>注意!! 後來發現用教育部宋體字太細了，閱讀起來眼睛其實蠻不舒服的，最後還是為了保護眼睛妥協於droid了，如果各位有找到任何耐看的符合台灣標準的字體歡迎推薦給我!!!!</font>**

下載之後把檔案放在以下目錄

    ./fonts/
  
或是放到系統資料夾
  
    /usr/share/fonts/
  
兩者選一個就可以了，前者是使用者自己的，後者是整個系統的。不過後面還是要修改系統檔案，還是建議以系統為主。然後修改字體優先順序檔案。

    sudo vim /etc/fonts/conf.d/69-language-selector-zh-tw.conf

找到類似

```
          <edit name="family" mode="prepend" binding="strong">
            <string>AR PL New Sung</string>
            <string>AR PL UMing TW</string>
            <string>AR PL UMing HK</string>
            <string>HYSong</string>
```

這樣的東西，應該會有三個，然後將教育部宋體字型檔的英文名稱「MOESongUN Regular」放到第一個，然後將「AR PL New Sung」放到第二個， **三個** 都要做這樣的設定

之所以要把「AR PL New Sung」放到第二個是因為教育部的字體並沒有簡體中文，為了讓簡體文章不會看起來很詭異所以把類似的有簡體字的字體放在第二順位，才不會造成字體詭異的狀況(參考下圖)
![螢幕擷圖存為 2014-01-16 17:52:36.png](http://user-image.logdown.io/user/6349/blog/6343/post/175873/ikbaiuLSKGOUWA131LWm_%E8%9E%A2%E5%B9%95%E6%93%B7%E5%9C%96%E5%AD%98%E7%82%BA%202014-01-16%2017:52:36.png)

最後附上一張教育部宋體字形檔的圖片

![螢幕擷圖存為 2014-01-16 18:12:36.png](http://user-image.logdown.io/user/6349/blog/6343/post/175873/A54cYVeQWz1HhbTGGsga_%E8%9E%A2%E5%B9%95%E6%93%B7%E5%9C%96%E5%AD%98%E7%82%BA%202014-01-16%2018:12:36.png)
