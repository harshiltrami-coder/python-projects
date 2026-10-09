'''
We are going to use python library like qrcode for conerting url to qrcode 
'''

import qrcode
url = input("Enter your url:- ")
filename = input("Enter the filename you want to save it as:- ")
if not(filename.endswith(".png")):
    filename = filename +".png"

image = qrcode.make(url)
image.save(filename)