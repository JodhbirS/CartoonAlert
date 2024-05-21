from config import client, r

def send_message(cartoon_url):
    phone_numbers = r.smembers('phone_numbers')
    for phone_number in phone_numbers:
        message = client.messages.create(
            to = phone_number.decode('utf-8'),
            from_= '+12097200651',
            body= f'New cartoon available! {cartoon_url}'
        )