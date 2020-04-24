# web-server- server process

Usage:
```python
ws = Websocket()
ws.test()
```
## Methods
- recv_server_func(websocket) - recv the data from client .
- remote_control(move) - recv key value to contrl spider move
- send_server_func(websocket) - send the data to the client.
- main_func() - the main logic api
- main_logic_1(websocket,path) - build a run forever recv api .

- main_logic_2(websocket,path) - build a run forever send api.

## 文件说明

- Music.py - 喇叭播放库文件

- spider.py - spider库文件

- robot.py - spider库文件

- vilib.py - 摄像头库文件

- web_server.py - websocket服务器库文件

- start_server.py  - 快捷启动websocket服务器和文件接收服务器文件

### 启动服务器命令: sudo python3 start_server.py