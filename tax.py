class TaxRate(object):
	"""docstring for TaxRate"""
	def __init__(self, before_tax, insurance):
		super(TaxRate, self).__init__()
		self.btax = before_tax
		self.atax = None
		self.insur = insurance
		self.Taxable_income = None

	def oldRate(self, tax_point):
		self.Taxable_income = self.btax - self.insur - tax_point
		if self.Taxable_income >0 and self.Taxable_income <= 1500:
			self.Taxable_num = self.Taxable_income*0.03 - 0
		elif self.Taxable_income >1500 and self.Taxable_income <=4500:
			self.Taxable_num = self.Taxable_income*0.1 - 105
		elif self.Taxable_income >4500 and self.Taxable_income <=9000:
			self.Taxable_num = self.Taxable_income*0.2 - 555
		elif self.Taxable_income >9000 and self.Taxable_income <=35000:
			self.Taxable_num = self.Taxable_income*0.25 - 1005
		elif self.Taxable_income >35000 and self.Taxable_income <=55000:
			self.Taxable_num = self.Taxable_income*0.3 - 2755
		elif self.Taxable_income >55000 and self.Taxable_income <=80000:
			self.Taxable_num = self.Taxable_income*0.35 - 5505
		elif self.Taxable_income >80000:
			self.Taxable_num = self.Taxable_income*0.4 - 13505
		else:
			self.Taxable_num = 0
		self.atax = self.btax-self.insur-self.Taxable_num
		print('旧税率应纳税：%.2f元，税后收入：%.2f元'%(self.Taxable_num, self.atax))

	def newRate(self, tax_point):
		rent = 1500
		self.Taxable_income = self.btax - self.insur - tax_point
		if self.Taxable_income < 1500:
			self.Taxable_num = 0
			if self.Taxable_income >= 0:
				special_deduct = self.Taxable_income
			else:
				special_deduct = 0
		elif self.Taxable_income >= 1500:
			special_deduct = 1500
			if self.Taxable_income <= 3000:
				ratio = 0.03
				remain = 0
			elif self.Taxable_income > 3000 and self.Taxable_income <= 12000:
				ratio = 0.1
				remain = 210
			elif self.Taxable_income >12000 and self.Taxable_income <=25000:
				ratio = 0.2
				remain = 1410
			elif self.Taxable_income >25000 and self.Taxable_income <=35000:
				ratio = 0.25
				remain = 2660
			elif self.Taxable_income >35000 and self.Taxable_income <=55000:
				ratio = 0.3
				remain = 4410
			elif self.Taxable_income >55000 and self.Taxable_income <=80000:
				ratio = 0.35
				remain = 7160
			elif self.Taxable_income >80000:
				ratio = 0.45
				remain = 15160
			else:
				ratio = 0
				remain = 0
			self.Taxable_num = (self.Taxable_income-rent)*ratio - remain
		self.atax = self.btax - self.insur - self.Taxable_num
		print('专项扣除总值：%.2f元，专项扣除实际值：%.2f元，新税率应纳税：%.2f元，税后收入：%.2f元'%(rent, special_deduct, self.Taxable_num, self.atax))


def main():
	before_tax = float(input('Input before tax income: '))
	insurance = float(input('Input insurance: '))
	print('税前收入：',before_tax)
	print('五险一金：',insurance)
	t = TaxRate(before_tax, insurance)
	t.oldRate(3500)
	t.newRate(5000)

if __name__ == '__main__':
	main()