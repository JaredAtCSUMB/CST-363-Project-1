#!/usr/bin/env python3

# this file must be in the /cgi-bin/ directory of the server
import cgitb , cgi
import mysql.connector
cgitb.enable()
form = cgi.FieldStorage()
#
#  code to get input values goes here
#
# we are not retrieving any data here

print("Content-Type: text/html")    # HTML is following
print("\n")                             # blank line required, end of headers
print("<!doctype html>")
print("<html lang=\"en\">")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">")
print("<link rel=\"stylesheet\" href=\"../styles.css\">")
print("<link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css\" integrity=\"sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS\" crossorigin=\"anonymous\">")
print("<link rel=icon href=../favicon.png>")
print("<title>JAD - Customer Portal</title>")
print("</head>")
print("<body>")

#queries
services = "SELECT * FROM service"
vehicles = "SELECT car_id, car_make, car_model, car_year, CONCAT(car_year, ' ', car_make, ' ', car_model) AS vehicleInfo FROM car WHERE customer_id = %s"
customerQuery = "SELECT * FROM customer WHERE username = %s AND password = %s"
usernameCheck = "SELECT * FROM customer WHERE username = %s"
orders = "SELECT o.order_id, DATE_FORMAT(o.order_date, '%m-%d-%y'), s.service_name, CONCAT(c.car_year, ' ', c.car_make, ' ', c.car_model) AS vehicleInfo FROM orders AS o INNER JOIN car AS c ON o.car_id = c.car_id INNER JOIN service AS s ON o.service_id = s.service_id WHERE c.customer_id = %s ORDER BY o.order_date ASC"
customer_orders = "SELECT * FROM orders AS o INNER JOIN car AS c ON o.car_id = c.car_id INNER JOIN service AS s ON o.service_id = s.service_id WHERE c.customer_id = %s"

deleteOrder = "DELETE FROM orders WHERE order_id = %s and car_id IN (SELECT car_id FROM car WHERE customer_id = %s)"
insertService = "INSERT INTO orders (order_date, car_id, service_id) VALUES (%s, %s, %s)"
addVehicle = "INSERT INTO car (car_make, car_model, car_year, customer_id) VALUES (%s, %s, %s, %s)"
updatePassword = "UPDATE customer SET password = %s WHERE password = %s AND customer_id = %s"
updateInformation = "UPDATE customer SET first_name = %s, last_name = %s, phone_number = %s WHERE customer_id = %s"
addCustomer = "INSERT INTO customer (first_name, last_name, username, password, phone_number) VALUES (%s, %s, %s, %s, %s)"


# connect to database
# IMPORTANT: update this password with your own
dbPassword = 'dbPassword'
cnx = mysql.connector.connect(user='root',
                                password=dbPassword,
                                database='jadautorepair',
                                host='127.0.0.1')



# userid and password did not match

print("<div class=\"main-container\">")
print("<div class=\"card main-card\">")
print("<a href=\"../index.html\" class=\"back-btn\">< Go Back</a>")
print("<h1>Customer Portal</h1>")
print("<div class=\"row justify-content-center\">")
print("<div class=\"card\">")
print("<img src=\"../images/customer.jpg\" class=\"card-img-top\" alt=\"services\">")

#Check if logged in.
if "addOrder" in form:
	print("<div class=\"alert alert-success alert-dismissible\" role=\"alert\"><a href=\"#\" class=\"close\" data-dismiss=\"alert\" aria-label=\"close\">&times;</a>Please register or login. Select vehicle, and request service. Select the service and date you want.</div>")
