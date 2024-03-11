
# ntucmlab_userform
研究發組表單系統
使用者輸入表單資料後可以自動生成excel檔以及pdf檔並存在本機
#

# Outline
- form :入口頁面，根據表單類型有不同分類 
- 手開單頁面 :使用者可以輸入資料並送出表單，產生excel以及pdf
- 表單列表 :在這裡會列出不同分類的所有表單

# form 頁面
![form_page](https://github.com/as2229181/ntucmlab_userform/assets/122463207/fb9cb760-6db4-4d69-b7e4-1bcf7656dcdc)
- 此頁面呈現六種不同的表單
  
-  <img src="https://github.com/as2229181/ntucmlab_userform/assets/122463207/4113331c-0d47-49d0-bb37-9191ccaad523" width="200px" heigh="150" >
- 點選鎖鏈可以進入輸入手開單頁面
  
- 點選表單名稱可以進入表單列表

# 手開單頁面 
![image](https://github.com/as2229181/ntucmlab_userform/assets/122463207/58334d45-4561-4b4d-a5d2-d305ead09787)

- 使用者在此頁面可以輸入所需資訊

- <img src="https://github.com/as2229181/ntucmlab_userform/assets/122463207/ef7cae53-dcf3-470c-b4b3-0db63716a8da" width="600px" heigh="450" >
  
  當編號輸入格式與當前不符合便會顯示錯誤

- ![未命名的影片_-_Made_with_Clipchamp_AdobeExpress](https://github.com/as2229181/ntucmlab_userform/assets/122463207/65d35ad1-0fc9-4471-8d7a-a4658a974136)

  輸入相對應價錢時頁面呈現的總價也會一起變動
  最後送出表單時會自動生成excel及pdf轉跳至表單列表頁面

# 表單列表
- <img src="https://github.com/as2229181/ntucmlab_userform/assets/122463207/b23b1e1e-6e86-4be0-9013-f103f13420ae" width="600px" heigh="450" >

  在此頁面呈現表單基本資訊紅色案你可以刪除表單，鉛筆按鈕可以更改繳費與否


# 2024/01 更新

- 表單輸入完後會在google 雲端表單新增資料
- 鉛筆按鈕可以改變雲端表單繳費狀態

# 使用技術
  - 前端

    - BOOTSTRAP
    - AJAX
    
  - 後端

    - Python
    - Django framework
    - Mysql

  - 工具

    - Git
    - memcached
      
# Database Schema
![image](https://github.com/as2229181/ntucmlab_userform/assets/122463207/1d0906db-1354-4cd9-9199-f96fc09ec63d)
# Future work
- 增加登入系統以及不同的授權等級
- 部屬至伺服器
- 使用docker開發

