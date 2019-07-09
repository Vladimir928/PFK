#!/usr/bin/env python3
################################################################################
#   modules.py
#
#   chapter 7: Modules
#
#   09.07.2019  Created by:  vo958
################################################################################

import time
print(time.time())
print(time.ctime())

import time as t
print(t.ctime())

from time import *
print(ctime())

from time import sleep
print('before sleep')
sleep(3)
print('after sleep')

