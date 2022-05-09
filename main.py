import requests
import json
from colorama import init,Fore,Back,Style
init(autoreset=True)
import os
server="https://server.duinocoin.com"
def clearl():
  os.system('cls' if os.name == 'nt' else 'clear')
def sendduco(username,password,recipient,amount,memo):
  req = requests.get(f'{server}/transaction?username={str(username)}&password={password}&recipient={recipient}&amount={amount}&memo={memo}')
  data=json.loads(req.text)
  result=data['result']
  print(result)
def getminers(username):
  req = requests.get(f'{server}/miners/{username}')
  reqr=json.loads(req.text)
  if reqr['success']:
    data=reqr['result']
    for miner in data:
      print(miner['accepted'])
def getbal(username):
  req=requests.get(f'{server}/balances/{username}')
  data=json.loads(req.text)
  result=data['result']
  print(f"Balance: {result['balance']} DUCO")
def wallet(username,password):
  print(Fore.GREEN+f"Welcome Back, {username}")
  while True:
    getbal(username)
    print("""
          1: Send Duino Coin
          2: Miners
          3: Check Transactions
          4: Check Network Stats
          """)
    try:
      action = int(input("Choice: "))
      if action==1:
        print("If you dont want to send a message with the transaction just type None")
        amount=float(input("Amount: "))
        to=input(f"Send {amount} To: ")
        message=input("Message: ")
        sendduco(username,password,to,amount,message)
      elif action==2:
        getminers(username)
    except:
      print("Invalid Choice")
    
while True:
  username=input("DUCO Username: ")
  password=input("DUCO Password: ")
  user = requests.get(f'https://server.duinocoin.com/auth/{username}?password={password}')
  res=json.loads(user.text)
  print(res)
  if res['success']:
    clearl()
    wallet(username,password)
    break
  else:
    print("Incorrect Login Try Again")