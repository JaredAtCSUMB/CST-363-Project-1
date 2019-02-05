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
print("<title>JAD - Services</title>")
print("</head>")
print("<body>")
services = 'select * from service'

# connect to database
# IMPORTANT: update this password with your own
dbPassword = 'dbPassword'
cnx = mysql.connector.connect(user='root',
                                password=dbPassword,
                                database='jadautorepair',
                                host='127.0.0.1')


# clicked register
cursor = cnx.cursor()
cursor.execute(services)
row = cursor.fetchall()
# userid and password did not match

print("<div class=\"main-container\">")
print("<div class=\"card main-card\">")
print("<a href=\"../index.html\" class=\"back-btn\">< Go Back</a>")
print("<h1>Browse the Services We Offer</h1>")
print("<div class=\"row justify-content-center\">")
print("<div class=\"card\" >")
print("<img src=\"../images/services.jpg\" class=\"card-img-top\" alt=\"services\">")
print("<div class=\"card-body\">")
print("<!-- TODO: connect services form -->")
print("<table style=\"width:40rem;\"><tr>")
print("<th>SKU/Service #</th>")
print("<th>Name/Description</th>")
print("<th>Price</th>")
print("<th></th>")
print("</tr>")
for x in row:
	print("<tr>")
	print("<td>" + str(x[0]) + "</td>")
	print("<td>" + str(x[1]) + "</td>")
	print("<td>" + str(x[2]) + "</td>")
	print("<td><form action=\"customer.py\" enctype=\"multipart/form-data\" method=\"post\"><button type=\"submit\" class=\"btn btn-secondary\" name=\"addOrder\" id=\"addOrder\" value=\"" + str(x[0]) + "\">Order Now</button></form></td>")
	print("</tr>")
print("</table>")
print("</div>")
print("</div>")
print("</div>")
print("</div>")
print("</div>")
print("<script src=\"https://code.jquery.com/jquery-3.3.1.slim.min.js\" integrity=\"sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo\" crossorigin=\"anonymous\"></script>")
print("<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js\" integrity=\"sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut\" crossorigin=\"anonymous\"></script>")
print("<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js\" integrity=\"sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k\" crossorigin=\"anonymous\"></script>")


print("</body></html>")
cnx.close()
