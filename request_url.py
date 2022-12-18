import requests
import time
from threading import Thread
from make_csv import make_csvfile, read_csvfile_last_value

def getUrl():
    return requests.get('https://api.waifu.pics/sfw/waifu')

def interval_getUrl():
    while True:
        time.sleep(0.3)
        make_csvfile(getUrl().json()['url'])

def fasapi_main():
    while True:
        time.sleep(1)
        print(read_csvfile_last_value('urls.csv'))

interval_thread = Thread(target=interval_getUrl, daemon=True)

def getUrl_thread():
    interval_thread.start()

if __name__ == "__main__":
    getUrl_thread()
    fasapi_main()