import time
from pages_parsing import tongcheng_url_list

while True:
    print(tongcheng_url_list.find().count())
    time.sleep(5)