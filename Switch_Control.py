import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

import sys, tty, termios, signal

######################
## Motor Establishment
######################

FmotorL = 0
FmotorR = 1
BmotorL = 2
BmotorR = 3

FmotorR_forward = 2000
FmotorR_backward = 1000
FmotorL_forward = 1000
FmotorL_backward = 2000
BmotorR_forward = 2000
BmotorR_backward = 1000
BmotorL_forward = 1000
BmotorL_backward = 2000

try:
  RPL.pinMode(FmotorL,RPL.SERVO)
  RPL.servoWrite(FmotorL,1500)
  RPL.pinMode(FmotorR,RPL.SERVO)
  RPL.servoWrite(FmotorR,1500)
  RPL.pinMode(BmotorL,RPL.SERVO)
  RPL.servoWrite(BmotorL,1500)
  RPL.pinMode(BmotorR,RPL.SERVO)
  RPL.servoWrite(BmotorR,1500)
except:
  pass

######################
## Individual commands
######################
def stopAll():
  try:
    RPL.servoWrite(FmotorL,1500)
    RPL.servoWrite(FmotorR,1500)
    RPL.servoWrite(BmotorL,1500)
    RPL.servoWrite(BmotorR,1500)
  except:
    print "error except"
    pass

def Fforward():
  RPL.servoWrite(FmotorL,FmotorL_forward)
  RPL.servoWrite(FmotorR,FmotorR_forward)

def Bforward():
  RPL.servoWrite(BmotorL,BmotorL_forward)
  RPL.servoWrite(BmotorR,BmotorR_forward)

def Freverse():
  RPL.servoWrite(FmotorL,FmotorL_backward)
  RPL.servoWrite(FmotorR,FmotorR_backward)

def Breverse():
  RPL.servoWrite(BmotorL,BmotorL_backward)
  RPL.servoWrite(BmotorR,BmotorR_backward)

def Fright():
  RPL.servoWrite(FmotorL,1460)#motorL_forward)
  RPL.servoWrite(FmotorR,1460)#motorR_backward)

def Bright():
  RPL.servoWrite(BmotorL,1460)#motorL_forward)
  RPL.servoWrite(BmotorR,1460)#motorR_backward)

def Fleft():
  RPL.servoWrite(FmotorL,1540)#motorL_backward)
  RPL.servoWrite(FmotorR,1540)#motorR_forward)

def Bleft():
  RPL.servoWrite(BmotorL,1540)#motorL_backward)
  RPL.servoWrite(BmotorR,1540)#motorR_forward)

def Fforward_right():
  RPL.servoWrite(FmotorL,FmotorL_forward)
  RPL.servoWrite(FmotorR,1500)

def Bforward_right():
  RPL.servoWrite(BmotorL,BmotorL_forward)
  RPL.servoWrite(BmotorR,1500)

def Fforward_left():
  RPL.servoWrite(FmotorL,1500)
  RPL.servoWrite(FmotorR,FmotorR_forward)

def Bforward_left():
  RPL.servoWrite(BmotorL,1500)
  RPL.servoWrite(BmotorR,BmotorR_forward)

def Fbackward_right():
  RPL.servoWrite(FmotorL,1500)
  RPL.servoWrite(FmotorR,FmotorR_backward)

def Bbackward_right():
  RPL.servoWrite(BmotorL,1500)
  RPL.servoWrite(BmotorR,BmotorR_backward)

def Fbackward_left():
  RPL.servoWrite(FmotorL,FmotorL_backward)
  RPL.servoWrite(FmotorR,1500)

def Bbackward_left():
  RPL.servoWrite(BmotorL,BmotorL_backward)
  RPL.servoWrite(BmotorR,1500)

def Fprint_speed():
  print 'Front--FORWARD: Left Motor: ', FmotorL_forward, ' Front--Right Motor: ', FmotorR_forward, '\r'
  print 'Front--BACKWARD: Left Motor: ', FmotorR_backward, ' Front--Right Motor: ', FmotorL_backward, '\r'

def Bprint_speed():
  print 'Back--FORWARD: Left Motor: ', BmotorL_forward, ' Back--Right Motor: ', BmotorR_forward, '\r'
  print 'Back--BACKWARD: Left Motor: ', BmotorR_backward, ' Back--Right Motor: ', BmotorL_backward, '\r'

def FforwardSpeedChanges(change, mn = 1600, mx = 2900):
  global FmotorR_forward
  global FmotorL_forward
  FmotorR_forward += change
  FmotorL_forward += change
  FmotorR_forward = max(min(FmotorR_forward, mx), mn)
  FmotorL_forward = max(min(FmotorL_forward, mx), mn)
  print_speed()

def BforwardSpeedChanges(change, mn = 1600, mx = 2900):
  global BmotorR_forward
  global BmotorL_forward
  BmotorR_forward += change
  BmotorL_forward += change
  BmotorR_forward = max(min(BmotorR_forward, mx), mn)
  BmotorL_forward = max(min(BmotorL_forward, mx), mn)
  print_speed()

def FbackwardSpeedChanges(change, mn = 100, mx = 1400):
  global FmotorR_backward
  global FmotorL_backward
  FmotorR_backward += change
  FmotorL_backward += change
  FmotorR_backward = max(min(FmotorR_backward, mx), mn)
  FmotorL_backward = max(min(FmotorL_backward, mx), mn)
  print_speed()

