import threading
class B(threading.Thread):
  def __init__(self, binanceid,v):
    super(B, self).__init__()
    self.binanceid = binanceid
    self.volCandle=v
    self.volCandleNew=0
  
  def calcular(self):
    return ((self.volCandleNew-self.volCandle)/self.volCandle)*100
  
 
    



    
    

    