import cgi
import yate
import digeratmodel

digerats=digeratmodel.get_from_store()

form_data=cgi.FieldStorage()
digerat_name=form_data["which_digerat"].value

print(yate.start_response())
print("<html>")
print("<head>")
print("<title>LIST OF DIGERATS</title>")
print("</head>")
print("<body>")
print('<h1 style="color:red;">DIGERAT: ' + digerat_name.upper() +"</h1>")
print(yate.para("This is the Biography of Digerat " + digerat_name))
if digerat_name=='melsy':
	print('<img src="/data/melsy.png"')
elif digerat_name=='david':
	print('<img src="/data/david.png"')
else:
	print('<img src="/data/enock.png"')
print('</br>')
print('<p><a href="/index.html">Home</a></p>')
print('<p><a href="list.py">select another athlete</a></p>')
print("</body>")
print("</html>")
      
