from flask import Flask     # 載入 Flask
from flask import request   # 載入 Request 物件
# 建立 Application 物件，可設定靜態檔案的路徑處理
app=Flask(
     __name__,
     static_folder="static",     # 靜態檔案的資料夾名稱
     static_url_path="/abc"      # 靜態檔案對應的網址路徑
)
# 所有在 static 資料夾底下的檔案，都對應到網址路徑 / 檔案名稱

# 建立路徑 / 對應的處理函式
@app.route("/")
def index():    # 用來回應路徑 / 的處理函式
    #  print("請求方法",request.method)
    #  print("通訊協定",request.scheme)
    #  print("主機名稱",request.host)
    #  print("路徑",request.path)
    #  print("完整的網址", request.url)
    #  print("瀏覽器和作業系統",request.headers.get("user-agent"))
    #  print("語言偏好",request.headers.get("accept-language"))
    #  print("引薦網址",request.headers.get("referer"))

    # lang=request.headers.get("accept-language")
    # if lang.startswith("en"):
    #      return "hello flask"
    # else:
    #      return "你好"
    return "Hello Flask"   # 回應網站首頁的內容

# 建立路徑 /data 對應的處理函式
@app.route("/data")
def handleData():
     return "Hello data"

# 動態路由: 建立路徑 /user/使用者名稱
@app.route("/user/<username>")
def handleUser(username):
     if username=="嘉宏":
          return "你好"+username
     return "Hello "+username

# 建立路徑 /getSum 對應的處理函式
# 利用要求字串 (Querry String) 提供彈性 : /getSum?min=最小數字&max=最大數字
@app.route("/getSum")
def getSum():   # min+(min+1)+(min+2)+...max
     # 接收要求字串中的參數資料
     minNumber=request.args.get("min",0)
     minNumber=int(minNumber)
     maxNumber=request.args.get("max",100)
     maxNumber=int(maxNumber)
    #  print("最大數字",maxNumber)
     
     result=0
     for n in range(minNumber,maxNumber+1):
          result+=n
     return "結果"+str(result)
     

# 啟動網站伺服器，可透過 port 參數指定阜號
app.run(port=3000)