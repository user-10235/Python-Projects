import os, time


app = True
val = True
text = "Countdown Timer\n1.) Start Timer\n2.) Close"

def run(app):
    val = True
    text = "Countdown Timer\n1.) Start Timer\n2.) Close"

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def window(val,text):
        if val:
            os.system("cls")
            print(text)
            user = input("Enter Option --> ")
            return user

    def timer(start):
        end = start*60
        dt = time.time()
        temp = 0
        ending = end
        while ending > 0:
            start = time.time() - dt
            ending = end - int(start)
            if ending != temp:
                os.system("cls")
                temp = ending
                print("    Countdown Running")
                print("time ---->  "+str(ending//60)+" : "+str(ending%60)+"  <----")
            

    def countdown(val):
        while(val):
            os.system("cls")
            print("Enter the Time up to 2 Hours.")
            count = input("Please Enter the Time in Minutes. --> ")
            number = is_number(count)
            if number:
                if int(count) > 0 and int(count) <= 120:
                    timer(int(count))
                input("Time is up. --> ")
                val = False
            else:
                input("Invalid Selection")
        
    while app:
        choice = window(val,text)
        if choice == "1":
            countdown(True)
        elif choice == "2":
            app = False
        else:
            input("Invalid Selection")


run(True)