if "register" in form:
	userName = form["userName"].value
	password= form["password"].value
	firstName = form["firstName"].value
	lastName = form["lastName"].value
	phoneNumber = form["phoneNumber"].value
	cursorf = cnx.cursor()
	cursorf.execute(usernameCheck, (userName, ))
	rowt = cursorf.fetchone()
	# userid and password did not match
	if rowt is None:
		insertcursor = cnx.cursor()
		insertcursor.execute(addCustomer, (firstName, lastName, userName, password, phoneNumber))
		#enter information sql
		cursord = cnx.cursor()
		cursord.execute(customerQuery, (userName, password))
		rowl = cursord.fetchone()
		# userid and password did not match
		if rowl is None:
			# error message
			login = False
		# userid and password did match
		else:
			login = True
			customerID = rowl[0];

			carMake = form["carMake"].value
			carModel = form["carModel"].value
			carYear = form["carYear"].value
			addVehiclecursor = cnx.cursor()
			addVehiclecursor.execute(addVehicle, (carMake, carModel, carYear, customerID))
			print("<div class=\"alert alert-success alert-dismissible\" role=\"alert\"><a href=\"#\" class=\"close\" data-dismiss=\"alert\" aria-label=\"close\">&times;</a>Thank you for creating your profile.</div>")
	# userid and password did match
	else:
		login = False
		print("<div class=\"alert alert-warning\" role=\"alert\">Username Already Exist</div>")
elif "userName" in form:
	userName = form["userName"].value
	password= form["password"].value
	cursord = cnx.cursor()
	cursord.execute(customerQuery, (userName, password))
	rowl = cursord.fetchone()
	# userid and password did not match
	if rowl is None:
		# error message
		login = False
	# userid and password did match
	else:
		login = True
		customerID = rowl[0];
else:
	login = False

