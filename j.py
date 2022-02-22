from typing import ByteString
import websocket,json
from binance import *
from pair import *
socket=f'wss://stream.binance.com:9443/ws/btcusdt@kline_1m/ethusdt@kline_1m/avaxusdt@kline_1m'
#CREATING A LIST
list= [B('AVAXUSDT',0),B('BTCUSDT',0),B('ETHUSDT',0)]
Best=[pair('',0),pair('',0),pair('',0)]


def on_message(ws,message):
    json_message=json.loads(message)
    info=json_message['k']
    is_closed=info['x']
    volumeb=info['v']
    symbol=info['s']
    print('volume base: ',volumeb,"candle fechado: ",is_closed,"symbol: ",symbol)
    count=0
    print(Best[0].binanceid,':',Best[0].var,'',Best[1].binanceid,':',Best[1].var,'',Best[2].binanceid,':',Best[2].var)
    print(count)
    if(is_closed==True):
        count=count+1
        if(count==3):
            Best[0]=Best[1]=Best[2]=pair('',0)
    #SAVE DATA
    if(is_closed==True):
        for f in list:
            if(f.binanceid==symbol):
                f.volCandleNew=f.volCandle
                f.volCandleNew=volumeb
            

    
    






                




                
def on_close(ws):
    print("##CLOSED###")

ws= websocket.WebSocketApp(socket,on_message=on_message,on_close=on_close)
ws.run_forever()
   

        


