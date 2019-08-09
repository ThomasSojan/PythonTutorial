start = False

while True:
    command = input(">>").lower()
    if command == "start":
        if start:
            print("car is already started....")
        else:    
            start = True
            print("car is started")
    elif command == "stop":
        if not start:
            print("car is already stopped...")
        else:
            start = False    
            print("car is stopped")
    elif command == "help":
        print("""
start-To start the car
stop- To stop the car
quit- To terminate """)
    elif command == "quit":
        break    
    else:
        print("sorry didn't understand that")
