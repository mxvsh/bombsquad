# -*- coding: utf-8 -*-
import bs
import bsInternal
import bsPowerup
import bsUtils
import random
import getPermissionsHashes as gph


class chatOptions(object):
    def __init__(self):
        self.all = True # just in case
       
        
        self.tint = None # needs for /nv
        
    def checkDevice(self,nick): # check host (settings.cmdForMe)
        client_str = []
        for client in bsInternal._getGameRoster():
            if client['players'] != []:
                if client['players'][0]['name'] == nick.encode('utf-8'):
                    client_str = client['displayString']
                    clientID = client['clientID']
        if client_str in gph.adminHashes:
            bsInternal._chatMessage("Sir, Yes Sir!")
            return True
        elif client_str in gph.assholes:
            bsInternal._chatMessage("The Commands are not for you assholes.")
            bsInternal._disconnectClient(int(client['displayString']))
            return False
        elif client_str in gph.chutiya:
            bsInternal._chatMessage("Tum jaise chutiyo ke liye commands nahi hai.")
            bsInternal._disconnectClient(int(client['displayString']))
            return False
        elif client_str in gph.co:
            bsInternal._chatMessage("Ohk, Done.")
            return True
        elif client_str in gph.elder:
            bsInternal._chatMessage("You can't use commands yet.")
            return False
        elif client_str in gph.member:
            bsInternal._chatMessage("You are just a newcomer.")
            return False
        elif client_str not in [gph.chutiya, gph.assholes, gph.co, gph.adminHashes, gph.member, gph.elder]:
            bsInternal._chatMessage("only admin can use chat commands")
            bsInternal._disconnectClient(int(client['displayString']))
            return False
        else:
            bs.screenMessage("only admin can use chat commands",color =(2,0,0),clients=clientID)
            bsInternal._disconnectClient(int(client['displayString']))
            return False
    
        
    def kickByNick(self,nick):
        roster = bsInternal._getGameRoster()
        for i in roster:
            try:
                if i['players'][0]['nameFull'].lower().find(nick.encode('utf-8').lower()) != -1:
                    bsInternal._disconnectClient(int(i['clientID']))
            except:
                pass
        
    def opt(self,nick,msg):
        if self.checkDevice(nick):
            m = msg.split(' ')[0] # command
            a = msg.split(' ')[1:] # arguments
            
            activity = bsInternal._getForegroundHostActivity()
            with bs.Context(activity):
                if m == '/kick':
                    if a == []:
                        bsInternal._chatMessage('Using: /kick name or number of list')
                    else:
                        if len(a[0]) > 3:
                            self.kickByNick(a[0])
                        else:
                            try:
                                s = int(a[0])
                                bsInternal._disconnectClient(int(a[0]))
                            except:
                                self.kickByNick(a[0])
                elif m == '/admin':
                    clID = int(a[0])
                    for client in bsInternal._getGameRoster():
                        if client['clientID']==clID:
                            if a[1] == 'add':
                                newadmin = client['displayString']
                                updated_admins = gph.co.append(newadmin)
                            elif a[1] == 'remove':
                                newadmin = client['displayString']
                                if newadmin in gph.co:
                                    updated_admins = gph.co.remove(newadmin)

                    
                    with open(bs.getEnvironment()['systemScriptsDirectory'] + "/getPermissionsHashes.py") as file:
                        s = [row for row in file]
                        s[0] = 'vipHashes = []'+'\n'
                        s[1] = 'co = '+ updated_admins + '\n'
                        f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/getPermissionsHashes.py",'w')
                        for i in s:
                            f.write(i)
                        f.close()
                elif m == '/chu':
                    clID = int(a[0])
                    for client in bsInternal._getGameRoster():
                        if client['clientID']==clID:
                            if a[1] == 'add':
                                chutiya = client['displayString']
                                updated_chutiya = gph.chutiya.append(chutiya)
                            elif a[1] == 'remove':
                                chutiya = client['displayString']
                                if chutiya in gph.chutiya:
                                    updated_chutiya = gph.chutiya.remove(chutiya)

                    
                    with open(bs.getEnvironment()['systemScriptsDirectory'] + "/getPermissionsHashes.py") as file:
                        s = [row for row in file]
                        s[0] = 'vipHashes = []'+'\n'
                        s[1] = 'co = []'+'\n'
                        s[2] = 'assholes = []'+'\n'
                        s[3] = 'chutiya = '+ updated_chutiya + '\n'
                        f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/getPermissionsHashes.py",'w')
                        for i in s:
                            f.write(i)
                        f.close()
                elif m == '/ass':
                    clID = int(a[0])
                    for client in bsInternal._getGameRoster():
                        if client['clientID']==clID:
                            if a[1] == 'add':
                                ass = client['displayString']
                                updated_ass = gph.assholes.append(ass)
                            elif a[1] == 'remove':
                                ass = client['displayString']
                                if ass in gph.assholes:
                                    updated_ass = gph.assholes.remove(ass)

                    
                    with open(bs.getEnvironment()['systemScriptsDirectory'] + "/getPermissionsHashes.py") as file:
                        s = [row for row in file]
                        s[0] = 'vipHashes = []'+'\n'
                        s[1] = 'co = []'+'\n'
                        s[2] = 'assholes = '+ updated_admins + '\n'
                        f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/getPermissionsHashes.py",'w')
                        for i in s:
                            f.write(i)
                        f.close()
                elif m == '/vip':
                    clID = int(a[0])
                    for client in bsInternal._getGameRoster():
                        if client['clientID']==clID:
                            if a[1] == 'add':
                                vip = client['displayString']
                                updated_vip = gph.vip.append(vip)
                            elif a[1] == 'remove':
                                vip = client['displayString']
                                if vip in gph.vip:
                                    updated_vip = gph.vip.remove(vip)

                    
                    with open(bs.getEnvironment()['systemScriptsDirectory'] + "/getPermissionsHashes.py") as file:
                        s = [row for row in file]
                        s[0] = 'vip = '+ updated_admins + '\n'
                        f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/getPermissionsHashes.py",'w')
                        for i in s:
                            f.write(i)
                        f.close()
    
                elif m == '/list':
                    bsInternal._chatMessage("======== FOR /kick ONLY: ========")
                    for i in bsInternal._getGameRoster():
                        try:
                            bsInternal._chatMessage(i['players'][0]['nameFull'] + "     (/kick " + str(i['clientID'])+")")
                        except:
                            pass
                    bsInternal._chatMessage("==================================")
                    bsInternal._chatMessage("======= For other commands: =======")
                    for s in bsInternal._getForegroundHostSession().players:
                        bsInternal._chatMessage(s.getName() + "     "+ str(bsInternal._getForegroundHostSession().players.index(s)))
                elif m == '/ooh':
                    if a is not None and len(a) > 0:
                        s = int(a[0])
                        def oohRecurce(c):
                            bs.playSound(bs.getSound('ooh'),volume = 2)
                            c -= 1
                            if c > 0:
                                bs.gameTimer(int(a[1]) if len(a) > 1 and a[1] is not None else 1000,bs.Call(oohRecurce,c=c))
                        oohRecurce(c=s)
                    else:
                        bs.playSound(bs.getSound('ooh'),volume = 2)
                elif m == '/playSound':
                    if a is not None and len(a) > 1:
                        s = int(a[1])
                        def oohRecurce(c):
                            bs.playSound(bs.getSound(str(a[0])),volume = 2)
                            c -= 1
                            if c > 0:
                                bs.gameTimer(int(a[2]) if len(a) > 2 and a[2] is not None else 1000,bs.Call(oohRecurce,c=c))
                        oohRecurce(c=s)
                    else:
                        bs.playSound(bs.getSound(str(a[0])),volume = 2)
                elif m == '/quit':
                    bsInternal.quit()
                elif m == '/nv':
                    if self.tint is None:
                        self.tint = bs.getSharedObject('globals').tint
                    bs.getSharedObject('globals').tint = (0.5,0.7,1) if a == [] or not a[0] == u'off' else self.tint
                elif m == '/freeze':
                    if a == []:
                        bsInternal._chatMessage('Using: /freeze all or number of list')
                    else:
                        if a[0] == 'all':
                            for i in bs.getSession().players:
                                try:
                                    i.actor.node.handleMessage(bs.FreezeMessage())
                                except:
                                    pass
                        else:
                            bs.getSession().players[int(a[0])].actor.node.handleMessage(bs.FreezeMessage())
                elif m == '/thaw':
                    if a == []:
                        bsInternal._chatMessage('Using: /thaw all or number of list')
                    else:
                        if a[0] == 'all':
                            for i in bs.getSession().players:
                                try:
                                    i.actor.node.handleMessage(bs.ThawMessage())
                                except:
                                    pass
                        else:
                            bs.getSession().players[int(a[0])].actor.node.handleMessage(bs.ThawMessage())
		elif m == '/sleep':
                    if a == []:
                        bsInternal._chatMessage('Using: number of list')
                    else:
                        if a[0] == 'all':
                            for i in bs.getSession().players:
                                try:
                                    i.actor.node.handleMessage("knockout",5000)
                                except:
                                    pass
			else:
                            bs.getSession().players[int(a[0])].actor.node.handleMessage("knockout",5000)

                elif m == '/kill':
                    if a == []:
                        bsInternal._chatMessage('Using: /kill all or number of list')
                    else:
                        if a[0] == 'all':
                            for i in bs.getSession().players:
                                try:
                                    i.actor.node.handleMessage(bs.DieMessage())
                                except:
                                    pass
                        else:
                            bs.getSession().players[int(a[0])].actor.node.handleMessage(bs.DieMessage())
                elif m == '/curse':
                    if a == []:
                        bsInternal._chatMessage('Using: /curse all or number of list')
                    else:
                        if a[0] == 'all':
                            for i in bs.getSession().players:
                                try:
                                    i.actor.curse()
                                except:
                                    pass
                        else:
                            bs.getSession().players[int(a[0])].actor.curse()
                elif m == '/box':
                    if a == []:
                        bsInternal._chatMessage('Using: /box all or number of list')
                    else:
                        try:
                            if a[0] == 'all':
                                for i in bs.getSession().players:
                                    try:
                                        i.actor.node.torsoModel = bs.getModel("tnt")
                                    except:
                                        print 'error'
                                for i in bs.getSession().players:
                                    try:
                                        i.actor.node.colorMaskTexture= bs.getTexture("tnt")
                                    except:
                                        print 'error'
                                for i in bs.getSession().players:
                                    try:
                                        i.actor.node.colorTexture= bs.getTexture("tnt")
                                    except:
                                        print 'error'
                                for i in bs.getSession().players:
                                    try:
                                        i.actor.node.highlight = (1,1,1)
                                    except:
                                        print 'error'
                                for i in bs.getSession().players:
                                    try:
                                        i.actor.node.color = (1,1,1)
                                    except:
                                        print 'error'
                                for i in bs.getSession().players:
                                    try:
                                        i.actor.node.headModel = None
                                    except:
                                        print 'error'
                                for i in bs.getSession().players:
                                    try:
                                        i.actor.node.style = "cyborg"
                                    except:
                                        print 'error'
                            else:
                                n = int(a[0])
                                bs.getSession().players[n].actor.node.torsoModel = bs.getModel("tnt"); 
                                bs.getSession().players[n].actor.node.colorMaskTexture= bs.getTexture("tnt"); 
                                bs.getSession().players[n].actor.node.colorTexture= bs.getTexture("tnt") 
                                bs.getSession().players[n].actor.node.highlight = (1,1,1); 
                                bs.getSession().players[n].actor.node.color = (1,1,1); 
                                bs.getSession().players[n].actor.node.headModel = None; 
                                bs.getSession().players[n].actor.node.style = "cyborg";
                        except:
                           bs.screenMessage('Ошибка!',color = (1,0,0))
		elif m == '/tex':
                    if a == []:
                        bsInternal._chatMessage('Using: /tex all or number of list')
                    else:
                        try:
                            if a[0] == 'all':
				for i in bs.getSession().players:
                                    try:
                                        i.actor.node.colorMaskTexture= bs.getTexture("egg1")
                                    except:
                                        print 'error'
                                for i in bs.getSession().players:
                                    try:
                                        i.actor.node.colorTexture= bs.getTexture("egg1")
                                    except:
                                        print 'error'
                            else:
                                n = int(a[0])
                                bs.getSession().players[n].actor.node.colorMaskTexture= bs.getTexture("egg1"); 
                                bs.getSession().players[n].actor.node.colorTexture= bs.getTexture("egg1") 
                        except:
                           bs.screenMessage('Ошибка!',color = (1,0,0))

                elif m == '/remove':
                    if a == []:
                        bsInternal._chatMessage('Using: /remove all or number of list')
                    else:
                        if a[0] == 'all':
                            for i in bs.getSession().players:
                                try:
                                    i.removeFromGame()
                                except:
                                    pass
                        else:
                            bs.getSession().players[int(a[0])].removeFromGame()
                elif m == '/end':
                    try:
                        bsInternal._getForegroundHostActivity().endGame()
                    except:
                        pass
                elif m == '/hug':
                    if a == []:
                        bsInternal._chatMessage('Using: /hug all or number of list')
                    else:
                        try:
                            if a[0] == 'all':
                                try:
                                    bsInternal._getForegroundHostActivity().players[0].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[1].actor.node
                                except:
                                    pass
                                try:
                                    bsInternal._getForegroundHostActivity().players[1].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[0].actor.node
                                except:
                                    pass
                                try:
                                    bsInternal._getForegroundHostActivity().players[3].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[2].actor.node
                                except:
                                    pass
                                try:
                                    bsInternal._getForegroundHostActivity().players[4].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[3].actor.node
                                except:
                                    pass
                                try:
                                    bsInternal._getForegroundHostActivity().players[5].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[6].actor.node
                                except:
                                    pass
                                try:
                                    bsInternal._getForegroundHostActivity().players[6].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[7].actor.node
                                except:
                                    pass
                            else:
                                bsInternal._getForegroundHostActivity().players[int(a[0])].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[int(a[1])].actor.node
                        except:
                           bs.screenMessage('Ошибка!',color = (1,0,0))
                elif m == '/gm':
                    if a == []:
                        for i in range(len(activity.players)):
                            if activity.players[i].getName().encode('utf-8').find(nick.encode('utf-8').replace('...','').replace(':','')) != -1:
                                activity.players[i].actor.node.hockey = activity.players[i].actor.node.hockey == False
                                activity.players[i].actor.node.invincible = activity.players[i].actor.node.invincible == False
                                activity.players[i].actor._punchPowerScale = 5 if activity.players[i].actor._punchPowerScale == 1.2 else 1.2
                    else:
                        activity.players[int(a[0])].actor.node.hockey = activity.players[int(a[0])].actor.node.hockey == False
                        activity.players[int(a[0])].actor.node.invincible = activity.players[int(a[0])].actor.node.invincible == False
                        activity.players[int(a[0])].actor._punchPowerScale = 5 if activity.players[int(a[0])].actor._punchPowerScale == 1.2 else 1.2
                elif m == '/tint':
                    if a == []:
                        bsInternal._chatMessage('Using: /tint R G B')
                        bsInternal._chatMessage('OR')
                        bsInternal._chatMessage('Using: /tint r bright speed')
                    else:
                        if a[0] == 'r':
                            m = 1.3 if a[1] is None else float(a[1])
                            s = 1000 if a[2] is None else float(a[2])
                            bsUtils.animateArray(bs.getSharedObject('globals'), 'tint',3, {0: (1*m,0,0), s: (0,1*m,0),s*2:(0,0,1*m),s*3:(1*m,0,0)},True)
                        else:
                            try:
                                if a[1] is not None:
                                    bs.getSharedObject('globals').tint = (float(a[0]),float(a[1]),float(a[2]))
                                else:
                                    bs.screenMessage('Error!',color = (1,0,0))
                            except:
                                bs.screenMessage('Error!',color = (1,0,0))
                elif m == '/pause':
                    bs.getSharedObject('globals').paused = bs.getSharedObject('globals').paused == False
                elif m == '/sm':
                    bs.getSharedObject('globals').slowMotion = bs.getSharedObject('globals').slowMotion == False
                elif m == '/bunny':
                    if a == []:
                        bsInternal._chatMessage('Using: /bunny count owner(number of list)')
                    import BuddyBunny
                    for i in range(int(a[0])):
                        p=bs.getSession().players[int(a[1])]
                        if not 'bunnies' in p.gameData:
                            p.gameData['bunnies'] = BuddyBunny.BunnyBotSet(p)
                        p.gameData['bunnies'].doBunny()
                elif m == '/cameraMode':
                    try:
                        if bs.getSharedObject('globals').cameraMode == 'follow':
                            bs.getSharedObject('globals').cameraMode = 'rotate'
                        else:
                            bs.getSharedObject('globals').cameraMode = 'follow'
                    except:
                        pass
                elif m == '/lm':
                    arr = []
                    for i in range(100):
                        try:
                            arr.append(bsInternal._getChatMessages()[-1-i])
                        except:
                            pass
                    arr.reverse()
                    for i in arr:
                        bsInternal._chatMessage(i)
                elif m == '/gp':
                    if a == []:
                        bsInternal._chatMessage('Using: /gp number of list')
                    else:
                        s = bsInternal._getForegroundHostSession()
                        for i in s.players[int(a[0])].getInputDevice()._getPlayerProfiles():
                            try:
                                bsInternal._chatMessage(i)
                            except:
                                pass
                elif m == '/icy':
                    bsInternal._getForegroundHostActivity().players[int(a[0])].actor.node = bsInternal._getForegroundHostActivity().players[int(a[1])].actor.node
                elif m == '/fly':
                    if a == []:
                        bsInternal._chatMessage('Using: /fly all or number of list')
                    else:
                        if a[0] == 'all':
                            for i in bsInternal._getForegroundHostActivity().players:
                                i.actor.node.fly = True
                        else:
                            bsInternal._getForegroundHostActivity().players[int(a[0])].actor.node.fly = bsInternal._getForegroundHostActivity().players[int(a[0])].actor.node.fly == False
                elif m == '/floorReflection':
                    bs.getSharedObject('globals').floorReflection = bs.getSharedObject('globals').floorReflection == False
                elif m == '/ac':
                    if a == []:
                        bsInternal._chatMessage('Using: /ac R G B')
                        bsInternal._chatMessage('OR')
                        bsInternal._chatMessage('Using: /ac r bright speed')
                    else:
                        if a[0] == 'r':
                            m = 1.3 if a[1] is None else float(a[1])
                            s = 1000 if a[2] is None else float(a[2])
                            bsUtils.animateArray(bs.getSharedObject('globals'), 'ambientColor',3, {0: (1*m,0,0), s: (0,1*m,0),s*2:(0,0,1*m),s*3:(1*m,0,0)},True)
                        else:
                            try:
                                if a[1] is not None:
                                    bs.getSharedObject('globals').ambientColor = (float(a[0]),float(a[1]),float(a[2]))
                                else:
                                    bs.screenMessage('Error!',color = (1,0,0))
                            except:
                                bs.screenMessage('Error!',color = (1,0,0))
                elif m == '/iceOff':
                    try:
                        activity.getMap().node.materials = [bs.getSharedObject('footingMaterial')]
                        activity.getMap().isHockey = False
                    except:
                        pass
                    try:
                        activity.getMap().floor.materials = [bs.getSharedObject('footingMaterial')]
                        activity.getMap().isHockey = False
                    except:
                        pass
                    for i in activity.players:
                        i.actor.node.hockey = False
                elif m == '/maxPlayers':
                    if a == []:
                        bsInternal._chatMessage('Using: /maxPlayers count of players')
                    else:
                        try:
                            bsInternal._getForegroundHostSession()._maxPlayers = int(a[0])
                            bsInternal._setPublicPartyMaxSize(int(a[0]))
                            bsInternal._chatMessage('Players limit set to '+str(int(a[0])))
                        except:
                            bs.screenMessage('Error!',color = (1,0,0))
                elif m == '/heal':
                    if a == []:
                        bsInternal._chatMessage('Using: /heal all or number of list')
                    else:
                        try:
                            bsInternal._getForegroundHostActivity().players[int(a[0])].actor.node.handleMessage(bs.PowerupMessage(powerupType = 'health'))
                        except:
                            bs.screenMessage('Error!',color = (1,0,0))
                elif m == '/reflections':
                    if a == [] or len(a) < 2:
                        bsInternal._chatMessage('Using: /reflections type(1/0) scale')
                    rs = [int(a[1])]
                    type = 'soft' if int(a[0]) == 0 else 'powerup'
                    try:
                        bsInternal._getForegroundHostActivity().getMap().node.reflection = type
                        bsInternal._getForegroundHostActivity().getMap().node.reflectionScale = rs
                    except:
                        pass
                    try:
                        bsInternal._getForegroundHostActivity().getMap().bg.reflection = type
                        bsInternal._getForegroundHostActivity().getMap().bg.reflectionScale = rs
                    except:
                        pass
                    try:
                        bsInternal._getForegroundHostActivity().getMap().floor.reflection = type
                        bsInternal._getForegroundHostActivity().getMap().floor.reflectionScale = rs
                    except:
                        pass
                    try:
                        bsInternal._getForegroundHostActivity().getMap().center.reflection = type
                        bsInternal._getForegroundHostActivity().getMap().center.reflectionScale = rs
                    except:
                        pass
                elif m == '/shatter':
                    if a == []:
                        bsInternal._chatMessage('Using: /shatter all or number of list')
                    else:
                        if a[0] == 'all':
                            for i in bsInternal._getForegroundHostActivity().players:
                                i.actor.node.shattered = int(a[1])
                        else:
                            bsInternal._getForegroundHostActivity().players[int(a[0])].actor.node.shattered = int(a[1])
                elif m == '/cm':
                    if a == []:
                        time = 8000
                    else:
                        time = int(a[0])
                        
                        op = 0.08
                        std = bs.getSharedObject('globals').vignetteOuter
                        bsUtils.animateArray(bs.getSharedObject('globals'),'vignetteOuter',3,{0:bs.getSharedObject('globals').vignetteOuter,17000:(0,1,0)})
                        
                    try:
                        bsInternal._getForegroundHostActivity().getMap().node.opacity = op
                    except:
                        pass
                    try:
                        bsInternal._getForegroundHostActivity().getMap().bg.opacity = op
                    except:
                        pass
                    try:
                        bsInternal._getForegroundHostActivity().getMap().bg.node.opacity = op
                    except:
                        pass
                    try:
                        bsInternal._getForegroundHostActivity().getMap().node1.opacity = op
                    except:
                        pass
                    try:
                        bsInternal._getForegroundHostActivity().getMap().node2.opacity = op
                    except:
                        pass
                    try:
                        bsInternal._getForegroundHostActivity().getMap().node3.opacity = op
                    except:
                        pass
                    try:
                        bsInternal._getForegroundHostActivity().getMap().steps.opacity = op
                    except:
                        pass
                    try:
                        bsInternal._getForegroundHostActivity().getMap().floor.opacity = op
                    except:
                        pass
                    try:
                        bsInternal._getForegroundHostActivity().getMap().center.opacity = op
                    except:
                        pass
                        
                    def off():
                        op = 1
                        try:
                            bsInternal._getForegroundHostActivity().getMap().node.opacity = op
                        except:
                            pass
                        try:
                            bsInternal._getForegroundHostActivity().getMap().bg.opacity = op
                        except:
                            pass
                        try:
                            bsInternal._getForegroundHostActivity().getMap().bg.node.opacity = op
                        except:
                            pass
                        try:
                            bsInternal._getForegroundHostActivity().getMap().node1.opacity = op
                        except:
                            pass
                        try:
                            bsInternal._getForegroundHostActivity().getMap().node2.opacity = op
                        except:
                            pass
                        try:
                            bsInternal._getForegroundHostActivity().getMap().node3.opacity = op
                        except:
                            pass
                        try:
                            bsInternal._getForegroundHostActivity().getMap().steps.opacity = op
                        except:
                            pass
                        try:
                            bsInternal._getForegroundHostActivity().getMap().floor.opacity = op
                        except:
                            pass
                        try:
                            bsInternal._getForegroundHostActivity().getMap().center.opacity = op
                        except:
                            pass
                        bsUtils.animateArray(bs.getSharedObject('globals'),'vignetteOuter',3,{0:bs.getSharedObject('globals').vignetteOuter,100:std})
                    bs.gameTimer(time,bs.Call(off))
                        
                elif m == '/help':
                    bsInternal._chatMessage(bs.Lstr(resource='help1').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help2').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help3').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help4').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help5').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help6').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help7').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help8').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help9').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help10').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help11').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help12').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help13').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help14').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help15').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help16').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help17').evaluate())
                    bsInternal._chatMessage("Please DONT USE \'/pasue\' because it makes the server crash")
                    bsInternal._chatMessage(bs.Lstr(resource='help18').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help19').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help20').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help21').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help22').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help23').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help24').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help25').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help26').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help27').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help28').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help29').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help30').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help31').evaluate())
                    bsInternal._chatMessage(bs.Lstr(resource='help32').evaluate())
                    bsInternal._chatMessage("/admin-use with number from the kick list to add/remove player\'s id in co-leader tag.")
                    bsInternal._chatMessage("/ass-use with number from the kick list to add/remove player\'s id in asshole tag.")
                    bsInternal._chatMessage("/chu-use with number from the kick list to add/remove player\'s id in chutiya tag.")

            
c = chatOptions()

def cmd(msg):
    if bsInternal._getForegroundHostActivity() is not None:
        n = msg.split(': ')
        c.opt(n[0],n[1])
bs.realTimer(5000,bs.Call(bsInternal._setPartyIconAlwaysVisible,True))
