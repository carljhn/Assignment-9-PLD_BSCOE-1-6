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
#Personal Info
cjzoleta.cell(60, 6, "PERSONAL INFORMATION", 0, 2)
cjzoleta.set_font("Arial", "", 12)
cjzoleta.cell(20, 6, "          Age                        :  " +str(myData["PERSONAL INFORMATION"][0]["Age"]), 0, 2)               
cjzoleta.cell(20, 6, "          Birthdate                : " +str (myData["PERSONAL INFORMATION"][0]["Birthday"]), 0, 2)
cjzoleta.cell(20, 6, "          Birthplace               : " +str(myData["PERSONAL INFORMATION"][0]["Birthplace"]), 0, 2)        
cjzoleta.cell(20, 6, "          Sex                         : " +str(myData["PERSONAL INFORMATION"][0]["Sex"]), 0, 2)
cjzoleta.cell(20, 6, "          Marital Status         : " +str(myData["PERSONAL INFORMATION"][0]["Marital Status"]), 0, 2)
cjzoleta.cell(20, 6, "          Nationality              : " +str(myData["PERSONAL INFORMATION"][0]["Nationality"]), 0, 2)
cjzoleta.cell(60, 6,"-"*133, 0, 2)
#Objective
cjzoleta.set_font("Arial", "B", 14)
cjzoleta.cell(60, 10, "OBJECTIVE", 0, 2)
cjzoleta.set_font("Arial", "", 12)
cjzoleta.multi_cell(180, 6, "" +str(myData["OBJECTIVE"][0]), 0)
cjzoleta.cell(60, 7,"-"*133, 0, 2)
#Educaitional Background
cjzoleta.set_font("Arial", "B", 14)
cjzoleta.cell(60, 10, "EDUCATIONAL BACKGROUND", 0, 2)
cjzoleta.set_font("Arial", "B", 13)
cjzoleta.cell(20, 10, "Tertiary", 0, 2)
cjzoleta.cell(20, 6, "         " +str(myData["EDUCATIONAL BACKGROUND"][0]["TertiarySchool"]), 0, 2)
cjzoleta.set_font("Arial", "", 12)
cjzoleta.cell(20, 6, "          " +str(myData["EDUCATIONAL BACKGROUND"][0]["TertiaryCourse"]), 0, 2)
cjzoleta.cell(20, 6, "          " +str(myData["EDUCATIONAL BACKGROUND"][0]["TertiaryAddress"]), 0, 2)
cjzoleta.cell(20, 6, "          " +str(myData["EDUCATIONAL BACKGROUND"][0]["TertiaryYear"]), 0, 2)
cjzoleta.set_font("Arial", "B", 13)
cjzoleta.cell(20, 10, "Secondary", 0, 2)
cjzoleta.cell(20, 6, "         " +str(myData["EDUCATIONAL BACKGROUND"][0]["SecondarySchool"]), 0, 2)
cjzoleta.set_font("Arial", "", 12)
cjzoleta.cell(20, 6, "          " +str(myData["EDUCATIONAL BACKGROUND"][0]["SecondaryLevel"]), 0, 2)
cjzoleta.cell(20, 6, "          " +str(myData["EDUCATIONAL BACKGROUND"][0]["SecondaryAddress"]), 0, 2)
cjzoleta.cell(20, 6, "          " +str(myData["EDUCATIONAL BACKGROUND"][0]["SecondaryYear"]), 0, 2)
cjzoleta.set_font("Arial", "B", 13)
cjzoleta.cell(20, 10, "Primary", 0, 2)
cjzoleta.cell(20, 6, "         " +str(myData["EDUCATIONAL BACKGROUND"][0]["PrimarySchool"]), 0, 2)
cjzoleta.set_font("Arial", "", 12)
cjzoleta.cell(20, 7, "          " +str(myData["EDUCATIONAL BACKGROUND"][0]["PrimaryLevel"]), 0, 2)
cjzoleta.cell(20, 7, "          " +str(myData["EDUCATIONAL BACKGROUND"][0]["PrimaryAddress"]), 0, 2)
cjzoleta.cell(20, 7, "          " +str(myData["EDUCATIONAL BACKGROUND"][0]["PrimaryYear"]), 0, 2)
cjzoleta.add_page()
cjzoleta.cell(60, 7,"-"*133, 0, 2)
#Skills
cjzoleta.set_font("Arial", "B", 14)
cjzoleta.cell(60, 10, "SKILLS", 0, 2)
cjzoleta.set_font("Arial", "", 12)
cjzoleta.cell(20, 6, "          " +str(myData["SKILLS"][0]["Skill_1"]), 0, 2)
cjzoleta.cell(20, 6, "          " +str(myData["SKILLS"][0]["Skill_2"]), 0, 2)
cjzoleta.cell(20, 6, "          " +str(myData["SKILLS"][0]["Skill_3"]), 0, 2)
cjzoleta.cell(20, 6, "          " +str(myData["SKILLS"][0]["Skill_4"]), 0, 2)
cjzoleta.cell(60, 7,"-"*133, 0, 2)
#Language Spoken
cjzoleta.set_font("Arial", "B", 14)
cjzoleta.cell(60, 10, "LANGUAGES SPOKEN", 0, 2) 
cjzoleta.set_font("Arial", "", 12)
cjzoleta.cell(20, 7, "          " +str(myData["LANGUAGES SPOKEN"]["Language_1"]), 0, 2)
cjzoleta.cell(20, 7, "          " +str(myData["LANGUAGES SPOKEN"]["Language_2"]), 0, 2)
