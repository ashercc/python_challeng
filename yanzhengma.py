# -*- coding:utf-8 -*-
from PIL import Image,ImageFont,ImageDraw,ImageFilter
from random import randint
def getColor():
    return (randint(100,255),randint(100,255),randint(100,255))
def getChar():
    return chr(randint(65,90))
def getCharColor():
    return (randint(0,100),randint(0,100),randint(0,100))
def createC():
    im = Image.new("RGB",(200,70),(255,255,255))
    draw = ImageDraw.Draw(im)
    font1 = ImageFont.truetype("Monaco",30)
    width,height = im.size
    for x in range(width):
        for y in range(height):
            im.putpixel((x,y),getColor())       #使图片背影杂乱一些
    for t in range(5):
        draw.text((10+40*t,20),getChar(),fill=getCharColor(),font=font1)
        draw.line([randint(0,200),randint(0,70),randint(0,200),randint(0,70)],fill=getColor(),width=2)
    im = im.filter(ImageFilter.BLUR)
    im.save("yanzhengma.jpg","JPEG")
    im.show()
if __name__=="__main__":
    createC()