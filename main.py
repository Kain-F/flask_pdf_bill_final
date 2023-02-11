"""
This script will create 3 webpages for our flatmate bill application
It will do this using flask and create 3 webpages from MethodView
We will also create a form to get the input needed to calculate the
amounts for the flatmates on the invoice
"""

from flask.views import MethodView
from wtforms import Form
from flask import Flask

app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return 'Hello world'

class BillFormPage(MethodView):
    def get(self):
        return 'this is the bill form page'

class ResultsPage(MethodView):
    def get(self):
        return 'this is the result page'

class BillForm(Form):
    pass

app.add_url_rule('/',view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill',view_func=BillFormPage.as_view('bill_form_page'))
app.run()