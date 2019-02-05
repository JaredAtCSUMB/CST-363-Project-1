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
employeeQuery = "SELECT * FROM jadautorepair.employee WHERE username = %s AND password = %s"

multicar = "select customer.customer_id, customer.first_name, customer.last_name from customer, orders where customer.customer_id = orders.customer_id group by customer.customer_id, customer.first_name, customer.last_name having count(distinct orders.car_id) > 1";
numberOfServices = "select service.service_id, service_name, order_year, order_month, order_day, sum(amount) as total from service, orders where service.service_id = orders.service_id group by service.service_id, service_name, order_year, order_month, order_day with rollup";
mostUsed = "select service.service_id, service_name, order_year as 'year', count(*) as times from service, orders where service.service_id = orders.service_id group by service.service_id, service_name, order_year order by times desc limit 1";
timeOfYear = "select service.service_id, service_name, order_year as 'year', order_month as 'month', order_day as 'day', count(*) as 'number of times used' from service, orders where service.service_id = orders.service_id group by service.service_id, service_name, order_year, order_month, order_day order by count(*) desc";
averageCount = "select order_year as 'year', order_month as 'month', avg(customer_id) as 'average number of customers' from orders group by order_year, order_month";
annualSpend = "select order_year as 'year', avg(amount) as 'average spending' from orders group by order_year";



# connect to database
# IMPORTANT: update this password with your own
dbPassword = ''
cnx = mysql.connector.connect(user='root',
                                password=dbPassword,
                                database='jadautorepair_dw',
                                host='127.0.0.1')



# userid and password did not match

print("<div class=\"main-container\">")
print("<div class=\"card main-card\">")
print("<a href=\"../employee.html\" class=\"back-btn\">< Go Back</a>")
print("<h1>Data Warehouse Portal</h1>")
print("<div class=\"row justify-content-center\">")
print("<div class=\"card\">")
print("<img src=\"../images/report.jpg\" class=\"card-img-top\" alt=\"services\">")

#Check if logged in.
if "addOrder" in form:
	print("<div class=\"alert alert-success alert-dismissible\" role=\"alert\"><a href=\"#\" class=\"close\" data-dismiss=\"alert\" aria-label=\"close\">&times;</a>Please register or login. Select vehicle, and request service. Select the service and date you want.</div>")

if "userName" in form:
	userName = form["userName"].value
	password= form["password"].value
	reportType = form["reportType"].value
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

else:
	login = False

