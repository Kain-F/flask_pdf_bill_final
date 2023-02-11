import webbrowser
import fpdf
import os
from filestack import Client

class Bill():
	"""
	Object that contains data about the bill such as the total amount and period of the bill
	"""

	def __init__(self,amount,period):
		self.amount = amount
		self.period = period

class Flatmate(Bill):
	"""
	Creates a flatmate person who lives in the flat and pays a share of the bill
	"""

	def __init__(self,name,days_in_house):
		self.name = name
		self.days_in_house = days_in_house

	def pays(self,bill, flatmate2):
		weight = self.days_in_house /(self.days_in_house + flatmate2.days_in_house)
		to_pay = bill.amount * weight
		return to_pay

class PdfReport(Flatmate):
	"""
Creates a pdf file that contains data about the flatmates
such as their names, their due amounts and the period of the bill
	"""

	def __init__(self,filename):
		self.filename = filename

	def generate(self,flatmate1,flatmate2,bill):
		flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2),2))
		flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1),2))
		# we create the pdf instance
		pdf = fpdf.FPDF(orientation='P',unit='pt',format='A4')

		# we create a page in our pdf instance
		pdf.add_page()

		# we make our headers
		# Add icon
		pdf.image('images/house.png',w=30,h=30)
		#pdf.image('house.png',w=30,h=30) # this will look for the png file in the working directory
		# Insert title
		pdf.set_font(family='Times', size=14, style='B')  # we set the font
		pdf.cell(w=0, h=80, txt='Flatmates bill',  align='C', border= 1, ln=1)  # we create a text inside a cell
		# Insert period
		pdf.cell(w=100, h=40, txt='Period:')  # we create a text inside a cell
		pdf.cell(w=150, h=40, txt=bill.period.capitalize(),ln=1)  # we create a text inside a cell
		# Insert flatmate names and their due amount
		# flatmate 1
		pdf.set_font(family='Times', size=12)  # we set the font
		pdf.cell(w=150,h=25,txt=flatmate1.name) # we made the name of our first flatmate
		pdf.cell(w=150,h=25,txt=flatmate1_pay,ln=1) # we wrote the due amount
		# flatmate 2
		pdf.cell(w=150, h=25, txt=flatmate2.name)  # we made the name of our first flatmate
		pdf.cell(w=150, h=25, txt=flatmate2_pay,ln=1)  # we wrote the due amount

		# we change the working directory to the directory where the reports need to be saved
		os.chdir("reports")
		# we create the pdf and save it in our working directory
		pdf.output(self.filename)
		# we open the pdf via the webbrowser
		webbrowser.open(self.filename)

class FileSharer():
	"""
	We will generate a link in which the generated pdf is uploaded and will be displayed and share that link
	"""
	def __init__(self,filepath,api_key = 'A1mgj36RyQ92wCnnEbcU7z'):
		self.api_key = api_key
		self.filepath = filepath 

	def share(self):
		# we want to generate a link to an url where the file is located using file link
		client = Client(self.api_key)
		new_filelink = client.upload(filepath=self.filepath)
		return  new_filelink.url




