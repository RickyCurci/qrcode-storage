#!/usr/bin/python3

from pyzbar.pyzbar import decode
from PIL import Image
import qrcode
import sys
import os



def encoding(name): 
	os.system("mkdir src/"+name); f = name; f = open(f,"r"); string = ""	
	for i in f: 
		string = string+"\n"+i
	ASCII_values = []; values = []; value = []
	for character in string:
		ASCII_values.append(ord(character))
	for i in range(0,len(ASCII_values)):
		for j in range(0,8): 
			if ASCII_values[i]%2 != 0: 
				value.append("1")
				ASCII_values[i] = int(ASCII_values[i]/2)
			else:
				value.append("0")
				ASCII_values[i] = int(ASCII_values[i]/2)

		values.append(value[::-1]); value = []; 
	string = ""
	for i in values: 
		string += str("".join(i))
	print(string)
	
	if len(string) <= 2953:
		qr = qrcode.QRCode(

				version=40,
				error_correction=qrcode.constants.ERROR_CORRECT_L,
		)

		img = qr.make_image(qr.add_data(string))
		img.save(name+".jpg"); os.system("mv "+name+".jpg"+" src/"+name+"/")

		print("open > '"+name+".jpg'")

	elif len(string) > 2960: 



		nstring = string; point = 0
		print(len(nstring))
		for i in range(0,round(len(nstring)//2960)+1):
			qr = qrcode.QRCode(

					version=40,
					error_correction=qrcode.constants.ERROR_CORRECT_L,
			)
			img = qr.make_image(qr.add_data(nstring[point:(point+2960)])); point += 2960		
			img.save(name+str(i)+".jpg"); os.system("mv "+name+str(i)+".jpg"+" src/"+name+"/")
			print("open > '"+name+str(i)+".jpg'")


def decoe(name, n): 	
	string = "";

	for i in range(0,int(n)): 

		d = decode(Image.open(name+str(i)+".jpg")); 
		string += d[0].data.decode("ascii");  
	
	string = list(string); sub_string=[]; rstring = []
	for i in range(0,int(len(string)/8)): 
		for j in range(0,8): 
			sub_string.append(string[0]); string.remove(string[0]);
		rstring.append(int("".join(sub_string),2)); sub_string = []
	print(''.join(chr(i) for i in rstring))

def indexGen(name): 
	f = open("src/index.html","r"); old = f.read(); w = old
	patch = os.listdir("src/"+name+"/"); patch.remove(patch[0])
	for i in patch: 
		w = w+"\n"+'	<img src="'+i+'">'
	w = w+"\n</body>\n</html>"; f = open("src/"+name+"/index.html","w"); f.write(w)
	


if sys.argv[1] == "-e":
	encoding(sys.argv[2]); indexGen(sys.argv[2])
elif sys.argv[1] == "-d": 
	decoe(sys.argv[2], sys.argv[3])