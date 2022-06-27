# qrcode-storage

> ## 📖 OverView

Utilizzando questo semplice programma sei in grado di stivare i dati di un generico file all'interno di un qrcode creando uno snapshot da poter inserire su un nastro o da stampare e inserire in un luogo fisico e non avere quindi solo una copia online. 

Funziona trasformando i char in numeri ASCII e poi li trasforma in sequenze binarie. 


> ## 🔧 How do this func? 

To **encrypt** some file type this: 

	
	python3 qr-gen.py -e "patch file"


instead to **decrypt**: 

	python3 qr-gen.py -d "patch file"


