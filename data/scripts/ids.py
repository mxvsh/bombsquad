ids = []
ver = 16000

def saveIds():
    import bs
    with open(bs.getEnvironment()['systemScriptsDirectory'] + "/ids.py") as file:
        s = [row for row in file]
        s[0] = 'ids = '+str(ids) + '\n'
        s[1] = 'ver = '+str(ver) + '\n'
    f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/ids.py",'w')
    for i in s:
        f.write(i)
    f.close()