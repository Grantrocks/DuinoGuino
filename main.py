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
      print(Back.BLACK+Fore.WHITE+f"Miner: {miner['identifier']}\nSoftware: {miner['software']}\n"+Fore.GREEN+f"Accepted Shares: {miner['accepted']}\n"+Fore.CYAN+f"Hashrate: {miner['hashrate']}/Hs\n"+Fore.RED+f"Rejected: {miner['rejected']}")
      print("------------------------------------------")
def getbal(username):
  req=requests.get(f'{server}/balances/{username}')
  data=json.loads(req.text)
  result=data['result']
  print(f"Balance: "+Fore.YELLOW+f"{round(result['balance'],5)} ᕲ")
def getnetstats():
  req=requests.get(f'{server}/statistics')
  data=json.loads(req.text)
  print(f"Active Connections: {data['Active connections']}\nAll-time mined DUCO: {data['All-time mined DUCO']}\nCurrent Difficulty: {data['Current difficulty']}\nDUCO-S1 hashrate: {data['DUCO-S1 hashrate']}\nDuco Node-S price: {data['Duco Node-S price']}\nDuco price: {data['Duco price']}\nLast block hash: {data['Last block hash']}\nMined blocks: {data['Mined blocks']}\nPool hashrate: {data['Pool hashrate']}\nRegistered users: {data['Registered users']}\nServer CPU usage: {data['Server CPU usage']}%\nServer RAM usage: {data['Server RAM usage']}%\nServer version: {data['Server version']}")
def gettrans(username):
  print("You can check a transaction with one of the following methods.")
  print("""
        1: Hash
        2: Last 5
        3: Transaction ID
        """)
  option=int(input("Option: "))
  if option==1:
    print("Please provide your transaction hash to look up the transaction.")
    hash=input("Hash: ")
    data=requests.get(f"{server}/transactions/{hash}")
    res=json.loads(data.text)
    result=res['result']
    print(f"From: {result['sender']}\nTo: {result['recipient']}\nAmount: {result['amount']} ᕲ\nTime: {result['datetime']}\nMessage: {result['memo']}\nHash: {result['hash']}\nID: {result['id']}\n-----------------------\n")
  elif option==2:
    req=requests.get(f'{server}/user_transactions/{username}')
    data=json.loads(req.text)
    result=data['result']
    if data['success']:
      for tran in result:
        print(f"From: {tran['sender']}\nTo: {tran['recipient']}\nAmount: {tran['amount']} ᕲ\nTime: {tran['datetime']}\nMessage: {tran['memo']}\nHash: {tran['hash']}\nID: {tran['id']}\n-----------------------\n")
  elif option==3:
    id=input("Transaction ID: ")
    req=requests.get(f"{server}/id_transactions/{id}")
    data=json.loads(req.text)
    result=data['result']
    if data['success']:
      print(f"From: {result['sender']}\nTo: {result['recipient']}\nAmount: {result['amount']} ᕲ\nTime: {result['datetime']}\nMessage: {result['memo']}\nHash: {result['hash']}\nID: {result['id']}\n-----------------------\n")
def wallet(username,password):
  print(Fore.GREEN+f"Welcome Back, {username}")
  while True:
    getbal(username)
    print("""
          1: Send Duino Coin
          2: Miners
          3: Check Transactions
          4: Check Network Stats
          5: Start PC Mining
          6: Update
          7: Donate
          """)
    try:
      action = int(input("Choice: "))
      clearl()
      if action==1:
        print("If you dont want to send a message with the transaction just type None")
        amount=float(input("Amount: "))
        to=input(f"Send {amount} ᕲ To: ")
        message=input("Message: ")
        confirm=input('Confirm Transaction (y/n): ')
        if confirm=="y" or confirm=="Y" or confirm=="yes" or confirm=="YES" or confirm=="Yes":
          sendduco(username,password,to,amount,message)
        else:
          print("Cancelled Transaction")
      elif action==2:
        getminers(username)
      elif action==3:
        gettrans(username)
      elif action==4:
        getnetstats()
      elif action==5:
        os.system('python3 PC_Miner.py')
      elif action==6:
        if os.path.exists('PC_Miner.py'):
          os.unlink('PC_Miner.py')
          os.system('wget https://raw.githubusercontent.com/revoxhere/duino-coin/master/PC_Miner.py')
        else:
          print("Downloading DUCO PC Miner")
          os.system('wget https://raw.githubusercontent.com/revoxhere/duino-coin/master/PC_Miner.py')
      elif action==7:
        print("I created this wallet so that any new or advanced users of Duino Coin could experience a simple and easy to use wallet to manage their Duino Coin. I really hope that anyone that likes this wallet will donate. I am also currently making more tools to use.")
        damount=float(input("Donate Amount: "))
        dmessage=input("Donate Message: ")
        print(f"Donate {damount} ᕲ to the creator with the message: {dmessage}")
        confirm=input("Confirm (y/n): ")
        if confirm=="y" or confirm=="Y" or confirm=="yes" or confirm=="YES" or confirm=="Yes":
          sendduco(username,password,"Grantrocks",damount,dmessage)
        else:
          print(Fore.RED+"Transaction Cancelled")
    except:
      clearl()
      print(Fore.RED+"Invalid Input")
print(Fore.YELLOW+"""
       Duino Guino Wallet Version 1.0
      
             (((((((((((((((((
          (((((((((((((((((((((((
        (((((((           ((((((((
       (((((((((((((((((    ((((((((
       ((((((((         ((    ((((((
       ((((((((((((((((  (((   ((((((
       ((((((((         ((    ((((((
       (((((((((((((((((     (((((((
         ((((((           ((((((((
          (((((((((((((((((((((((
             (((((((((((((((((
      """)
while True:
  username=input("DUCO Username: ")
  password=input("DUCO Password: ")
  user = requests.get(f'https://server.duinocoin.com/auth/{username}?password={password}')
  res=json.loads(user.text)
  if res['success']:
    clearl()
    wallet(username,password)
    break
  else:
    print(Fore.RED+"Incorrect Login Try Again")