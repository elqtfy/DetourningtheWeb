from PIL import Image, ImageFilter, ImageDraw, ImageFont

baby = Image.open('baby.jpg')
print baby.size
print baby.format

#resize
baby.thumbnail((150,150)) #auto keep ratio
#if you use resize, it will distort a bit.
#baby = baby.resize((150,150)) it needs create one object cuz it is copying the imgae

baby.save('baby_thumb.jpg')

baby = baby.filter(ImageFilter.BLUR)
baby.save('blurred_baby.png')

canvas = ImageDraw.Draw(baby)
canvas.rectang([20,20,300,300], fill = (255,0,0))
#canvas.save('redbaby.jpg')

font = ImageFont.truetype('/Library/Fonts/BrushScriptStd.otf',60)
canvas.text((10,10),"A spector is haunting this baby", font=font, fill=(255,255,255))

baby.save('redbaby.jpg')
