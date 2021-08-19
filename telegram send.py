import telegram_send

while(1):
    number = int(input("Enter a number: "))
    if(number == 0):
        telegram_send.send(messages=["Doing tests"])
        break

    elif number == 1:
        print("User entered 1")

    else:
        break