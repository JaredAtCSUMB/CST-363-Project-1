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
employeeQuery = "SELECT * FROM employee WHERE username = %s AND password = %s"
orders = "SELECT o.order_id, DATE_FORMAT(o.order_date, '%m-%d-%y'), s.service_name, CONCAT(c.car_year, ' ', c.car_make, ' ', c.car_model) AS vehicleInfo FROM orders AS o INNER JOIN car AS c ON o.car_id = c.car_id INNER JOIN service AS s ON o.service_id = s.service_id ORDER BY o.order_date ASC"

deleteOrder = "DELETE FROM orders WHERE order_id = %s"

insertOrder = "INSERT INTO orders (car_id, service_id, order_date) VALUE (%s, %s, %s)"



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
print("<a href=\"../employee.html\" class=\"back-btn\">< Go Back</a>")
print("<h1>Employee Portal</h1>")
print("<div class=\"row justify-content-center\">")
print("<div class=\"card\">")
print("<img src=\"../images/employee.jpg\" class=\"card-img-top\" alt=\"services\">")

#Check if logged in.
if "addOrder" in form:
	print("<div class=\"alert alert-success alert-dismissible\" role=\"alert\"><a href=\"#\" class=\"close\" data-dismiss=\"alert\" aria-label=\"close\">&times;</a>Please register or login. Select vehicle, and request service. Select the service and date you want.</div>")

if "userName" in form:
	userName = form["userName"].value
	password= form["password"].value
	customerID = form["customerId"].value
	serviceID= form["serviceId"].value
	cursord = cnx.cursor()
	cursord.execute(employeeQuery, (userName, password))
	rowl = cursord.fetchone()
	# userid and password did not match
	if rowl is None:
		# error message
		login = False
	# userid and password did match
	else:
		login = True
		if(serviceID != '' and customerID != ''):
			insertcursor = cnx.cursor()
			insertcursor.execute(insertOrder, (customerID, serviceID, '2019-01-31'))

else:
	login = False

if login == True:

	if "closeOrder" in form:
		orderid = form["orderid"].value

		cancelcursor = cnx.cursor()
		cancelcursor.execute(deleteOrder, (orderid, ))
		print("<div class=\"alert alert-success alert-dismissible\" role=\"alert\"><a href=\"#\" class=\"close\" data-dismiss=\"alert\" aria-label=\"close\">&times;</a>Successfully removed service request.</div>")


	cursorb = cnx.cursor()
	cursorb.execute(orders)
	rowb = cursorb.fetchall()

	print("<div class=\"card-body\">")

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
		print("<td><button type=\"submit\" class=\"btn btn-danger\" name=\"serviceID\" value=\"" + str(y[0]) + "\" data-toggle=\"modal\" data-target=\"#cancelAppointmentModal" + str(y[0]) + "\">Close Appointment</button></td>")


		print("<div class=\"modal fade\" id=\"cancelAppointmentModal" + str(y[0]) + "\" role=\"dialog\">")
		print("<div class=\"modal-dialog\">")

		print("<div class=\"modal-content\">")
		print("<div class=\"modal-header\">")
		print("<h4 class=\"modal-title\">Are You sure You want to close appointment?</h4>")
		print("</div>")
		print("<div class=\"modal-body\">")
		print("<form enctype=\"multipart/form-data\" method=\"post\" action=\"employee.py\">")
		print("<input type=\"hidden\" name=\"userName\" id=\"userName\" value=\"" + userName + "\" />")
		print("<input type=\"hidden\" name=\"password\" id=\"password\" value=\"" + password + "\" />")
		print("<input type=\"hidden\" name=\"orderid\" id=\"orderid\" value=\"" + str(y[0]) + "\" />")
		print("<input type=\"submit\" class=\"btn btn-success\" name=\"closeOrder\" id=\"closeOrder\" value=\"Yes\"> </form>")
		print("<button type=\"button\" class=\"btn btn-danger\" data-dismiss=\"modal\">No</button>")
		print("</div>")
		print("</div>")
		print("</div>")
		print("</div>")


		print("</tr>")
	print("</table>")
	print("<hr />")
	print("</div>")


else:
	print("Account Not Found. Please click back and try again.");





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
