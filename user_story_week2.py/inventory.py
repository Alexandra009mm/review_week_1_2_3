from funtions import mostrar_menu as mn
import time
import subprocess
import os 

def clear():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)

def write(mensaje):
    for letra in mensaje:
        print(letra, end='', flush=True)
        time.sleep(0.06)
    print()
write("\n--- INVENTARY SISTEM ---")

ejecutar = "ejecutar"

inventory = {} 
c_id =1 
total_price = 0
total_product = 0
total_quantity = 0
total_general = total_price * total_quantity

while ejecutar:

    mn("Add product", "Show inventory"," Calculate statistics","exit")
    roll = "si"

    try:
        op = int(input("Enter a option: "))

        if op not in (1,2,3,4):
            print("Error: incorrect option .Try again.")
            continue
    except ValueError:
        
        clear()
        print("------")
        print("Error. Try again") 
        print("\n------")
        
        continue


    if op == 1:
        clear()
      
        print("You chose option 1 => ")

        while roll:
            try:
               
                product_name = input("Enter the product name: ")
                print("------")
                price = float(input("Enter a price c/u:  "))
                print("------")
                quantity = int(input("Enter a quantity: "))
                print("\n")

            except ValueError: 
                clear()
                print("Error, read well :/")    
                continue

            inventory[c_id] = {"produc name": product_name ,
                "price": price, 
                "quantity": quantity}
            c_id += 1


            try:
                ask = input("Do you want to add another product? yes/no: ").lower()
        
                if ask not in ("yes","no"):
                        print("ERROR! Try again.")

            except ValueError:
                print("ERROR! Try again.")


            if ask == "yes":
                print("OK, Let's add another product! :D =>")
                continue

            elif  ask == "no":
                print("The product was successfully added!")
                roll = False
                continue

    elif op == 2:
         clear()
         print("You chose option 1 => ")
         print(inventory)

    elif op == 3:
        while roll:
            clear()
            write("\n--- SUBMENU STADISTICS ---")
            mn("View Total Inventory Value","View Average Price View Leading","View Leading Product ")
        try:
            ask = int(input("What do you want to see?")).lower()

            if ask not in (1,2,3,4):
                    print("ERROR! Try again.")

        except ValueError:
            print("ERROR! Try again.")

            if ask == 1:  
                suma_total = 0
                for id_prod in inventory:
                    # Entramos a cada producto y multiplicamos
                    precio = inventory[id_prod]["price"]
                    cantidad = inventory[id_prod]["quantity"]
                    suma_total += (precio * cantidad)
                
                print(f"\n>>> The total value of your inventory is: ${suma_total:,.2f}")
                input("\nPress Enter to continue...")


            # resultado
            # roll = False

            # elif ask == 2:
            #     resultado
            
            #     roll = False

            # elif ask ==3: 
            #     resultado
            #     roll = False


            #     continue



    elif op == 4:
        ejecutar = False
        print("Thank you for used the register sistem")

    else:
        
        print("ERROR! enter a correct value. Try again.")
        continue