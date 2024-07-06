import random
choice = input("Would you like to roll the dice? (y/n) ")

if choice == "y":
    num = random.randint(1, 6)

    if(num == 1):
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("Press y to roll again or n to exit")
        

    if(num == 2):
        print("[0    ]")
        print("[     ]")
        print("[    0]")
        print("Press y to roll again or n to exit")
        

    if(num == 3):
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
        print("Press y to roll again or n to exit")
        

    if(num == 4):
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("Press y to roll again or n to exit")
       

    if(num == 5):
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("Press y to roll again or n to exit")
       
    
    if(num == 6):
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("Press y to roll again or n to exit")
        