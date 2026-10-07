import time

def asking():
    while True:
        try:
            print()
            print("Press 1 for Celsius to Fahrenheit.")
            print("Press 2 for Fahrenheit to Celsius.")
            print("Press 'q' for exit.")

            ask = input("Enter input: ")
            print()

            if ask.strip().lower()=='q':
                print("program ended")
                break

            elif int(ask)>2 or int(ask)<1:
                print("Enter a valid input")
                continue

            elif int(ask) ==1:
                print("You choose Celsius to Fahrenheit")
                c_to_f()

            elif int(ask) ==2:
                print("You choose Fahrenheit to Celcius")
                f_to_c()
        except Exception:
            print("Enter a valid input")

def c_to_f():
    num = int(input("Enter value: "))
    formula = (num*(9/5)+32)
    print(f"Temperature is {formula:.2f}°F")
    time.sleep(2.7)

def f_to_c():
    num = int(input("Enter value: "))
    formula = (num-32)*(5/9)
    print(f"Temperature is {formula:.2f}°C")
    time.sleep(2.7)

if __name__ =="__main__":
    asking()