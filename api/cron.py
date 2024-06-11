#!/usr/bin/env python3
import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import get_cartoon
import send_cartoon

def handler(req, res):
    cron_secret = os.getenv('CRON_SECRET')
    authorization_header = req.headers.get('Authorization')

    if authorization_header != f"Bearer {cron_secret}":
        return res.status(401).send('Unauthorized')
    
    cartoon_url, cartoon_date = get_cartoon.get_latest_cartoon()
    print(cartoon_url, cartoon_date)
    
    if cartoon_date and get_cartoon.is_new_cartoon(cartoon_date):
        send_cartoon.send_message(cartoon_url)
    
    res.status(200).send("Cron job executed successfully.")

if __name__ == "__main__":
    handler()