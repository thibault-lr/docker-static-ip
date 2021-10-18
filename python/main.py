import requests
from stem import Signal
from stem.control import Controller
from stem.util.log import get_logger

from urllib3 import disable_warnings as url3_disable_warnings

class ErrorIpRenewException(Exception):
    pass


import time 
time.sleep(10)
class Fetcher:
    def __init__(self):
        url3_disable_warnings()

        self.http = requests.Session()
        self.http.proxies = {}

        logger = get_logger()
        logger.propagate = False


    def add_proxies(self):
        self.http.proxies['http'] = 'socks5://172.18.18.10:9051'
        self.http.proxies['https'] = 'socks5://172.18.18.10:9051'

    def renew_proxy_ip(self):
        with Controller.from_port(port=10001, address="172.18.18.10") as controller:
            controller.authenticate(password="testtor")
            print("Authentication :: ", controller.is_authenticated())
            controller.signal(Signal.NEWNYM)

    def fetchData(self, url):
        
        try:
            req = self.http.get(
                "https://ifconfig.io/ip")
            print("After request :: ", url, req.status_code, req.text)

            req.raise_for_status()
        except Exception as err:
            print(err)


fetcher = Fetcher()


fetcher.fetchData("https://ifconfig.io/ip")
fetcher.add_proxies()
fetcher.fetchData("https://ifconfig.io/ip")
fetcher.renew_proxy_ip()
fetcher.fetchData("https://ifconfig.io/ip")
