scenes = [12, 11, 1, 2, 3]
fair = False
bolt = True
badWords = False
puppeteer = False
cmdForAll = True
cmdForMe = True
halloweenScene = False
duck = True
forcedUI = 0

def saveSettings():
    import bs
    with open(bs.getEnvironment()['systemScriptsDirectory'] + "/settings.py") as file:
        s = [row for row in file]
        s[0] = 'scenes = '+str(scenes) + '\n'
        s[1] = 'fair = '+str(fair) + '\n'
        s[2] = 'bolt = '+str(bolt) + '\n'
        s[3] = 'badWords = '+str(badWords) + '\n'
        s[4] = 'puppeteer = '+str(puppeteer) + '\n'
        s[5] = 'cmdForAll = '+str(cmdForAll) + '\n'
        s[6] = 'cmdForMe = '+str(cmdForMe) + '\n'
        s[7] = 'halloweenScene = '+str(halloweenScene) + '\n'
        s[8] = 'duck = '+str(duck) + '\n'
        s[9] = 'forcedUI = '+str(forcedUI) + '\n'
        
    f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/settings.py",'w')
    for i in s:
        f.write(i)
    f.close()