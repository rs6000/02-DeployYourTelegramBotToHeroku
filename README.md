# Deploy Your TelegramBot to Heroku (with Django)
本篇內容是將Telegram ChatBot 佈署到 [Heroku](http://www.heroku.com)網站上，所以需要有[Heroku](http://www.heroku.com) 的帳號，沒有的請註冊一個(Free)  
程式完全沒有更動，所以直接用上一篇完成的範例程式。

### 快速懶人包:
直接使用本篇的範例程式:
```
$ git clone https://github.com/rs6000/02-DeployYourTelegramBotToHeroku
$ cd mysite
$ pip install -r requirements.txt
```
填入TelegramBot的token:
```
# mysite/myapp/views.py
bot=telebot.TeleBot('請輸入你的token!!!')
```
這個範例基本上都已經把需要的檔案都準備好了，但還是解說一下  
這次把ChatBot佈署到Heroku有新增或修改那些檔案。
- 新增 Procfile
- 新增 runtime.txt
- 修改 mysite/wsgi.py
- 修改 mysite/setting.py
- 修改 .gitignore

### 佈署到Heroku
> 請先準備好以下的東西
> > -   Git
> > -   申請 Heroku 帳號 & 安裝 Heroku CLI
以下操作流程都是在終端機介面下(命令提示字元)

    $ heroku login
    $ heroku create 專案名稱
    $ git init
    $ heroku git:remote -a 專案名稱
    $ heroku config:set DISABLE_COLLECTSTATIC=1
    $ git add .
    $ git commit -m "add your commit"
    $ git push heroku master
    $ heroku run python manage.py migrate (可省略此步驟)
    $ heroku run python manage.py createsuperuser (可省略此步驟)
    $ heroku ps:scale web=1

### 設定 Webhook

    格式:
    https://api.telegram.org/bot{$token}/setWebhook?url=https://專案名稱.herokuapp.com/api/telegram
    
    把上面的{token}換成自己申請的token
    專案名稱就是在heroku建立的專案，替換好後，貼到瀏覽器上

### 打開Telegram測試
![圖片1](https://smilehsu.cc/wp-content/uploads/2020/05/c7a7dc02ff6507856d29a2847f092200.png)
 
### Telegram ChatBot 後台管理
這個Bot是架在Django上面，所以是有內建後台管理的  

    網址格式:
    https://專案名稱.herokuapp.com/admin/
預設的帳號密碼都是 admin
![圖片2](https://smilehsu.cc/wp-content/uploads/2020/05/dc5199fb7d63c4dd0ffc5f9113f8f60a.png)
這個後台管理，目前只有一個功能，會記錄User的ID，所有跟Bot對話的User都會記錄在後台的MYAPP/Users 裡面

### 最後
後來我才理解網路上有關Telegram ChatBot為什麼大多是用單檔或Flask框架，因為這樣最簡單。用Django就要修改一些檔案跟url的設定。  

剩下的就自己需要什麼就加上去吧 :)

---
### Reference:

-   [heroku-deploy-django-telegrambot-webhook](https://www.youtube.com/watch?v=bWDKUl1OgJk)  作者來自烏茲別克(跟上一篇一樣)
- [Telegram Bot 上傳到 Heroku，如何操作呢？看這篇你一定懂！](https://shareboxnow.com/telegram-python-4/) (Flask)
