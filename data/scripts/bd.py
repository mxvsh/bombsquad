import bs
import bsUtils
import math

#########################################################################################################################


class serverCloses(object):
    """
        Beautifully close the server, with the warning players.
        
        serverCloses(timer = 10)
    """
    def __init__(self,timer = 10):
        if bs.getActivity() is not None:
            try:
                def showZoomMessage():
                    bs.getActivity().showZoomMessage("Server closes!!!")
                showZoomMessage()
                if timer*1000 > 3000: bs.gameTimer(3000,bs.Call(showZoomMessage))
            except Exception: pass
        a = bs.newNode('globals')
        bsUtils.animateArray(a,'tint',3,{0:bs.getSharedObject('globals').tint,(timer)*1000:(0.0,0.0,0.0)})
        def flash():
            bsUtils.animateArray(a,'tint',3,{0:bs.getSharedObject('globals').tint,999:(7.0,7.0,7.0)})
        bs.gameTimer(1400+timer*1000,bs.Call(flash))
        bs.screenMessage("The server will close after "+ str(timer) +" seconds!")
        print "The server will close after "+ str(timer) +" seconds!"
        def printTimer(time):
            bs.screenMessage(str(time))
            print time
            if time == -1:
                bs.quit()
        for i in range(timer+2):
            bs.gameTimer(((timer+2)-i)*1000,bs.Call(printTimer,i-1))
                
#########################################################################################################################
           
class effect(object):
    def __init__(self,position = (0,0.1,0),r = 2):
        self.s = 0
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.maxR = r
        self.r = r
        self.revers = False
        self.repeat = True

            
        def spawnParticles():
            sin = math.sin(self.s)*self.r
            cos = math.cos(self.s)*self.r
            self.s += 0.1
            
            if self.r < 0:
                self.revers = True
            elif self.r > self.maxR:
                self.revers = False
             
            if not self.revers:
                self.r -= 0.003
                self.y += 0.008
            else:
                self.r += 0.003
                self.y -= 0.008
                
            bs.emitBGDynamics(position=(self.x + cos, self.y, self.z + sin),count=5,scale=1,spread=0,chunkType='spark')
            
            
            
        bs.gameTimer(1,bs.Call(spawnParticles),repeat = True if self.repeat else False)
        
    def __del__(self):
        print "Effect deleted!"
        self.repeat = False



































































































