import tkinter as tk
from tkinter.messagebox import *
import numpy


class SwitchOrPs(object):
	"""docstring for SwitchOrPs"""
	def __init__(self, root):
		super(SwitchOrPs, self).__init__()
		self.root = root
		self.indexes_name = self.__dict__
		self.create_weight()

	def create_weight(self):
		self.root.title('SwitchOrPs')
		self.battle1 = tk.Entry(self.root)
		self.battle2 = tk.Entry(self.root)
		self.vs = tk.Label(self.root, text="VS")
		self.battle1.grid(row=0, column=1)
		self.battle2.grid(row=0, column=3)
		self.vs.grid(row=0, column=2)

		self.index_name = tk.Label(self.root, text="指标名")
		self.value1_label = tk.Label(self.root, text="值")
		self.value2_label = tk.Label(self.root, text="值")
		self.weight_label = tk.Label(self.root, text="权重")
		self.index_name.grid(row=1, column=0)
		self.value1_label.grid(row=1, column=1)
		self.value2_label.grid(row=1, column=3)
		self.weight_label.grid(row=1, column=4)

		# 默认指标
		self.idx_name1 = tk.Entry(self.root)
		self.idx_name1.insert(0, "主机价格")

		self.idx_value11 = tk.Entry(self.root)
		self.idx_value21 = tk.Entry(self.root)
		self.weight1 = tk.Entry(self.root)

		self.idx_name2 = tk.Entry(self.root)
		self.idx_name2.insert(0, "配件价格")

		self.idx_value12 = tk.Entry(self.root)
		self.idx_value22 = tk.Entry(self.root)
		self.weight2 = tk.Entry(self.root)
		
		self.idx_name3 = tk.Entry(self.root)
		self.idx_name3.insert(0, "游戏价格")

		self.idx_value13 = tk.Entry(self.root)
		self.idx_value23 = tk.Entry(self.root)
		self.weight3 = tk.Entry(self.root)


		self.hint_label = tk.Label(self.root, text="以下是自定义指标")

		self.idx_name1.grid(row=2, column=0)
		self.idx_name2.grid(row=3, column=0)
		self.idx_name3.grid(row=4, column=0)
		self.idx_value11.grid(row=2, column=1)
		self.idx_value21.grid(row=2, column=3)
		self.weight1.grid(row=2, column=4)

		self.idx_value12.grid(row=3, column=1)
		self.idx_value22.grid(row=3, column=3)
		self.weight2.grid(row=3, column=4)

		self.idx_value13.grid(row=4, column=1)
		self.idx_value23.grid(row=4, column=3)
		self.weight3.grid(row=4, column=4)

		self.hint_label.grid(row=5, column=0, columnspan=5)

		# 使用destroy()动态调整按钮位置


		# pack(), grid() or place() functions of Entry object return none
		# get() will return an error otherwise
		# split it on to two lines 


		for i in range(5, 12):
			self.indexes_name["idx_name"+str(i)] = tk.Entry(self.root)
			self.indexes_name["idx_value1"+str(i)] = tk.Entry(self.root)
			self.indexes_name["idx_value2" + str(i)] = tk.Entry(self.root)
			self.indexes_name["weight" + str(i)] = tk.Entry(self.root)

			self.indexes_name["idx_name" + str(i)].grid(row=i+1, column=0)
			self.indexes_name["idx_value1" + str(i)].grid(row=i+1, column=1)
			self.indexes_name['idx_value2' + str(i)].grid(row=i+1, column=3)
			self.indexes_name["weight" + str(i)].grid(row=i+1, column=4)

		self.button_ok = tk.Button(self.root, text='Caculate')
		self.button_quit = tk.Button(self.root, text='QUIT', fg='red', command=self.root.destroy).grid(row=14, column=4)
		self.button_ok.grid(row=14, column=3)
		self.button_ok.bind('<Button-1>', self.result)


	def result(self, event):
		self.name = locals()
		count = 0
		value1_list = []
		value2_list = []
		weight_list = []

		battle1 = self.battle1.get()
		battle2 = self.battle2.get()
		for i in range(1, 12):
			if i is 4:
				continue
			self.name["n"+str(i)] = self.indexes_name["idx_name"+str(i)].get()
			if self.name["n"+str(i)] is None:
				break
			self.name["v1"+str(i)] = self.indexes_name["idx_value1"+str(i)].get()
			self.name["v2"+str(i)] = self.indexes_name["idx_value2"+str(i)].get()
			self.name["w"+str(i)] = self.indexes_name['weight'+str(i)].get()
			if self.name["v1"+str(i)] is "" or self.name["v2"+str(i)] is "" or self.name["w"+str(i)] is "":
				break
			count += float(self.name["w"+str(i)])
			if count > 1:
				self.weight_error(count)

			value1_list.append(float(self.name["v1"+str(i)]))
			value2_list.append(float(self.name["v2" + str(i)]))
			weight_list.append(float(self.name["w" + str(i)]))

		ret = self.calculate(value1_list, value2_list, weight_list)

		if round(count) == 1:
			showinfo(message="%s: %.2f\n%s: %.2f"%(battle1, ret[0], battle2, ret[-1]))
		else:
			self.weight_error(count)

	def weight_error(self, count):
		showinfo(message="weight' sum unequal 1! current weight%.2f"%count)

	def calculate(self, value1, value2, weight):

		v1 = (numpy.mat(value1)*numpy.mat(weight).T)/len(weight)
		v2 = (numpy.mat(value2)*numpy.mat(weight).T)/len(weight)

		return [v1,v2]


def main():
	root = tk.Tk()
	tr = SwitchOrPs(root)
	root.mainloop()

if __name__ == '__main__':
	main()