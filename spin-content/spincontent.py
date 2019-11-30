# built-in function 
# (pip install googletrasns) Cammand for install google trasnslate 



from googletrans import Translator # Import Translator 
translator = Translator() # Set As Variable 
def Spin(abc): 
    a = translator.translate(abc, dest = 'en') # dest = Language to transale & abc is Content ex: en = english
    b = translator.translate(a.text, dest = 'fr') # a.text for fetch only text 
    c = translator.translate(b.text, dest = 'de')
    d = translator.translate(c.text, dest = 'it')
    e = translator.translate(d.text, dest = 'es')
    f = translator.translate(e.text, dest = 'en')
    print("Spin Text : " + f.text) # final conetent print

text = input("Enter Text: ")

Spin(text)