if login == True:

	if "cancelOrder" in form:
		orderid = form["orderid"].value

		cancelcursor = cnx.cursor()
		cancelcursor.execute(deleteOrder, (orderid, customerID))
		print("<div class=\"alert alert-success alert-dismissible\" role=\"alert\"><a href=\"#\" class=\"close\" data-dismiss=\"alert\" aria-label=\"close\">&times;</a>Successfully removed service request.</div>")

	if "requestService" in form:
		apptDate = form["apptDate"].value
		vehicleid = form["vehicleid"].value
		serviceid = form["serviceid"].value
		requestcursor = cnx.cursor()
		requestcursor.execute(insertService, (apptDate, vehicleid, serviceid))

	if "addVehicle" in form:
		carMake = form["carMake"].value
		carModel = form["carModel"].value
		carYear = form["carYear"].value
		addVehiclecursor = cnx.cursor()
		addVehiclecursor.execute(addVehicle, (carMake, carModel, carYear, customerID))
		print("<div class=\"alert alert-success alert-dismissible\" role=\"alert\"><a href=\"#\" class=\"close\" data-dismiss=\"alert\" aria-label=\"close\">&times;</a>Successfully added vehicle to your profile.</div>")
	if "updatePassword" in form:
		newPassword = form["newPassword"].value
		updatePasswordcursor = cnx.cursor()
		updatePasswordcursor.execute(updatePassword, (newPassword, password, customerID))
		print("<div class=\"alert alert-success alert-dismissible\" role=\"alert\"><a href=\"#\" class=\"close\" data-dismiss=\"alert\" aria-label=\"close\">&times;</a>Successfully updated your password.</div>")
		password = newPassword
	if "updateInformation" in form:
		firstName = form["firstName"].value
		lastName = form["lastName"].value
		phoneNumber = form["phoneNumber"].value
		addVehiclecursor = cnx.cursor()
		addVehiclecursor.execute(updateInformation, (firstName, lastName, phoneNumber, customerID))
		print("<div class=\"alert alert-success alert-dismissible\" role=\"alert\"><a href=\"#\" class=\"close\" data-dismiss=\"alert\" aria-label=\"close\">&times;</a>Successfully updated profile information.</div>")


	cursor = cnx.cursor()
	cursor.execute(vehicles, (customerID,))
	row = cursor.fetchall()

	cursorb = cnx.cursor()
	cursorb.execute(orders, (customerID, ))
	rowb = cursorb.fetchall()

	cursorc = cnx.cursor()
	cursorc.execute(services)
	rowc = cursorc.fetchall()
	print("<script type=\"text/javascript\">")
	print("function openSection(section){")
	print("if(document.getElementById(section).style.display == 'none'){")
	print("document.getElementById(section).style.display = '';")
	print("}else{")
	print("document.getElementById(section).style.display = 'none';")
	print("}}")
	print("</script>")

	print("<div class=\"card-body\">")
	print("<div class=\"row\">")
	print("<div class=\"col-lg-6\"><a href=\"#\" class=\"h5\" onclick=\"openSection('myVehicles')\">My Vehicles +</a></div>")
	print("<div class=\"col-lg-6\"><a href=\"#\" class=\"h5\" onclick=\"openSection('myAppointments')\">My Appointments +</a></div>")
	print("</div>")
	print("<div class=\"row\">")
	print("<div class=\"col-lg-6\"><a href=\"#\" class=\"h5\" onclick=\"openSection('addVehicle')\">Add A Vehicles +</a></div>")
	print("<div class=\"col-lg-6\"><a href=\"#\" class=\"h5\" onclick=\"openSection('editAccount')\">Edit Account Information +</a></div>")
	print("</div>")
	print("<hr />")


	#My Appointments
	print("<div id=\"myAppointments\">")
	print("<h4>My Appointments</h4>")
	print("<table style=\"width:50rem;\" class=\"table-bordered\"><tr>")
	print("<th>Date</th>")
	print("<th>Service</th>")
	print("<th>Vehicle</th>")
	print("<th></th>")
	print("</tr>")
	for y in rowb:
		print("<tr>")
		print("<td>" + str(y[1]) + "</td>")
		print("<td>" + str(y[2]) + "</td>")
		print("<td>" + str(y[3]) + "</td>")
		print("<td><button type=\"submit\" class=\"btn btn-danger\" name=\"serviceID\" value=\"" + str(y[0]) + "\" data-toggle=\"modal\" data-target=\"#cancelAppointmentModal" + str(y[0]) + "\">Cancel Appointment</button></td>")


		print("<div class=\"modal fade\" id=\"cancelAppointmentModal" + str(y[0]) + "\" role=\"dialog\">")
		print("<div class=\"modal-dialog\">")

		print("<div class=\"modal-content\">")
		print("<div class=\"modal-header\">")
		print("<h4 class=\"modal-title\">Are You sure You want to cancel appointment?</h4>")
		print("</div>")
		print("<div class=\"modal-body\">")
		print("<form enctype=\"multipart/form-data\" method=\"post\" action=\"customer.py\">")
		print("<input type=\"hidden\" name=\"userName\" id=\"userName\" value=\"" + userName + "\" />")
		print("<input type=\"hidden\" name=\"password\" id=\"password\" value=\"" + password + "\" />")
		print("<input type=\"hidden\" name=\"orderid\" id=\"orderid\" value=\"" + str(y[0]) + "\" />")
		print("<input type=\"submit\" class=\"btn btn-success\" name=\"cancelOrder\" id=\"cancelOrder\" value=\"Yes\"> </form>")
		print("<button type=\"button\" class=\"btn btn-danger\" data-dismiss=\"modal\">No</button>")
		print("</div>")
		print("</div>")
		print("</div>")
		print("</div>")


		print("</tr>")
	print("</table>")
	print("<hr />")
	print("</div>")

	#My Vehicles
	print("<div id=\"myVehicles\" >")
	print("<h4>My Vehicles</h4>")
	print("<table style=\"width:50rem;\" class=\"table-bordered\"><tr>")
	print("<th>Year</th>")
	print("<th>Make</th>")
	print("<th>Model</th>")
	print("<th></th>")
	print("</tr>")
	for x in row:
		print("<tr>")
		print("<td>" + str(x[3]) + "</td>")
		print("<td>" + str(x[1]) + "</td>")
		print("<td>" + str(x[2]) + "</td>")

		print("<td><button type=\"submit\" class=\"btn btn-success\" name=\"serviceID\" value=\"" + str(x[0]) + "\" data-toggle=\"modal\" data-target=\"#requestServiceModal" + str(x[0]) + "\">Request Service</button></td>")
		print("<div class=\"modal fade\" id=\"requestServiceModal" + str(x[0]) + "\" role=\"dialog\">")
		print("<div class=\"modal-dialog\">")

		print("<div class=\"modal-content\">")
		print("<div class=\"modal-header\">")
		print("<h4 class=\"modal-title\">Request Service for " + str(x[4]) + "</h4>")
		print("</div>")
		print("<div class=\"modal-body\">")
		print("<form enctype=\"multipart/form-data\" method=\"post\" action=\"customer.py\">")
		print("<input type=\"hidden\" name=\"userName\" id=\"userName\" value=\"" + userName + "\" />")
		print("<input type=\"hidden\" name=\"password\" id=\"password\" value=\"" + password + "\" />")
		print("<input type=\"hidden\" name=\"vehicleid\" id=\"vehicleid\" value=\"" + str(x[0]) + "\" />")
		print("<label for=\"apptDate\">Phone Number: </label>")
		print("<input type=\"date\" name=\"apptDate\" id=\"apptDate\" /><br>")
		print("<label for=\"service\">Phone Number: </label>")
		print("<select name=\"serviceid\" id=\"serviceid\" />")
		for z in rowc:
			print("<option value='" + str(z[0]) + "'>" + str(z[1]) + " ($" + str(z[2]) + ")</option>")
		print("</select>")
		print("<input type=\"submit\" class=\"btn btn-success\" name=\"requestService\" id=\"requestService\" value=\"Submit\"> </form>")
		print("<button type=\"button\" class=\"btn btn-default\" data-dismiss=\"modal\">Cancel</button>")
		print("</div>")
		print("</div>")
		print("</div>")
		print("</div>")


		print("</tr>")
	print("</table>")
	print("</div>")
	print("<hr />")
	print("</div>")

	#Add A Vehicle
	print("<div id=\"addVehicle\" style=\"display:none\">")
	print("<h4>Add A Vehicle</h4>")
	print("<form method=\"post\" enctype=\"multipart/form-data\" action=\"customer.py\">")
	print("<label for=\"carMake\">Car Make: </label>")
	print("<input type=\"text\" name=\"carMake\" id=\"carMake\" /><br>")
	print("<label for=\"carModel\">Car Model: </label>")
	print("<input type=\"text\" name=\"carModel\" id=\"carModel\" /><br>")
	print("<label for=\"carYear\">Car Year: </label>")
	print("<input type=\"text\" name=\"carYear\" id=\"carYear\" /><br>")
	print("<input type=\"hidden\" name=\"userName\" id=\"userName\" value=\"" + userName + "\" />")
	print("<input type=\"hidden\" name=\"password\" id=\"password\" value=\"" + password + "\" />")
	print("<button type=\"submit\"  name=\"addVehicle\" id=\"addVehicle\" class=\"btn btn-success\">Add Vehicle</button>")
	print("</form>")
	print("<hr />")
	print("</div>")

	#Edit Account Information
	print("<div id=\"editAccount\" style=\"display:none\">")
	print("<h4>Edit Account Information</h4>")
	print("<form method=\"post\" enctype=\"multipart/form-data\" action=\"customer.py\">")
	print("<h5>Edit Information</h5>")
	print("<label for=\"firstName\">First Name: </label>")
	print("<input type=\"text\" name=\"firstName\" id=\"firstName\" value=\"" + rowl[1] + "\" /><br>")
	print("<label for=\"lastName\">Last Name: </label>")
	print("<input type=\"text\" name=\"lastName\" id=\"Lastname\" value=\"" + rowl[2] + "\" /><br>")
	print("<label for=\"phoneNumber\">Phone Number: </label>")
	print("<input type=\"text\" name=\"phoneNumber\" id=\"phoneNumber\"  value=\"" + rowl[5] + "\" /><br>")
	print("<input type=\"hidden\" name=\"userName\" id=\"userName\" value=\"" + userName + "\" />")
	print("<input type=\"hidden\" name=\"password\" id=\"password\" value=\"" + password + "\" />")
	print("<button type=\"submit\" name=\"updateInformation\" id=\"updateInformation\" class=\"btn btn-success\">Update</button>")
	print("</form>")

	print("<br /><br />")

	print("<form method=\"post\" enctype=\"multipart/form-data\" action=\"customer.py\">")
	print("<h5>Update Password</h5>")
	print("<label for=\"password\">New Password: </label>")
	print("<input type=\"password\" name=\"newPassword\" id=\"newPassword\" /><br>")
	print("<input type=\"hidden\" name=\"userName\" id=\"userName\" value=\"" + userName + "\" />")
	print("<input type=\"hidden\" name=\"password\" id=\"password\" value=\"" + password + "\" />")
	print("<button type=\"submit\" name=\"updatePassword\" id=\"updatePassword\" class=\"btn btn-success\">Update</button>")
	print("</form>")
	print("<hr />")
	print("</div>")
	print("</div>")
