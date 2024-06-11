import os
import get_cartoon
import send_cartoon

def handler():
    cron_secret = os.getenv('CRON_SECRET')
    
    cartoon_url, cartoon_date = get_cartoon.get_latest_cartoon()
    print(cartoon_url, cartoon_date)
    
    #if cartoon_date and get_cartoon.is_new_cartoon(cartoon_date):
    send_cartoon.send_message(cartoon_url)

if __name__ == "__main__":
    handler()