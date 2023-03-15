# -*- coding:utf-8 -*-
'''!
  @file  output_square.py
  @brief  Use DAC to output square wave.
  @copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license  The MIT License (MIT)
  @author  [tangjie](jie.tang@dfrobot.com)
  @version  V1.0
  @date  2022-03-07
  @url  https://github.com/DFRobot/DFRobot_GP8403
'''
from __future__ import print_function
import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from DFRobot_GP8403 import *

DAC = DFRobot_GP8403(0x58)  
status = DAC.begin()
if(status != 0):
  while True:time.sleep(1)
  
print("init succeed")
#Set output range  
DAC.set_DAC_outrange(OUTPUT_RANGE_5V)
while True:
  '''!
      @brief Output square wave from channel 0
      @param amp Set square wave amplitude Vp
      @param freq Set square wave frequency f
      @param offset Set square wave DC offset Voffset
      @param dutyCycle Set square wave duty cycle
      @param channel Channel select
    '''
  DAC.output_square(2500, 10, 2500, 50, 0)
  
  
