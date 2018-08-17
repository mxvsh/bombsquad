# -*- coding: utf-8 -*-

import bs
import random

class goWriteWords(object):
    def __init__(self):
        self.words = ["TEAMING ARE BANNED!", "ТИМИНГ\игра командой запрещены!", "Нарушаения правил караются баном.", "Violations of the rules are punishable by ban.",'Не путайте админа Паша с фейком! Фейк не [ADMIN] и без иконки!',"Если увидите фейк админа, пишите /dump это поможет забанить нарушителя!","admin Паша without crown icon and [ADMIN] is fake!"]
        self.delay = 20000
        self.printWord(self.words)
        self._writer = bs.Timer(self.delay,bs.WeakCall(self.printWord,self.words),repeat = True)
        
    def printWord(self,array):
        bs.screenMessage(random.choice(array))
        
    def stop(self):
        self._writer = None
        