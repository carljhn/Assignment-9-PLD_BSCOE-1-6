# PDF Resume Creator
# 	- Create a python program that will create your personal resume in PDF format
# 	- All personal details are stored in a JSON file
# 	- Your program should read the JSON file and write the details in the PDF
# 	- The output file should be: LASTNAME_FIRSTNAME.pdf

# Note:
# 	- Search for available PDF library that you can use
# 	- Search how data is structured using JSON format
# 	- Search how to read JSON file
# 	- You will create the JSON file manually
# 	- Your code should be in github before Feb12
from fpdf import FPDF
import json
with open("resume_zoleta.json", "r") as resumeJson:
    myData= json.loads(resumeJson.read())

cjzoleta=FPDF("P", "mm", "Letter")
cjzoleta.add_page() #1st page
cjzoleta.image("profile.jpg", x= 150, y=0, w=45, h=45, type="jpg") #picture
cjzoleta.set_font("Arial", "B", 14)
cjzoleta.cell(60, 10, "ZOLETA, CARL JOHN R.", 0, 1)
cjzoleta.set_font("Arial", "", 12)
cjzoleta.cell(20, 6, "Address: 1280 Sunlight Street, Muzon, San Jose del Monte, Bulacan", 0, 2)
cjzoleta.cell(20, 6, "Contact No.: 0912-345-6789", 0, 2)
cjzoleta.cell(20, 6, "E-mail: zoletacj1@gmail.com", 0, 2)
cjzoleta.cell(60, 15,"-"*133, 0, 2)
cjzoleta.set_font("Arial", "B", 14)
