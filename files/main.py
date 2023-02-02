import utils

bill_amount = int(input('Hey user enter the bill amount: '))
current_period = input('What is the period of the bill: ')
flatmate_1 = input('Enter the first flatmate: ')
flatmate_2 = input('Enter the second flatmate: ')
days_fm1 = int(input(f'How many days was {flatmate_1} in the flat: '))
days_fm2 = int(input(f'How many days was {flatmate_2} in the flat: '))

bill = utils.Bill(bill_amount, current_period)
flatmate1 = utils.Flatmate(flatmate_1, days_fm1)
flatmate2 = utils.Flatmate(flatmate_2, days_fm2)

print(f'{flatmate1.name} pays {flatmate1.pays(bill, flatmate2)} €')
print(f'{flatmate2.name} pays {flatmate2.pays(bill, flatmate1)} €')

pdf_report = utils.PdfReport(filename=f'{bill.period}.pdf')
pdf_report.generate(flatmate1, flatmate2, bill)
