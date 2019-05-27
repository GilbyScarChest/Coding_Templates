import numpy as np

# Import Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
# Create an engine for the chinook.sqlite database
engine = create_engine("sqlite:///../Resources/chinook.sqlite", echo=False)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Invoices = Base.classes.invoices
Items = Base.classes.invoice_items

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
   """List all available api routes."""
   return (
       f"Available Routes:<br/>"
       f"/api/countries<br/>"
       f"/api/invoice_total<br/>"
       f"/api/postal_codes_country/<country_name><br/>"
       f"/api/item_totals_country/<country_name><br/>"
       f"/api/item_totals<br/>"
       f"/api/item_totals_all_postal_code/<country_name><br/>"
   )


@app.route("/api/countries")
def countries():
   """Return a list of all passenger names"""
   # Query all passengers
   results = session.query(Invoices.BillingCountry).group_by(Invoices.BillingCountry).all()

   # Convert list of tuples into normal list
   all = list(np.ravel(results))

   return jsonify(all)

@app.route("/api/invoice_total")
def invoice_total():
   """# Design a query that lists the invoices totals for each billing country 
# and sort the output in descending order."""
   # Query all passengers
   results = session.query(Invoices.BillingCountry, func.sum(Invoices.Total)).\
   group_by(Invoices.BillingCountry).\
   order_by(func.sum(Invoices.Total).desc()).all()

   results =  [(item[0], float(item[1]))  for item in results]

   # Convert list of tuples into normal list
   invoice = list(np.ravel(results))

   return jsonify(invoice)

@app.route("/api/postal_codes_country/<country_name>")
def postal_codes(country_name):
   """# List all of the Billing Postal Codes for the country."""

   results = session.query(Invoices.BillingPostalCode).\
   filter(Invoices.BillingCountry == country_name).group_by(Invoices.BillingPostalCode).all()

   postal_codes = list(np.ravel(results))

   return jsonify(postal_codes)


# @app.route("/api/item_totals_country/<country_name>")
# def item_totals(country_name):
#     """Calculate the Item Totals (sum(UnitPrice * Quantity)) for the country"""
#     results = session.query(func.sum(Items.UnitPrice * Items.Quantity)).\
#     filter(Invoices.InvoiceId == Items.InvoiceId).\
#     filter(Invoices.BillingCountry == country_name).scalar()
#     item_totals = list(np.ravel(results))

#     return jsonify(item_totals)


# @app.route("/api/item_totals_all_postal_code/<country_name>")
# def item_totals(country_name):
# # Calculate the Item Totals `sum(UnitPrice * Quantity)` for each Billing Postal Code in the country
# # Sort the results in descending order by Total
#     results = session.query(Invoices.BillingPostalCode, func.sum(Items.UnitPrice * Items.Quantity)).\
#     filter(Invoices.InvoiceId == Items.InvoiceId).\
#     filter(Invoices.BillingCountry == country_name).\
#     group_by(Invoices.BillingPostalCode).\
#     order_by(func.sum(Items.UnitPrice * Items.Quantity).desc()).all()

#     item_totals_per_code = list(np.ravel(results))

#     return jsonify(item_totals_per_code)



if __name__ == '__main__':
   app.run(debug=True)