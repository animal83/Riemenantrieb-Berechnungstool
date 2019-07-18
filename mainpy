from math import pi, sqrt


while True:
    try:
        while True:
            GROSS = eval(input("Anzahl der Zaehne am grossen Rittzel: "))
            if type(GROSS) == int:
                    break
                
        while True:
            KLEIN = eval(input("Anzahl der Zaehne am kleinen Rittzel: "))
            if type(KLEIN) == int:
                break
        
        while True:
            GT = eval(input("Zahn abstand GT: "))
            if type(GT) == int or type(GT) == float:
                break
            
        while True:
            Am = eval(input("Abstand zwischen den Achsen in mm: "))
            if type(Am) == int or type(Am) == float:
                break
            
        break       
     
    except: 
            print("Bitte eine Zahl eingeben") 
            
   
RIL = (2 * sqrt(Am**2+(((GROSS * GT)-(KLEIN * GT))/(2*pi))**2))+(((GROSS * GT)+(KLEIN * GT))/2)

print("\n-----------------------------------------\nDie Riemenlaenge " + str(round(RIL,2)) + "mm")
exit()
