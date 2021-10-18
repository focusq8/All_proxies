import requests

choose = input("""which kind of proxy do you want:

1 http
2 https
3 sock4
4 sock5
5 all

Choose the Number: """)

if "1" in choose : 
   url = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=yes https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt https://www.proxy-list.download/api/v1/get?type=http https://www.proxyscan.io/download?type=http https://premiumproxy.net/http-proxy-list")
   file_text = open("http_proxy.txt", "w")
   file_text.write(url.text)
   file_text.close()

if "2" in choose : 
   url = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500&ssl=yes https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt https://www.proxy-list.download/api/v1/get?type=https https://www.proxyscan.io/download?type=https https://premiumproxy.net/https-ssl-proxy-list http://free-proxy.cz/en/proxylist/country/all/https/ping/all")
   file_text = open("https_proxy.txt", "w")
   file_text.write(url.text)
   file_text.close()


if "3" in choose : 
   url = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500&ssl=yes")
   file_text = open("sock4_proxy.txt", "w")
   file_text.write(url.text)
   file_text.close()

if "4" in choose : 
   url = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500&ssl=yes")
   f = open("sock5_proxy.txt", "w")
   f.write(url.text)
   f.close()

if "5" in choose : 
   url = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=1500&ssl=yes https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt https://www.proxy-list.download/api/v1/get?type=http https://www.proxyscan.io/download?type=http https://premiumproxy.net/http-proxy-list https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt https://www.proxy-list.download/api/v1/get?type=https https://www.proxyscan.io/download?type=https https://premiumproxy.net/https-proxy-list")
   file_text = open("all_proxy.txt", "w")
   file_text.write(url.text)
   file_text.close()