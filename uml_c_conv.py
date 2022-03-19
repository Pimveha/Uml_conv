class Uml_conv:
	def __init__(self, class_name, attributes, methods):
		self.class_name = class_name
		self.attributes = attributes
		self.methods = methods

	def set_class(self, n_class):
		self.class_name = n_class

	def get_class(self):
		return self.class_name

	def set_attributes(self, n_attributes):
		self.attributes = n_attributes

	def get_attributes(self):
		return self.attributes

	def set_methods(self, n_methods):
		self.methods = n_methods

	def get_methods(self):
		return self.methods

	def get_f_class(self):
		return f"class {self.class_name}:"

	def get_f_attributes(self):
		atr = self.attributes.split("\n")
		atr_list = [f"self.{atr[i]} = {atr[i]}" for i in range(len(atr))]
		return "\n".join(atr_list)

	def get_f_methods(self):
		# with or without proper return?
		meth = self.methods.split("\n")
		met_list = [f"def {(meth[i]).replace('(', '(self, ')}:" for i in range(len(meth))]
		for i in range(len(met_list)):
			if met_list[i].endswith(", ):"):
				met_list[i] = str(met_list[i])[:-4] + str(met_list[i])[-2:]
		return "\n".join(met_list)

	def __str__(self):
		f_class = f"class {self.class_name}:"

		atr = self.attributes.split("\n")
		atr_list = [f"self.{atr[i]} = {atr[i]}" for i in range(len(atr))]
		f_atributes = "\n\t\t".join(atr_list)

		meth = self.methods.split("\n")
		met_list = [f"def {(meth[i]).replace('(', '(self, ')}:" for i in range(len(meth))]
		for i in range(len(met_list)):
			if met_list[i].endswith(", ):"):
				met_list[i] = str(met_list[i])[:-4] + str(met_list[i])[-2:]
		f_methods = "\n\t".join(met_list[1:])

		f_comb = '{cls}\n\t{init_met}\n\t\t{atr}\n\t{met}'.format(cls = f_class, init_met = met_list[0], atr = f_atributes, met = f_methods)
	
		return f_comb


clas = "Werkwoord"

atr = """woord
verleden_tijd
voltooid_deelwoord
taal"""

met = """__init__(woord, verleden_tijd, voltooid_deelwoord, taal=’Nederlands’)
get_woord()
set_woord(woord)
get_verleden_tijd()
set_verleden_tijd(verleden_tijd)
get_voltooid_deelwoord()
set_voltooid_deelwoord(voltooid_deelwoord)
get_taal()
set_taal(taal)
__str__()"""

ww = Uml_conv(clas, atr, met)
print(ww.get_f_attributes())
print(ww)
