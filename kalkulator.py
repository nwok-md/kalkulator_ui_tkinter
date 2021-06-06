from tkinter import *
from functools import partial

class kalkulator(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.ikon()
		self.bhpl = False
	def ikon(self):
		self.config(bg='black')
		self.lbl = Label(self, text='Kalkulator',font=('metrics, 27'),fg='lime',bg='black')
		self.lbl.grid(columnspan=3, pady=10)
		
		self.layar = Entry(self, width=15,fg='lime', bg='black',font=('metricts',20))
		self.layar.grid(columnspan=3, row=1)
		
		a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '+', 'C', '/', '*', '=' ]
		klm = 0
		brs = 2
		for kon in a:
			perintah = partial(self.hasil, kon)
			if kon == '=':
				Button(self, text='=', command=perintah,width=14,font=('families', 20),fg='lime',bg='black').grid(columnspan=3, row=brs,pady=5)
			else:
				Button(self, text=kon, command=perintah,width=3,font=('families', 20),fg='lime',bg='black').grid(column=klm,row=brs, pady=20, padx=15)
			klm += 1
			if klm > 2:
				klm = 0
				brs += 1
						
	def hasil(self, key):
		if key == '=':
			self.bhpl = True
			try:
				hasilnya = eval(self.layar.get())
				self.layar.delete(0, END)
				self.layar.insert(END, hasilnya)
			except:
				self.layar.insert(END, 'ERROR')
		elif key == 'C':
			self.layar.delete(0, END)
		else:
				if self.bhpl:
					self.layar.delete(0, END)
					self.bhpl = False
				
				self.layar.insert(END, key)
	
							
			
call = kalkulator()
call.mainloop()
