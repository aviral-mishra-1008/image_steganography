import numpy as np
from PIL import Image

def Encode(src_path, message, dest_path):

    #Opening the image and counting pixels while also checking the mode
    img = Image.open(src_path, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))
    n = 3

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    message += "$$82"
    

    #Converting message to binary
    temp = []

    for i in message:
      temp.append(format(ord(i), "08b"))

    b_message = ''.join(temp)
    req_pixels = len(b_message)

    #encoding the data
    if req_pixels > total_pixels:
      print("ERROR: Larger Image Needed!!")

    else:
      index=0
      for p in range(total_pixels):
          for q in range(0, n):
              if index < req_pixels:
                  array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                  index += 1
        
    #Saving the encoding
    array=array.reshape(height, width, n)
    enc_img = Image.fromarray(array.astype('uint8'), img.mode)
    enc_img.save(dest_path)