def BbackwardSpeedChanges(change, mn = 100, mx = 1400):
  global BmotorR_backward
  global BmotorL_backward
  BmotorR_backward += change
  BmotorL_backward += change
  BmotorR_backward = max(min(BmotorR_backward, mx), mn)
  BmotorL_backward = max(min(BmotorL_backward, mx), mn)
  print_speed()

def FbackwardRightSpeedChange(change, mn = 100, mx = 1400):
  global FmotorR_backward
  FmotorR_backward += change
  FmotorR_backward = max(min(FmotorR_backward, mx), mn)
  print_speed()

def BbackwardRightSpeedChange(change, mn = 100, mx = 1400):
  global BmotorR_backward
  BmotorR_backward += change
  BmotorR_backward = max(min(BmotorR_backward, mx), mn)
  print_speed()

def FbackwardLeftSpeedChange(change, mn = 100, mx = 1400):
  global FmotorL_backward
  FmotorL_backward += change
  FmotorL_backward = max(min(FmotorL_backward, mx), mn)
  print_speed()

def backwardLeftSpeedChange(change, mn = 100, mx = 1400):
  global BmotorL_backward
  BmotorL_backward += change
  BmotorL_backward = max(min(BmotorL_backward, mx), mn)
  print_speed()

def FforwardRightSpeedChange(change, mn = 1600, mx = 2900):
  global FmotorR_forward
  FmotorR_forward += change
  FmotorR_forward = max(min(FmotorR_forward, mx), mn)
  print_speed()

def BforwardRightSpeedChange(change, mn = 1600, mx = 2900):
  global BmotorR_forward
  BmotorR_forward += change
  BmotorR_forward = max(min(BmotorR_forward, mx), mn)
  print_speed()

def FforwardLeftSpeedChange(change, mn = 1600, mx = 2900):
  global FmotorL_forward
  FmotorL_forward += change
  FmotorL_forward = max(min(FmotorL_forward, mx), mn)
  print_speed()

def BforwardLeftSpeedChange(change, mn = 1600, mx = 2900):
  global BmotorL_forward
  BmotorL_forward += change
  BmotorL_forward = max(min(BmotorL_forward, mx), mn)
  print_speed()

fd = sys.stdin.fileno() # I don't know what this does
old_settings = termios.tcgetattr(fd) # this records the existing console settings that are later changed with the tty.setraw... line so that they can be replaced when the loop ends

######################################
## Other motor commands should go here
######################################

def interrupted(signum, frame): # this is the method called at the end of the alarm
  stopAll()

signal.signal(signal.SIGALRM, interrupted) # this calls the 'interrupted' method when the alarm goes off
tty.setraw(sys.stdin.fileno()) # this sets the style of the input

print "Ready To Drive! Press * to quit.\r"
## the SHORT_TIMEOUT needs to be greater than the press delay on your keyboard
## on your computer, set the delay to 250 ms with `xset r rate 250 20`
SHORT_TIMEOUT = 0.255 # number of seconds your want for timeout
while True:
  signal.setitimer(signal.ITIMER_REAL,SHORT_TIMEOUT) # this sets the alarm
  ch = sys.stdin.read(1) # this reads one character of input without requiring an enter keypress
  signal.setitimer(signal.ITIMER_REAL,0) # this turns off the alarm
  if ch == '*': # pressing the asterisk key kills the process
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) # this resets the console settings
    break # this ends the loop
  else:
    if ch == 'w':
      Fforward()
      Bforward()
    elif ch == "a":
      Fleft()
      Bleft()
    elif ch == "s":
      Freverse()
      Breverse()
    elif ch == "d":
      Fright()
      Bright()
    elif ch == "e":
      Fforward_right()
      Bforward_right()
    elif ch == "q":
      Fforward_left()
      Bforward_left()
    elif ch == "z":
      Fbackward_left()
      Bbackward_left()
    elif ch == "c":
      Fbackward_right()
      Bbackward_right()
    elif ch == "]":
      FforwardSpeedChanges(100)
      BforwardSpeedChanges(100)
    elif ch == "[":
      FbackwardSpeedChanges(-100)
      BbackwardSpeedChanges(-100)
    elif ch == "}":
      FforwardSpeedChanges(-100)
      BforwardSpeedChanges(-100)
    elif ch == "{":
      FbackwardSpeedChanges(100)
      BbackwardSpeedChanges(100)
    elif ch == "1":
      FforwardLeftSpeedChange(100)
      BforwardLeftSpeedChange(100)
    elif ch == "!":
      FforwardLeftSpeedChange(-100)
      BforwardLeftSpeedChange(-100)
    elif ch == "2":
      FforwardRightSpeedChange(100)
      BforwardRightSpeedChange(100)
    elif ch == "@":
      FforwardRightSpeedChange(-100)
      BforwardRightSpeedChange(-100)
    elif ch == "3":
      FbackwardLeftSpeedChange(-100)
      BbackwardLeftSpeedChange(-100)
    elif ch == "#":
      FbackwardLeftSpeedChange(100)
      BbackwardLeftSpeedChange(100)
    elif ch == "4":
      FbackwardRightSpeedChange(-100)
      BbackwardRightSpeedChange(-100)
    elif ch == "$":
      FbackwardRightSpeedChange(100)
      BbackwardRightSpeedChange(100)
    else:
      stopAll()