if login == True:

	if reportType == 'multiCar':
		print("<form method=\"post\" enctype=\"multipart/form-data\" action=\"datawarehouse.py\">")
		print("<label for=\"reportType\">Report Type: </label>")
		print("<select name=\"reportType\" id=\"reportType\" class=\"select form-control-sm\">")
		print("<option value=\"multiCar\" selected>Multiple Cars in Shop</option>")
		print("<option value=\"numberOfServices\">Number of Services per Car</option>")
		print("<option value=\"mostUsed\">Most Used Services</option>")
		print("<option value=\"timeOfYear\">Service Times of Year</option>")
		print("<option value=\"averageCount\">Average Customer Count</option>")
		print("<option value=\"annualSpend\">Annual Average Spend</option>")
		print("</select>")
		print("<input type=\"hidden\" name=\"report\" id=\"report\" />")
		print("<input type=\"hidden\" name=\"userName\" id=\"userName\" value=\"" + userName + "\" />")
		print("<input type=\"hidden\" name=\"password\" id=\"password\" value=\"" + password + "\" />")
		print("<button type=\"submit\" class=\"btn btn-primary\">Request Report</button>")
		print("</form>")

		cursorb = cnx.cursor()
		cursorb.execute(multicar)
		rowb = cursorb.fetchall()

		print("<div class=\"card-body\">")

		#Multicar
		print("<div>")
		print("<h4>Multiple Cars in Shop</h4>")
		print("<table style=\"width:50rem;\" class=\"table-bordered\"><tr>")
		print("<th>customer_id</th>")
		print("<th>first_name</th>")
		print("<th>last_name</th>")
		print("</tr>")
		for y in rowb:
			print("<tr>")
			print("<td>" + str(y[0]) + "</td>")
			print("<td>" + str(y[1]) + "</td>")
			print("<td>" + str(y[2]) + "</td>")


			print("</tr>")
		print("</table>")
		print("<hr />")
		print("</div>")

	elif reportType == 'numberOfServices':
		print("<form method=\"post\" enctype=\"multipart/form-data\" action=\"datawarehouse.py\">")
		print("<label for=\"reportType\">Report Type: </label>")
		print("<select name=\"reportType\" id=\"reportType\" class=\"select form-control-sm\" value=\"" + reportType + "\">")
		print("<option value=\"multiCar\">Multiple Cars in Shop</option>")
		print("<option value=\"numberOfServices\" selected>Number of Services per Car</option>")
		print("<option value=\"mostUsed\">Most Used Services</option>")
		print("<option value=\"timeOfYear\">Service Times of Year</option>")
		print("<option value=\"averageCount\">Average Customer Count</option>")
		print("<option value=\"annualSpend\">Annual Average Spend</option>")
		print("</select>")
		print("<input type=\"hidden\" name=\"report\" id=\"report\" />")
		print("<input type=\"hidden\" name=\"userName\" id=\"userName\" value=\"" + userName + "\" />")
		print("<input type=\"hidden\" name=\"password\" id=\"password\" value=\"" + password + "\" />")
		print("<button type=\"submit\" class=\"btn btn-primary\">Request Report</button>")
		print("</form>")

		cursorb = cnx.cursor()
		cursorb.execute(numberOfServices)
		rowb = cursorb.fetchall()

		print("<div class=\"card-body\">")

		#Multicar
		print("<div>")
		print("<h4>Number of Services per Car</h4>")
		print("<table style=\"width:50rem;\" class=\"table-bordered\"><tr>")
		print("<th>service_id</th>")
		print("<th>service_name</th>")
		print("<th>order_year</th>")
		print("<th>order_month</th>")
		print("<th>order_day</th>")
		print("<th>total</th>")
		print("</tr>")
		for y in rowb:
			print("<tr>")
			print("<td>" + str(y[0]) + "</td>")
			print("<td>" + str(y[1]) + "</td>")
			print("<td>" + str(y[2]) + "</td>")
			print("<td>" + str(y[3]) + "</td>")
			print("<td>" + str(y[4]) + "</td>")
			print("<td>" + str(y[5]) + "</td>")


			print("</tr>")
		print("</table>")
		print("<hr />")
		print("</div>")

	elif reportType == 'mostUsed':
		print("<form method=\"post\" enctype=\"multipart/form-data\" action=\"datawarehouse.py\">")
		print("<label for=\"reportType\">Report Type: </label>")
		print("<select name=\"reportType\" id=\"reportType\" class=\"select form-control-sm\" value=\"" + reportType + "\">")
		print("<option value=\"multiCar\">Multiple Cars in Shop</option>")
		print("<option value=\"numberOfServices\">Number of Services per Car</option>")
		print("<option value=\"mostUsed\" selected>Most Used Services</option>")
		print("<option value=\"timeOfYear\">Service Times of Year</option>")
		print("<option value=\"averageCount\">Average Customer Count</option>")
		print("<option value=\"annualSpend\">Annual Average Spend</option>")
		print("</select>")
		print("<input type=\"hidden\" name=\"report\" id=\"report\" />")
		print("<input type=\"hidden\" name=\"userName\" id=\"userName\" value=\"" + userName + "\" />")
		print("<input type=\"hidden\" name=\"password\" id=\"password\" value=\"" + password + "\" />")
		print("<button type=\"submit\" class=\"btn btn-primary\">Request Report</button>")
		print("</form>")

		cursorb = cnx.cursor()
		cursorb.execute(mostUsed)
		rowb = cursorb.fetchall()

		print("<div class=\"card-body\">")

		#Multicar
		print("<div>")
		print("<h4>Most Used Services</h4>")
		print("<table style=\"width:50rem;\" class=\"table-bordered\"><tr>")
		print("<th>service_id</th>")
		print("<th>service_name</th>")
		print("<th>year</th>")
		print("<th>times</th>")

		print("</tr>")
		for y in rowb:
			print("<tr>")
			print("<td>" + str(y[0]) + "</td>")
			print("<td>" + str(y[1]) + "</td>")
			print("<td>" + str(y[2]) + "</td>")
			print("<td>" + str(y[3]) + "</td>")
			print("</tr>")
		print("</table>")
		print("<hr />")
		print("</div>")

	elif reportType == 'timeOfYear':
		print("<form method=\"post\" enctype=\"multipart/form-data\" action=\"datawarehouse.py\">")
		print("<label for=\"reportType\">Report Type: </label>")
		print("<select name=\"reportType\" id=\"reportType\" class=\"select form-control-sm\" value=\"" + reportType + "\">")
		print("<option value=\"multiCar\">Multiple Cars in Shop</option>")
		print("<option value=\"numberOfServices\">Number of Services per Car</option>")
		print("<option value=\"mostUsed\">Most Used Services</option>")
		print("<option value=\"timeOfYear\" selected>Service Times of Year</option>")
		print("<option value=\"averageCount\">Average Customer Count</option>")
		print("<option value=\"annualSpend\">Annual Average Spend</option>")
		print("</select>")
		print("<input type=\"hidden\" name=\"report\" id=\"report\" />")
		print("<input type=\"hidden\" name=\"userName\" id=\"userName\" value=\"" + userName + "\" />")
		print("<input type=\"hidden\" name=\"password\" id=\"password\" value=\"" + password + "\" />")
		print("<button type=\"submit\" class=\"btn btn-primary\">Request Report</button>")
		print("</form>")

		cursorb = cnx.cursor()
		cursorb.execute(timeOfYear)
		rowb = cursorb.fetchall()

		print("<div class=\"card-body\">")

		#Multicar
		print("<div>")
		print("<h4>Service Times of Year</h4>")
		print("<table style=\"width:50rem;\" class=\"table-bordered\"><tr>")
		print("<th>service_id</th>")
		print("<th>service_name</th>")
		print("<th>year</th>")
		print("<th>month</th>")
		print("<th>day</th>")
		print("<th>number of times used</th>")
		print("</tr>")
		for y in rowb:
			print("<tr>")
			print("<td>" + str(y[0]) + "</td>")
			print("<td>" + str(y[1]) + "</td>")
			print("<td>" + str(y[2]) + "</td>")
			print("<td>" + str(y[3]) + "</td>")
			print("<td>" + str(y[4]) + "</td>")
			print("<td>" + str(y[5]) + "</td>")


			print("</tr>")
		print("</table>")
		print("<hr />")
		print("</div>")

	elif reportType == 'averageCount':
		print("<form method=\"post\" enctype=\"multipart/form-data\" action=\"datawarehouse.py\">")
		print("<label for=\"reportType\">Report Type: </label>")
		print("<select name=\"reportType\" id=\"reportType\" class=\"select form-control-sm\" value=\"" + reportType + "\">")
		print("<option value=\"multiCar\">Multiple Cars in Shop</option>")
		print("<option value=\"numberOfServices\">Number of Services per Car</option>")
		print("<option value=\"mostUsed\">Most Used Services</option>")
		print("<option value=\"timeOfYear\">Service Times of Year</option>")
		print("<option value=\"averageCount\" selected>Average Customer Count</option>")
		print("<option value=\"annualSpend\">Annual Average Spend</option>")
		print("</select>")
		print("<input type=\"hidden\" name=\"report\" id=\"report\" />")
		print("<input type=\"hidden\" name=\"userName\" id=\"userName\" value=\"" + userName + "\" />")
		print("<input type=\"hidden\" name=\"password\" id=\"password\" value=\"" + password + "\" />")
		print("<button type=\"submit\" class=\"btn btn-primary\">Request Report</button>")
		print("</form>")
		cursorb = cnx.cursor()
		cursorb.execute(averageCount)
		rowb = cursorb.fetchall()

		print("<div class=\"card-body\">")

		#Multicar
		print("<div>")
		print("<h4>Average Customer Count</h4>")
		print("<table style=\"width:50rem;\" class=\"table-bordered\"><tr>")
		print("<th>year</th>")
		print("<th>month</th>")
		print("<th>average_number_of_customers</th>")
		print("</tr>")
		for y in rowb:
			print("<tr>")
			print("<td>" + str(y[0]) + "</td>")
			print("<td>" + str(y[1]) + "</td>")
			print("<td>" + str(y[2]) + "</td>")


			print("</tr>")
		print("</table>")
		print("<hr />")
		print("</div>")

	else:
		print("<form method=\"post\" enctype=\"multipart/form-data\" action=\"datawarehouse.py\">")
		print("<label for=\"reportType\">Report Type: </label>")
		print("<select name=\"reportType\" id=\"reportType\" class=\"select form-control-sm\" value=\"" + reportType + "\">")
		print("<option value=\"multiCar\">Multiple Cars in Shop</option>")
		print("<option value=\"numberOfServices\">Number of Services per Car</option>")
		print("<option value=\"mostUsed\">Most Used Services</option>")
		print("<option value=\"timeOfYear\">Service Times of Year</option>")
		print("<option value=\"averageCount\">Average Customer Count</option>")
		print("<option value=\"annualSpend\" selected>Annual Average Spend</option>")
		print("</select>")
		print("<input type=\"hidden\" name=\"report\" id=\"report\" />")
		print("<input type=\"hidden\" name=\"userName\" id=\"userName\" value=\"" + userName + "\" />")
		print("<input type=\"hidden\" name=\"password\" id=\"password\" value=\"" + password + "\" />")
		print("<button type=\"submit\" class=\"btn btn-primary\">Request Report</button>")
		print("</form>")
		#annualSpend
		cursorb = cnx.cursor()
		cursorb.execute(annualSpend)
		rowb = cursorb.fetchall()

		print("<div class=\"card-body\">")

		#Multicar
		print("<div>")
		print("<h4>Annual Average Spend</h4>")
		print("<table style=\"width:50rem;\" class=\"table-bordered\"><tr>")
		print("<th>year</th>")
		print("<th>average spending</th>")
		print("</tr>")
		for y in rowb:
			print("<tr>")
			print("<td>" + str(y[0]) + "</td>")
			print("<td>" + str(y[1]) + "</td>")


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
