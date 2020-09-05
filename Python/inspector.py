# -*- coding: UTF8 -*-

import re

def testme(testString):
    if len(testString) < 6:
        return False
    
    else:
        test1 = re.search('[a-zA-Z]',testString)
        if test1:
            test2 = re.search('[0-9]',testString)
            if test2:
                return True
            else:
                return False
        else:
            return False
