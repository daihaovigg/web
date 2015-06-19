#!/usr/bin/env python
#-*-coding:utf-8-*-

from PIL import Image,ImageFilter,ImageDraw,ImageFont
import random
#验证码

class mycaptcha(object):
  def __init__(self):
    self.code=''
# 240 x 60:
    self.width = 60 * 4
    self.height = 60
    self.image = Image.new('RGB', (self.width, self.height), (255, 255, 255))
# 创建Font对象:
    self.font = ImageFont.truetype('/usr/share/fonts/dejavu/DejaVuSans.ttf',36)
# 创建Draw对象:
    self.draw = ImageDraw.Draw(self.image)
    self.fillcode()



# 随机字母:
  def rndChar(self):
    return chr(random.randint(65, 90))

# 随机颜色1:
  def rndColor(self):
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
  def rndColor2(self):
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


  def fillcode(self):
# 填充每个像素:
    for x in range(self.width):
      for y in range(self.height):
        self.draw.point((x, y), fill=self.rndColor())
# 输出文字:
    for t in range(4):
      rndchar=self.rndChar()
      self.code=self.code+rndchar
      self.draw.text((60 * t + 10, 10), rndchar, font=self.font, fill=self.rndColor2())
  def save(self):
    self.image.save('static/code.jpg', 'jpeg')

  def reload(self):
    return self.__init__()
# 模糊:
#image = image.filter(ImageFilter.BLUR)
#image.save('code.jpg', 'jpeg');
