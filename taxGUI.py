import tkinter as tk
from tkinter.messagebox import *

class TaxRate(object):
	"""docstring for TaxRate"""
	def __init__(self, master):
		self.old_tax_point=3500
		self.new_tax_point=5000
		self.master = master
		self.create_widget()

	def create_widget(self):
		self.master.title('Tax Calculate')
		self.btax = tk.Text(self.master, height='1', width=30)
		self.insur = tk.Text(self.master, height='1', width=30)
		self.btax_label = tk.Label(self.master, text='税前收入:')
		self.insur_label = tk.Label(self.master, text='五险一金:')
		self.btax_label.grid(row=0, column=0)
		self.btax.grid(row=0, column=1)
		self.insur_label.grid(row=1, column=0)
		self.insur.grid(row=1, column=1)

		self.button_ok = tk.Button(self.master, text='Calculate')
		self.button_quit = tk.Button(self.master, text='QUIT', fg='red', command=self.master.destroy)

		# do not mix pack and grid in same master window
		self.button_ok.grid(row=3, column=1)
		self.button_quit.grid(row=4, column=1)

		self.button_ok.bind('<Button-1>', self.Calculate)

	def Calculate(self, event):
		btax = float(self.btax.get('0.0', 'end'))
		insurance = float(self.insur.get('0.0', 'end'))
		self.old_taxable_num = self.old_tax_rate(btax, insurance)
		self.old_atax = btax - insurance - self.old_taxable_num
		self.new_taxable_num = self.new_tax_rate(btax, insurance)
		self.new_atax = btax - insurance - self.new_taxable_num
		showinfo(message='税前收入：%.2f元。\n五险一金：%.2f元。\n旧税率应纳税：%.2f元，税后收入：%.2f元。\n新税率应纳税：%.2f元，税后收入：%.2f元。'%(btax, insurance, self.old_taxable_num, self.old_atax, self.new_taxable_num, self.new_atax))

	def old_tax_rate(self, btax, insurance):
		self.old_taxable_income = btax-insurance-self.old_tax_point
		if self.old_taxable_income >0 and self.old_taxable_income <= 1500:
			self.old_taxable_num = self.old_taxable_income*0.03 - 0
		elif self.old_taxable_income >1500 and self.old_taxable_income <=4500:
			self.old_taxable_num = self.old_taxable_income*0.1 - 105
		elif self.old_taxable_income >4500 and self.old_taxable_income <=9000:
			self.old_taxable_num = self.old_taxable_income*0.2 - 555
		elif self.old_taxable_income >9000 and self.old_taxable_income <=35000:
			self.old_taxable_num = self.old_taxable_income*0.25 - 1005
		elif self.old_taxable_income >35000 and self.old_taxable_income <=55000:
			self.old_taxable_num = self.old_taxable_income*0.3 - 2755
		elif self.old_taxable_income >55000 and self.old_taxable_income <=80000:
			self.old_taxable_num = self.old_taxable_income*0.35 - 5505
		elif self.old_taxable_income >80000:
			self.old_taxable_num = self.old_taxable_income*0.4 - 13505
		else:
			self.old_taxable_num = 0
		return self.old_taxable_num

	def new_tax_rate(self, btax, insurance):
		self.new_taxable_income = btax - insurance- self.new_tax_point
		if self.new_taxable_income >0 and self.new_taxable_income <= 3000:
			self.new_taxable_num = self.new_taxable_income*0.03 - 0
		elif self.new_taxable_income >3000 and self.new_taxable_income <=12000:
			self.old_taxable_num = self.old_taxable_income*0.1 - 210
		elif self.new_taxable_income >12000 and self.new_taxable_income <=25000:
			self.old_taxable_num = self.old_taxable_income*0.2 - 1410
		elif self.new_taxable_income >25000 and self.new_taxable_income <=35000:
			self.old_taxable_num = self.old_taxable_income*0.25 - 2660
		elif self.new_taxable_income >35000 and self.new_taxable_income <=55000:
			self.old_taxable_num = self.old_taxable_income*0.3 - 4410
		elif self.new_taxable_income >55000 and self.new_taxable_income <=80000:
			self.old_taxable_num = self.old_taxable_income*0.35 - 7160
		elif self.new_taxable_income >80000:
			self.old_taxable_num = self.old_taxable_income*0.45 - 15160
		else:
			self.new_taxable_num = 0
		return self.new_taxable_num

def main():
	root = tk.Tk()
	tr = TaxRate(root)
	root.mainloop()

if __name__ == '__main__':
	main()