"""
This script will create 3 webpages for our flatmate bill application
It will do this using flask and create 3 webpages from MethodView
We will also create a form to get the input needed to calculate the
amounts for the flatmates on the invoice
"""

from flask.views import MethodView
from wtforms import Form,StringField,SubmitField
from flask import Flask,render_template

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
    def get(self):
        return 'this is the result page'

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

# we will now run the app (our flask instance) and create the webpages
# by setting the debug to true our changes will happen dynamically
app.run(debug=True)