import requests

#https://api.telegram.org/botXXXX:YYYYY/getUpdates

token = '' # get token from tokens.txt
def broadcastMessage(listOfGroups, message):
    for groupToSend in listOfGroups:
        URL = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token, groupToSend, message)
        resp = requests.get(URL)
        print(resp.text)


gorda_id = input('What is your Telegram id given by the bot?\n')

groups = ['-577681397', '-553627771']
privateChat = ['1766671538']

privateChat.append(gorda_id)

#message = "Testing the Python script to broadcast a message"
message = "Testing the Python script to send a private message"

broadcastMessage(privateChat, message)

print("Done")