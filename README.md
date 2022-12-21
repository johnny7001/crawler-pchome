# 爬取 pchome商品 
##  觀察json api <br>
* https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=switch&page=2&sort=sale/dc  
網頁的操作方式是往下滑可以載入新資料, 不過觀察到透過修改page就可以抓到新的頁面了, 所以這邊不選擇用selenium  
    * q=要搜尋的商品名稱
    * page=頁碼
    * sortOrder= (dc:降冪, ac=升冪) 
    * sortParm= (sale=有貨優先, rnk=精準度,prc=價格) 
    * min=2000&max=5000 (價格範圍2000~5000)  

    修改需要的欄位後可以做成DataFrame並且篩選, 也可以直接insert 資料庫  
    json檔有直接給商品的總頁數, 藉由修改裡面的參數來查詢不同的商品  

* https://24h.pchome.com.tw/prod/DGBJCW-A900EOBBG  
prod後面加上商品的id, 可以進到商品頁面  

* 整理成json檔格格式
```json
{
    "Results": [
        {
            "Id": "DGBJDE-A900BQBJ4",
            "image": "https://cs-a.ecimg.tw/items/DGBJDEA900BQBJ4/000001_1644992544.jpg",
            "name": "任天堂 NS Switch 紅藍主機 電力加強版 台灣公司貨+熱門遊戲+贈周邊",
            "describe": "任天堂 NS Switch 紅藍主機 電力加強版 台灣公司貨+熱門遊戲+贈周邊\\r\\npchome 2022強檔特惠｜紅藍主機x自選多人同樂必備片 加碼贈送9h鋼化膜!! \r\n\r\n1.switch 紅藍主機\r\n■ 電力加強版 可遊玩時間加長!!!\r\n■ switch & play 遊戲生活變得更加互動\r\n■ 改變形態多種遊戲模式：tv模式、桌上模式、手提模式\r\n■ 最多連線8台主機，進行對戰或協力遊戲\r\n■ joy-con內置「hd震動」體驗逼真細膩臨場感\r\n■ ⚡台灣公司貨 原廠一年保固⚡\r\n\r\n2.熱門遊戲片自選一\r\n👉超級轟炸超人r\r\n👉樂高世界\r\n👉超級雞馬 鄰居版\r\n👉當個創世神\r\n👉樂高漫威超級英雄2\r\n\r\n※遊戲片皆為國際版封面 支援中文，內容與代理版完全相同唷!\r\n\r\n\r\n3.限時加碼贈超值好禮\r\n■ oivo主機鋼化玻璃貼\r\n■ 隨機特典x1\r\n\r\n\r\n❕主機商品為特殊3c產品，請開箱檢查時【全程錄影】，若無全程開箱檢測影片我方有權不接受退換貨。\r\n❕商品一經拆封、開機或還原，便無法退貨，若有商品有問題請洽原廠展碁。",
            "price": 8350,
            "url": "https://24h.pchome.com.tw/prod/DGBJDE-A900BQBJ4"
        },
        {
            "Id": "DGBJDE-1900DF5EI",
            "image": "https://cs-a.ecimg.tw/items/DGBJDE1900DF5EI/000001_1642148990.jpg",
            "name": "Switch 電力加強版-灰黑主機",
            "describe": "Switch 電力加強版-灰黑主機\\r\\nswitch灰黑電力加強版主機\r\n台灣公司貨主機\r\n主機本體保固一年\r\n支援繁體中文介面",
            "price": 7680,
            "url": "https://24h.pchome.com.tw/prod/DGBJDE-1900DF5EI"
        },
```