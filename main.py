"""
This script will create 3 webpages for our flatmate bill application
It will do this using flask and create 3 webpages from MethodView
We will also create a form to get the input needed to calculate the
amounts for the flatmates on the invoice
"""

from flask.views import MethodView
from wtforms import Form,StringField,SubmitField
from flask import Flask,render_template,request
# to import from different directories on your pc you need to state
# import from directory.file the desired object
from files import utils


app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template('index.html')

class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html',
                               billform = bill_form)

class ResultsPage(MethodView):
    """
    this
    """
    def post(self):
        # we will request (acces) the data that is inputted in the previous page (BillFormPage)
        billform = BillForm(request.form)
        amount = float(billform.amount.data)
        period = billform.period.data
        # with this info we will instantiate a bill that needs to be divided
        the_bill = utils.Bill(amount,period)
        # now that we have the bill we create our flatmates
        name1 = billform.name1.data
        name2 = billform.name2.data
        days_in_house1 = float(billform.days_in_house1.data)
        days_in_house2 = float(billform.days_in_house2.data)
        flatmate1 = utils.Flatmate(name1,days_in_house1)
        flatmate2 = utils.Flatmate(name2,days_in_house2)

        return f'{flatmate1.name} pays {flatmate1.pays(the_bill,flatmate2)} €\n ' \
               f'{flatmate2.name} pays {flatmate2.pays(the_bill,flatmate1)}'

class BillForm(Form):
    amount = StringField('Bill amount: ')
    period = StringField('Period: ')

    name1 = StringField('Name: ')
    days_in_house1 = StringField('Days in house: ')

    name2 = StringField('Name: ')
    days_in_house2 = StringField('Days in house: ')

    button = SubmitField('Calculate')

app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form',
                 view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results',
                 view_func=ResultsPage.as_view('results_page'))

# we will now run the app (our flask instance) and create the webpages
# by setting the debug to true our changes will happen dynamically
app.run(debug=True)