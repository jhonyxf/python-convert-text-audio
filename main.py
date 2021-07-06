import pyttsx3 
import pdfplumber 
import PyPDF2
import gtts
from playsound import playsound

file = 'artigo.pdf'

#Creating a PDF File Object
pdfFileObj = open(file, 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#Get the number of pages
pages = pdfReader.numPages

text = ''

#Create a pdfplumber object and loop through the pages
with pdfplumber.open(file) as pdf:
 #Loop through the number of pages
    for i in range(0, pages): 
      page = pdf.pages[i]
      text = page.extract_text()
      print(text)
      audio = gtts.gTTS(text, lang='pt-br', slow=False)
      audio.save("hello.mp3")
      #playsound("hello.mp3")
      speaker = pyttsx3.init()
      speaker.save_to_file(text, 'speech.mp3')
      speaker.say(text)
      speaker.runAndWait()
      