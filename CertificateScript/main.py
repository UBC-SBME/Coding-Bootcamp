#Should populate the OUT folder with all certificates. If grades list updates, just replace the
#CSV and rerun. It won't make duplicates of any certificate it has already made


from PIL import Image, ImageFont, ImageDraw
import pandas as pd
from pdf2image import convert_from_path

yearFont = ImageFont.truetype("IN/OpenSans-Bold.ttf", 30)
nameFont = ImageFont.truetype("IN/OpenSans-Bold.ttf", 100)

def modifyImage(year, name):
    image = convert_from_path("IN/BASE.pdf", size = (2000,1414))[0].convert("RGB")
    #image = Image.open("IN/BASE.png").convert("RGB")
    edit = ImageDraw.Draw(image)
    #The placement of the year and name I got with trial and error
    #If you make a new certificate, you will probably have to change this too.
    edit.text((370,451), year,fill =(192,33,47), font = yearFont)
    edit.text((135,560), name, fill = (0,0,0), font = nameFont)
    filePath = "OUT/" + name + " 2023 CBC Certificate.pdf"
    image.save(filePath, format = "pdf")


if __name__ == '__main__':
    grades = pd.read_csv("IN/GRADES.csv")
    projectGrade = grades['Project Code (1546984)'] #this may change, so check the CSV
    names = grades['Student']
    names = [" ".join(n.split(", ")[::-1]) for n in names] #Change from Lname, Fname to Fname Lname
    n = len(names)
    for x in range(1,n):
        if projectGrade[x] == 1:
            modifyImage("2023", names[x]) #CHANGE THE YEAR HERE IF NEEDED
            #print(names[x])