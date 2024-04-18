import yate
import glob

import digeratmodel

data_files=glob.glob("C:/Users/kenneth/Desktop/DIGERATI/data/*.png")
digerati=digeratmodel.put_to_store(data_files)

print(yate.start_response())
print("<html>")
print("<head>")
print("<title>LIST OF DIGERATS</title>")
print("</head>")
print("<body>")
print('<h1 style="color:red;">LIST OF DIGERATS</h1>')
print(yate.start_form("bio.py"))
print(yate.para("select a digerat to veiw bio"))

for each_digerat in digerati:
    print(yate.radio_button("which_digerat", each_digerat))
print(yate.end_form("select"))
print('<p><a href="/index.html">Home</a></p>')
print("</body>")
print("</html>")
      