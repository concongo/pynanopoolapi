import urllib
import urllib2
import json
import sys

class nanopoolapi:
    __wallet = ''
    __coing = ''

    def __init__(self, wallet, coin):
        self.__wallet = wallet
        self.__coin = coin

    def getbalance(self):
    #Returns the current Balance

        endpoint = 'https://api.nanopool.org/v1/' + self.__coin + '/balance/' + self.__wallet
        headers = {
            'User-agent': 'Mozilla/4.0 (compatible; pynanopoolapi; ' +
                          str(sys.platform) + '; ' + str(sys.version).replace('\n', '') + ')'
        }
        req = urllib2.Request(endpoint, None, headers)
        page = urllib2.urlopen(req).read()
        return json.loads(page)["data"]

    def getaveragehashratelimited(self, hours):
    #Returns the averagehasrate for a time
        endpoint = 'https://api.nanopool.org/v1/' + self.__coin + '/avghashratelimited/' + self.__wallet + '/' + str(hours)
        headers = {
            'User-agent': 'Mozilla/4.0 (compatible; pynanopoolapi; ' +
                          str(sys.platform) + '; ' + str(sys.version).replace('\n', '') + ')'
        }
        req = urllib2.Request(endpoint, None, headers)
        page = urllib2.urlopen(req).read()
        return json.loads(page)["data"]

    def getaveragehashrate(self):
    #Returns the averagehasrate for 1, 3, 6, 12, 24
        endpoint = 'https://api.nanopool.org/v1/' + self.__coin + '/avghashrate/' + self.__wallet
        headers = {
            'User-agent': 'Mozilla/4.0 (compatible; pynanopoolapi; ' +
                          str(sys.platform) + '; ' + str(sys.version).replace('\n', '') + ')'
        }
        req = urllib2.Request(endpoint, None, headers)
        page = urllib2.urlopen(req).read()
        return json.loads(page)["data"]

    def hashrate(self):
        endpoint = 'https://api.nanopool.org/v1/' + self.__coin + '/hashrate/' + self.__wallet
        headers = {
            'User-agent': 'Mozilla/4.0 (compatible; pynanopoolapi; ' +
                          str(sys.platform) + '; ' + str(sys.version).replace('\n', '') + ')'
        }
        req = urllib2.Request(endpoint, None, headers)
        page = urllib2.urlopen(req).read()
        return json.loads(page)["data"]

    def generalinfo(self):
        endpoint = 'https://api.nanopool.org/v1/' + self.__coin + '/user/' + self.__wallet
        headers = {
            'User-agent': 'Mozilla/4.0 (compatible; pynanopoolapi; ' +
                          str(sys.platform) + '; ' + str(sys.version).replace('\n', '') + ')'
        }
        req = urllib2.Request(endpoint, None, headers)
        page = urllib2.urlopen(req).read()
        return json.loads(page)["data"]

    def historyhashrate(self):
        endpoint = 'https://api.nanopool.org/v1/' + self.__coin + '/history/' + self.__wallet
        headers = {
            'User-agent': 'Mozilla/4.0 (compatible; pynanopoolapi; ' +
                          str(sys.platform) + '; ' + str(sys.version).replace('\n', '') + ')'
        }
        req = urllib2.Request(endpoint, None, headers)
        page = urllib2.urlopen(req).read()
        return json.loads(page)["data"]

    def balancehashrate(self):
        #Returns current balance and hashrate
        endpoint = 'https://api.nanopool.org/v1/' + self.__coin + '/balance_hashrate/' + self.__wallet
        headers = {
            'User-agent': 'Mozilla/4.0 (compatible; pynanopoolapi; ' +
                          str(sys.platform) + '; ' + str(sys.version).replace('\n', '') + ')'
        }
        req = urllib2.Request(endpoint, None, headers)
        page = urllib2.urlopen(req).read()
        return json.loads(page)["data"]

    def calculator(self, hashrate):
        # Returns current balance and hashrate
        endpoint = 'https://api.nanopool.org/v1/' + self.__coin + '/approximated_earnings/' + str(hashrate)
        headers = {
            'User-agent': 'Mozilla/4.0 (compatible; pynanopoolapi; ' +
                          str(sys.platform) + '; ' + str(sys.version).replace('\n', '') + ')'
        }
        req = urllib2.Request(endpoint, None, headers)
        page = urllib2.urlopen(req).read()
        return json.loads(page)["data"]

    def prices(self):
        # Returns current balance and hashrate
        endpoint = 'https://api.nanopool.org/v1/' + self.__coin + '/prices'
        headers = {
            'User-agent': 'Mozilla/4.0 (compatible; pynanopoolapi; ' +
                          str(sys.platform) + '; ' + str(sys.version).replace('\n', '') + ')'
        }
        req = urllib2.Request(endpoint, None, headers)
        page = urllib2.urlopen(req).read()
        return json.loads(page)["data"]

    def paymenttimeestimate(self, hours_average):
        hashrate = self.getaveragehashratelimited(hours_average)
        earning_estimate = self.calculator(hashrate)['minute']['coins']
        current_balance = self.getbalance()
        payouts = [1.0, 0.5, 0.25, 0.10, 0.05]
        estimate = {'Minutes':{}, 'Hours':{}, 'Days':{}}
        for p in payouts:
            min_to_pay = (p - current_balance) / earning_estimate
            estimate['Minutes'][str(p)]=min_to_pay
            estimate['Hours'][str(p)]=min_to_pay/60
            estimate['Days'][str(p)]=(min_to_pay/60)/24
        return estimate
