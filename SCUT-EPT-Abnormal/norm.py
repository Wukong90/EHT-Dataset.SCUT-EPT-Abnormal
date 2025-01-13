from PIL import Image

image_path = './img.jpg'
save_path = './img_norm.jpg'
image = Image.open(image_path).convert('L')
if ((image.height > 96) and (image.width > 1440)):
   image = image.resize(
   (1440, 96), resample=Image.BILINEAR)
   image.save(save_path)
else:
   new_image = Image.new('L',(1440,96),255)
   location_width = (1440 - image.width)/2
   location_height = (96 - image.height)/2
   new_image.paste(image,(int(location_width),int(location_height)))
   new_image.save(save_path)