else:
	print("<div class=\"row\">")
	print("<div class=\"card\" style=\"width: 20rem; padding: 20px 0;\">")
	print("<h5 class=\"card-title\">View Your Order(s)</h5>")
	print("<div class=\"card-body\">")
	print("<!-- TODO: connect customer form -->")
	print("<form method=\"post\" enctype=\"multipart/form-data\" action=\"customer.py\">")
	print("<label for=\"userName\">Username: </label>")
	print("<input type=\"text\" name=\"userName\" id=\"userName\" /><br>")
	print("<label for=\"password\">Password: </label>")
	print("<input type=\"password\" name=\"password\" id=\"password\" /><br>")
	print("<button type=\"submit\" class=\"btn btn-primary\">Login</button>")
	print("</form>")
	print("</div>")
	print("</div>")
	print("<p class=\"divider\">or</p>")
	print("<div class=\"card\" style=\"width: 22rem; padding: 20px 0;\">")
	print("<h5 class=\"card-title\">Register a New Account</h5>")
	print("<div class=\"card-body\">")
	print("<!-- TODO: connect customer form -->")
	print("<form method=\"post\" enctype=\"multipart/form-data\" action=\"customer.py\">")
	print("<label for=\"userName\">Username: </label>")
	print("<input type=\"text\" name=\"userName\" id=\"userName\" /><br>")
	print("<label for=\"password\">Password: </label>")
	print("<input type=\"password\" name=\"password\" id=\"password\" /><br>")
	print("<label for=\"firstName\">First Name: </label>")
	print("<input type=\"text\" name=\"firstName\" id=\"firstName\" /><br>")
	print("<label for=\"lastName\">Last Name: </label>")
	print("<input type=\"text\" name=\"lastName\" id=\"Lastname\" /><br>")
	print("<label for=\"phoneNumber\">Phone Number: </label>")
	print("<input type=\"text\" name=\"phoneNumber\" id=\"phoneNumber\" /><br>")
	print("<label for=\"carMake\">Car Make: </label>")
	print("<input type=\"text\" name=\"carMake\" id=\"carMake\" /><br>")
	print("<label for=\"carModel\">Car Model: </label>")
	print("<input type=\"text\" name=\"carModel\" id=\"carModel\" /><br>")
	print("<label for=\"carYear\">Car Year: </label>")
	print("<input type=\"text\" name=\"carYear\" id=\"carYear\" /><br>")
	print("<button type=\"submit\" name=\"register\" id=\"register\" class=\"btn btn-primary\">Register</button>")
	print("</form>")
	print("</div>")
	print("</div>")
	print("</div>")





print("</div>")
print("</div>")
print("</div>")
print("</div>")
print("<script src=\"https://code.jquery.com/jquery-3.3.1.slim.min.js\" integrity=\"sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo\" crossorigin=\"anonymous\"></script>")
print("<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js\" integrity=\"sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut\" crossorigin=\"anonymous\"></script>")
print("<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js\" integrity=\"sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k\" crossorigin=\"anonymous\"></script>")


print("</body></html>")
cnx.commit()
cnx.close()
