# qrcode-storage

> ## 📖 OverView

Utilizzando questo semplice programma sei in grado di stivare i dati di un generico file all'interno di un qrcode creando uno snapshot da poter inserire su un nastro o da stampare e inserire in un luogo fisico e non avere quindi solo una copia online. 

Funziona trasformando i char in numeri ASCII e poi li trasforma in sequenze binarie. 

I qrcode generati saranno salvati nella cartella **/src** con il nome del file e con i numerini. 

Saranno anche caricati all'interno dell'file: **index.html** nella main directory. Li potrete stamparli come un nastro o visionarli sul cellure lanciando un web server con il comando 
	
	python3 -m http.server 8016
<br>

> ## 🔧 How do this func? 

Read this section to install the system and how to use. <br>

>> installation

clone the repository: 

	git clone https://github.com/rickycurci/qrcode-storage.git

move the the correct folder 

	cd qrcode-storage

install the dependecies (pyzbar, pillow): 
	
	pip3 install -r requirements.txt 

install zbar, the shared library (on MacOS):
	
	brew install zbar

(on Ubuntu/Debian): 
	
	sudo apt-get install zbar 
 

>> basic command 

To **encrypt** some file type this: 

	python3 qr-gen.py -e "patch file"


instead to **decrypt**: 

	python3 qr-gen.py -d "patch file"


