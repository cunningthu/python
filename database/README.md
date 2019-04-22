Runs on Flask using python, postgresql, bootstrap, and sqlalchemy

Files needed:
  /templates
  application.py
  flights.csv
  create.sql (for postgresql)
  passengers.sql (for postgresql)
  insert.sql (for postgresql flights db values)
  joins.sql (for postgresql passenger db values)

Navigetion:
  / : lets you select a flight and add a passenger
  /flights : shows a list of flights and each item is a link to a detail of flight
  /flights/1 : shows first flight's details and all the passengers on that flight
  /flights/(int) : shows flight # (int) details and all passengers on that flight

To run type on cmd: set FLASK_APP=application.py
then type: flask run
