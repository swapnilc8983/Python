# Use built-in function --> googletrasns
# ($ pip install googletrasns) Cammand for install google trasnslate 

from googletrans import Translator # Import Translator 
translator = Translator() # Set As Variable 
def Spin(abc):  
    file = open('spincontent.txt','w') # to Save Spin Conetent in spincontent.txt file
    a = translator.translate(abc, dest = 'en') # dest = Language to transale & abc is Content ex: en = english
    b = translator.translate(a.text, dest = 'fr') # a.text for fetch only text 
    c = translator.translate(b.text, dest = 'de')
    d = translator.translate(c.text, dest = 'it')
    e = translator.translate(d.text, dest = 'es')
    f = translator.translate(e.text, dest = 'en')
    return file.write(f.text) # Output Save
    #print("Spin Text : " + f.text) # final content print

#text = input("Enter Text: ")

#Spin(text)

file = open('content.txt','r') # fro read a original content
Spin(file.read()) # Call spin function
file.close() # file close

