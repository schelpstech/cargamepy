'Car Game'

command = ''
started = False
speed = False
while True:
    new_command = input('Enter New Command : ').lower()

    if new_command == 'start':
        if started == False:
            print('Car started... Lets go')
            started = True
        else:
            print('Car already Started')
    elif new_command == 'speed':
        if started == False:
            print('Car has been stopped. Switch on Car')
        elif started == True and speed != True:
            print('Car Accelerator Pressed. Hold on Tight')
            speed = True
        else:
            print('Car Accelerator Already Pressed. Car Moving at High Speed')
    elif new_command == 'brake':
        if started == False or speed == False:
            print('Car not moving. Brake cannot be activated')
        else:
            print('Brake applied. Car halted')
            speed = False

    elif new_command == 'stop':
        if started != False :
            print('car stopped')
            started = False
        else:
            print('Car already Stopped')
    elif new_command == 'quit':
        print ('Car Game Ended')
        break
    else:
        print('''
Command not recognised ***** 
Enter Start - Start
Enter Brake - brake
Enter Stop - stop''')
else:
    print('Game ended')
