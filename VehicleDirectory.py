class Vehicle:      #vehicle class
    def _init_(self, number, make, model, year, vin, value, dealer):
        self.number = number
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.value = value
        self.dealer = dealer

m = []      #instances are stored here


def Choosevehicle(action):
    global num
    num = 0
    while True:
        num = raw_input("Which vehicle number would you like to %s? \nType 'menu' to return to the main menu. " %action)

        if num.isdigit() == False:
            if num == 'menu':
                menu()
            else:
                print "Invalid input"
                
                    
        elif num.isdigit() == True:
            if int(num) <= len(m):
                return int(num)
                False
                break
                
            else:
                print "Invalid Input"
    
        

def Displaydirec(): 
    for i in m:     #print entire directory
            print "Vehicle: # %d" %i.number 
            print "Make: ", i.make
            print "Model: ",i.model
            print "Year: %d" %i.year
            print "VIN: ", i.vin
            print "Value: $%.2f" %i.value
            print "Dealer: %s\n" %i.dealer

def Display(i):     #display one vehicle
    print "Vehicle: # %d" %i.number 
    print "Make: ", i.make
    print "Model: ",i.model
    print "Year: %s" %i.year
    print "VIN: ", i.vin
    print "Value: $%.2f" %i.value
    print "Dealer: %s\n" %i.dealer

def addVehicle():   #add vehicle to inventory
    
        new = Vehicle()
        new.number = len(m)+1
        print "This is vehicle number %d in the inventory" %new.number
        new.make = raw_input("What is the make of the vehicle? ")
        new.model = raw_input("What is the model of the vehicle? ")
        new.year = input("What is the year of the vehicle? ")
        new.vin = int(input("What is the VIN of the vehicle? "))
        new.value = float(input("What is the value of the vehicle? "))
        new.dealer = raw_input("Which dealership is the vehicle located at? ")
        m.append(new)
        print "A %d %s %s has been added to the directory." %(new.year, new.make, new.model)

def Updatevehicle():
    if len(m) == 0:
        print "No vehicles in directory. Please add a vehicle first."
        menu()
    
    num = Choosevehicle("update")

    Display(m[int(num)-1])
    #print [Display(i) for i in m if i.number == num]   #show you the vehicle you selected
    
    while True:
        cat = (raw_input("Which category would you like to update?\n'Menu' to return to the main menu. ")).lower()
        if cat == 'menu':
            menu()
        elif cat == 'make':
            print "The current make is ", m[(num)-1].make
            m[(num)-1].make = raw_input("What is the new value? ")
        elif cat == 'model':
            print "The current model is ", m[(num)-1].model
            m[(num)-1].model = raw_input("What is the new value? ")
        elif cat == 'year':
            print "The current year is ", m[(num)-1].year
            m[(num)-1].year = raw_input("What is the new value? ")
        elif cat == 'vin':
            print "The current vin is ", m[(num)-1].vin
            m[(num)-1].vin = raw_input("What is the new value? ")
        elif cat == 'value':
            print "The current value is ", m[(num)-1].value
            m[(num)-1].value = float(raw_input("What is the new value? "))
        elif cat == 'dealer':
            print "The current dealer is ", m[(num)-1].dealer
            m[(num)-1].dealer = raw_input("What is the new value? ")
        else:
            print "Please enter a valid category or type 'menu' to return to the main menu."
        #print "The current %s value is %d." %(cat, m[(num)-1].cat) #How to input class instance variable?



        print "Success. The new directory item is:"
        Display(m[(num)-1])
    menu()


def Deletevehicle():
    
    x = Choosevehicle("delete")

    Display(m[(x - 1)])

    y = raw_input("Are you sure you want to delete vehicle #%s? " %m[(x-1)].number)

    if y == 'y' or 'yes':
        del m[(x-1)]

def menu():         #main menu
    while True:
        print "      Main Menu\n"
        print "1. Display Inventory\n"
        print "2. Add to Inventory\n"
        print "3. Update a Vehicle\n"
        print "4. Delete from Inventory\n"
        print "5. Sort Inventory by VIN\n"
        print "6. Search inventory by Model\n"
        print "7. Read inventory from file\n"
        print "8. Write inventory to file and exit\n"
        choice = raw_input("Type the number of what you would like to do. ")
        
        if choice == '1':
            if len(m) == 0:
                print "Error.  No vehicles in directory."  #Error checking
                menu()
            Displaydirec()
            back = raw_input("Type 'menu' to return to the main menu ")
            if back == "menu":
                menu()
            else:
                back = raw_input("invalid input")
                
        elif choice == '2':
            addVehicle()
            menu()

        elif choice == '3':
            Displaydirec()
            Updatevehicle()

        elif choice == '4':
            Displaydirec()
            Deletevehicle()

        elif choice == '8':
            
            with open('VehicleInventory.txt', 'w') as open_file:
        
                for i in m:
                    open_file.write("Vehicle #:")
                    open_file.write(str(i.var))
                    open_file.write("\n")
                    open_file.write("Make: ")
                    open_file.write(str(i.make))
                    open_file.write("\n")
                    open_file.write("Model: ")
                    open_file.write(str(i.model))
                    open_file.write("\n")
                    open_file.write("Year: ")
                    open_file.write(str(i.year))
                    open_file.write("\n")
                    open_file.write("Value: ")
                    open_file.write(str(i.value))
                    open_file.write("\n")
                    open_file.write("Dealer: ")
                    open_file.write(str(i.dealer))
                    open_file.write("\n")
                    open_file.write("\n")
            
        else:
            print "Invalid choice."
            continue
    

        
        
    
        
menu()
