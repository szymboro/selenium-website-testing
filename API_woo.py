from woocommerce import API
from urllib.parse import urlencode
import time
consumer_key = "REST_API"
consumer_secret = "REST_API_secret"

wcapi = API(
    url="http://IP/",
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    version="wc/v3",
    wp_api=True,
    query_string_auth=True,
    timeout=10,
    key_permissions = "read"
)
get_orders = wcapi.get("orders")

def orders():
    if get_orders != '0':
        time.sleep(1)
    else:
        print("new order found!")

def orders_wait():
    if get_orders != '0':
        time.sleep(1)
while True:
    orders()
    if not orders_wait(): break

print("OK Goodbye...")
