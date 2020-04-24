import asyncio
import websockets
import json
import time
import os
from spider import Spider
# from ezblock import Taskmgr
from ezblock import getIP, TTS, Pin
from ezblock.modules import Ultrasonic
from vilib import Vilib
import Music as music

ip = getIP()
sp = Spider([10,11,12,4,5,6,1,2,3,7,8,9])
Vilib.camera_start()
# Vilib.human_detect_switch(True)
# Vilib.color_detect_switch(True)

class Websocket():
    recv_dict = {
        'SP':50,
        'RC':'null',
        'SS':['off',0,0.5], #喇叭播放音效
        'SM':['off',0,0.5], #喇叭播放音乐
        'TT':['off','you'],  #TTS
        'AC':['off', 1], # 动作
        'US':'off',  #超声波
        'OA':'off',  #避障开关
        'HT':'off', #人脸开关
        'HF':'off', #人脸跟踪
        'CT':'off', #颜色开关
        'CF':'off', #颜色跟踪
        'OF':['off',1,'up',0] , #校准
        'CC':'blue', #颜色选择
        
    }

    send_dict = {
        'TP':'PiCrawler',
        'US':20,
        'CC':'blue',
        'AD':'http://' + ip + ':8888/mjpg',
        'AS':[62, 0, -30]
        
    } 
    
    def __init__(self):
        self.gs_list = [0,0,0]
        self.sound_name = ['Weapon_Armor.wav', 'Emergency_Alarm.wav', 'Emergency_Truck_Honk.wav', 'Weapon_Continue_Shooting.wav', 'Weapon_Shell_Drop.wav']
        self.music_name = ["excitement.mp3", 'peace.mp3', 'power.mp3', 'spry.mp3']
        self.us = Ultrasonic(Pin('D0'), Pin('D1'))
        self.music_flag = True
        self.tts = TTS()
        self.current_music = -1
        
        
    async def recv_server_func(self, websocket):
        while 1:
            tmp = await websocket.recv()
            print(tmp)
            tmp = json.loads(tmp)
            
            for key in tmp:
                self.recv_dict[key] = tmp[key]
            print("recv_dict: %s"%self.recv_dict)
            self.remote_control(str(self.recv_dict['RC']), int(self.recv_dict['SP']))
            # print(recv_dict)
            Vilib.detect_color_name(str(self.recv_dict['CC']))
    
            
    def remote_control(self, move, speed):
        if move == 'forward':
            sp.do_action('forward', speed=speed)
        elif move == 'backward':
            sp.do_action('backward', speed=speed)
        elif move == 'left':
            sp.do_action('turn left', speed=speed)
        elif move == 'right':
            sp.do_action('turn right', speed=speed)
        
    

    async def send_server_func(self, websocket): 
        while 1:
            if self.recv_dict['US'] =='on':
                self.send_dict['US'] = self.us.read()
            self.send_dict['CC'] = Vilib.detect_obj_parameter['color_default'] 
            # print(self.send_dict)
            self.send_dict['AS'] = sp.current_coord[self.recv_dict['OF'][1] - 1]
            await websocket.send(json.dumps(self.send_dict))
            await asyncio.sleep(0.01)
    
    
        
    async def main_func(self):
        while 1:
        
            if self.recv_dict['OA'] == 'on':
                # print("ultrasonic on")
                distance = self.us.read()
                if distance > 40 or distance == -2:
                    sp.do_action('forward', speed=int(self.recv_dict['SP']))
                elif distance < 10:
                    sp.do_action('backward', speed=int(self.recv_dict['SP']))
                elif distance < 30:
                    sp.do_action('turn right', step=2, speed=int(self.recv_dict['SP']))
                    
            if self.recv_dict['AC'][0] == 'on':
                num = int(self.recv_dict['AC'][1])
                if num == 0:
                    sp.do_action("stand",speed=int(self.recv_dict['SP']))
                elif num == 1:
                    sp.do_action("sit",speed=int(self.recv_dict['SP']))
                elif num == 2:
                    sp.do_action("push up",speed=int(self.recv_dict['SP']))
                elif num == 3:
                    sp.do_action("wave",speed=int(self.recv_dict['SP']))
                elif num == 4:
                    sp.do_action("dance",speed=int(self.recv_dict['SP']))
                self.recv_dict['AC'][0] = 'off'
            
            if self.recv_dict['HT'] == 'on':
                Vilib.human_detect_switch(True)
            
            if self.recv_dict['HT'] == 'off':
                Vilib.human_detect_switch(False)
                
            if self.recv_dict['HF'] == 'on':
                Vilib.human_detect_switch(True)
                status = Vilib.human_detect_object('x')
                size = [Vilib.human_detect_object('width'), Vilib.human_detect_object('height')]
                # time.sleep(0.005)
                #on left -1 on right 1
                if status == -1:
                    sp.do_action('turn left', step=2, speed=int(self.recv_dict['SP']))
                elif status == 1:
                    sp.do_action('turn right', speed=int(self.recv_dict['SP']))
               
                if 0 < size[0] < 100 or 0 < size[1] < 100:
                    sp.do_action('forward', speed=int(self.recv_dict['SP']))
                
            
            if self.recv_dict['CT'] == 'on':
                Vilib.color_detect_switch(True)
            
            if self.recv_dict['CT'] == 'off':
                Vilib.color_detect_switch(False)
            
            if self.recv_dict['CF'] == 'on':
                Vilib.color_detect_switch(True)
                status = Vilib.color_detect_object('x')
                size = [Vilib.color_detect_object('width'), Vilib.color_detect_object('height')]
                # time.sleep(0.005)
                #on left -1 on right 1
                if status == -1:
                    sp.do_action('turn left', speed=int(self.recv_dict['SP']))
                elif status == 1:
                    sp.do_action('turn right', speed=int(self.recv_dict['SP']))
                
                if 0 < size[0] < 100 or 0 < size[1] < 100:
                    sp.do_action('forward', speed=int(self.recv_dict['SP']))
            
            if self.recv_dict['OF'][0] == 'on':
                sp.cali_helper(int(self.recv_dict['OF'][1]), self.recv_dict['OF'][2], int(self.recv_dict['OF'][3]))
                
            
            if self.recv_dict['SS'][0] == 'on':
                music.sound_effect_threading(self.sound_name[int(self.recv_dict['SS'][1])], float(self.recv_dict['SS'][2]))
                self.recv_dict['SS'][0] = 'off' 
            
            if self.recv_dict['SM'][0] == 'on':
                temp = int(self.recv_dict['SM'][1])
                if self.current_music != temp:
                    music.music_stop()
                    self.music_flag = True
                    self.current_music = temp
                if self.music_flag:
                    try:
                        music_file = self.music_name[self.current_music]
                        volume = float(self.recv_dict['SM'][2])
                        music.background_music(music_file, volume=volume) 
                    except IndexError:
                        print("no such music file: ", int(self.recv_dict['SM'][1]) + 1)
                    self.music_flag = False
                # self.recv_dict['SM'][0] = 'off' 
            elif self.recv_dict['SM'][0] == 'off':
                if self.music_flag == False:
                    music.music_stop()
                    self.music_flag = True
            
          
            if self.recv_dict['TT'][0] == 'on':
                self.tts.say(self.recv_dict['TT'][1]) 
                self.recv_dict['TT'][0] = 'off'  
            
        
            await asyncio.sleep(0.01)
            
   
    async def main_logic_1(self, websocket, path):
        while 1:
            await self.recv_server_func(websocket)

    async def main_logic_2(self, websocket, path):
        while 1:
            await self.send_server_func(websocket)
            
    def test(self):
        try:
            for _ in range(10):
                # ip = getIP()
                if ip:
                    print("IP Address: "+ ip)
                    # start_http_server()
                    break
                time.sleep(1)
            
            start_server_1 = websockets.serve(self.main_logic_1, ip, 8765)
            start_server_2 = websockets.serve(self.main_logic_2, ip, 8766)
            print('Start!')
            tasks = [self.main_func(),start_server_1,start_server_2]
            asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
            asyncio.get_event_loop().run_forever()
 
        finally:
            print("Finished")

if __name__ == "__main__":
    ws = Websocket()
    ws.test()


