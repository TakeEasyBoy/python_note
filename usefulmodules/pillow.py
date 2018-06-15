#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PIL import Image,ImageFilter,ImageDraw,ImageFont
# 读取文件 ,奇怪的路径配置,只能通过python_note去查找
im = Image.open('./python_note/usefulmodules/type_3.png')
print (im)
w, h = im.size
print (w,h)
# 缩放
im.thumbnail((w//2,h//2))
# 保存修改过后的图片
im.save('test.jpeg','jpeg')

# 滤镜效果
im1 = Image.open('test.jpeg')
# 模糊滤镜
im2 = im1.filter(ImageFilter.BLUR)
im2.save('blur.png','png')

# imgageDraw  绘图方法
import random
# 随机字母 a-z
def randChar():
    return chr(random.randint(65,90))  # # 产生 65 到 90 的一个整数型随机数 ,通过chr转换成对应的ascii字符
# 随机颜色
def randColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
# 随机颜色2
def randColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
width = 60 * 4
height = 60
image = Image.new('RGB',(width,height),(255,255,255))
# 创建一个font对象
font = ImageFont.truetype('/usr/share/fonts/truetype/abyssinica/AbyssinicaSIL-R.ttf',36)
# 创建draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=randColor2())
# 输出文字
for t in range(4):
    draw.text((60 * t + 10,10),randChar(),font=font,fill=randColor2())
# 滤镜
image = image.filter(ImageFilter.BLUR)
image.save('rand.png','png')
