import time

def asking():
    while True:
        try:
            print()
            print("Press 1 for Celsius to Fahrenheit.")
            print("Press 2 for Fahrenheit to Celsius.")
            print("Press 3 for kmph to knots.")
            print("Press 4 for knots to kmph.")
            print("Press 'q' for exit.")

            ask = input("Enter input: ")
            print()

            if ask.strip().lower()=='q':
                print("program ended")
                break

            elif int(ask)>=5 or int(ask)<1:
                print("Enter a valid input")
                time.sleep(2)
                continue

            elif int(ask) ==1:
                print("You choose Celsius to Fahrenheit")
                c_to_f()

            elif int(ask) ==2:
                print("You choose Fahrenheit to Celcius")
                f_to_c()

            elif int(ask) ==3:
                print("You choose kmph to knots")
                kmph_to_knots()

            elif int(ask) ==4:
                print("You choose knots to kmph")
                knots_to_kmph()

        except Exception:
            print("Enter a valid input")
            time.sleep(2)

def c_to_f():
    num = float(input("Enter value: "))
    formula = (num*(9/5)+32)
    print(f"Temperature is {formula:.2f}°F")
    time.sleep(2.7)

def f_to_c():
    num = float(input("Enter value: "))
    formula = (num-32)*(5/9)
    print(f"Temperature is {formula:.2f}°C")
    time.sleep(2.7)

def kmph_to_knots():
    num = float(input("Enter value: "))
    formula = num/1.852
    print(f"Speed is {formula:.3f} knots")
    time.sleep(2.7)

def knots_to_kmph():
    num = float(input("Enter value: "))
    formula = num*1.852
    print(f"Speed is {formula:.3f} kmph")
    time.sleep(2.7)



if __name__ =="__main__":
    asking()