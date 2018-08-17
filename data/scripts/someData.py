lastDataUpdate = 16
haveUpdate = False
lastMessage = None

def saveData():
    import bs
    with open(bs.getEnvironment()['systemScriptsDirectory'] + "/someData.py") as file:
        s = [row for row in file]
        s[0] = 'lastDataUpdate = '+str(lastDataUpdate) + '\n'
        s[1] = 'haveUpdate = '+str(haveUpdate) + '\n'
        
    f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/someData.py",'w')
    for i in s:
        f.write(i)
    f.close()