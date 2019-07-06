import logging
import socket
import sys
import time
import pigpio

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

class CarManager(object):
  
  def __init__(self, servo=4):
        self.response = None
        self.pi = pigpio.pi()
        self.servo = servo


  def send_command(self, command):
      logger.info({'action': 'send_command', 'command': command})
      if command=='forward':
        pwm = 500
      elif command=='back':
        pwm = 1450
      elif command=='right':
        pwm = 1450
      elif command=='left':
        pwm = 1450
      self.pi.set_servo_plusewidth(self.servo, pwm)
      time.sleep(3)

      return self.response

  def forward(self):
      return self.send_command('forward')

  def back(self):
      return self.send_command('back')

  def left(self):
      return self.send_command('left')

  def right(self):
      return self.send_command('right')
