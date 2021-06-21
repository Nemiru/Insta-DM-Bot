from instadm import InstaDM
import time
import schedule


with open(r'users.txt', 'r') as f:
    users = [line.strip() for line in f]

print(users)

# Auto login
insta = InstaDM(username='ma@gmail.com', password='Bi20', headless=False)

def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


def msg():
    for user in users:  
        # Send message
        insta.sendMessage(user=user, message="Hi hope you're well,"
"I'm Clive from Matrix Epos.")
        
### message sent everyday at 01:05
### 24 HH:MM format
schedule.every().day.at("01:05").do(msg)



if __name__ == '__main__':
    msg()
    scheduler()

