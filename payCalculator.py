def calculatePay():
    # This first line is provided for you
    hrs = input("Enter Hours: ")
    
    try:
        hrs = float(hrs)
        rate = input("Enter Rate: ")
        try:
            rate = float(rate)
            
            if hrs > 40:
                overtime = float(hrs - 40)
                pay = (40 * rate) + (rate * 1.5 * overtime)
            else:
                pay = hrs * rate
            
            print(f"Pay: {pay}")
        
        except:
            print("Error, please enter numeric input")
    except:
        print("Error, please enter numeric input")
    
    
    
    
    


    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
