import requests

choose = input("""which kind of proxy do you want:

1 http

2 https

3 sock4

4 sock5

5 all

Choose the Number: """)

if "1" in choose : 
   url = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=yes")
   url2 = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt")
   url3 = requests.get("https://www.proxy-list.download/api/v1/get?type=http")
   url4 = requests.get("https://www.proxyscan.io/download?type=http")
   url5 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt")
   file_text = open("http_proxy.txt", "a")
   file_text.write(url.text.replace('\n\n', ''))
   file_text.write(url2.text.replace('\n\n', ''))
   file_text.write(url3.text.replace('\n\n', ''))
   file_text.write(url4.text.replace('\n\n', ''))
   file_text.write(url5.text.replace('\n\n', ''))
   file_text.close()

if "2" in choose : 
   url = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500&ssl=yes")
   url2 = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt")
   url3 = requests.get("https://www.proxy-list.download/api/v1/get?type=https")
   url4 = requests.get("https://www.proxyscan.io/download?type=https")
   file_text = open("https_proxy.txt", "a")
   file_text.write(url.text.replace('\n\n', ''))
   file_text.write(url2.text.replace('\n\n', ''))
   file_text.write(url3.text.replace('\n\n', ''))
   file_text.write(url4.text.replace('\n\n', ''))
   file_text.close()


if "3" in choose : 
   url = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt")
   url1 = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500&ssl=yes")
   file_text = open("sock4_proxy.txt", "a")
   file_text.write(url.text.replace('\n\n', ''))
   file_text.write(url1.text.replace('\n\n', ''))
   file_text.close()

if "4" in choose :
   url =requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt")
   url1 =requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500&ssl=yes")
   url2 =requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt")
   url3 =requests.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt")
   url4 =requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt")
   url5 =requests.get("https://raw.githubusercontent.com/UserR3X/proxy-list/main/socks4.txt")
   url6 =requests.get("https://www.proxy-list.download/api/v1/get?type=socks4")
   file_text = open("proxies.txt", "a")
   file_text.write(url.text.replace('\n\n', ''))
   file_text.write(url1.text.replace('\n\n', ''))
   file_text.write(url2.text.replace('\n\n', ''))
   file_text.write(url3.text.replace('\n\n', ''))
   file_text.write(url4.text.replace('\n\n', ''))
   file_text.write(url5.text.replace('\n\n', ''))
   file_text.write(url6.text.replace('\n\n', ''))
   file_text.close()

if "5" in choose : 
   url = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=1500&ssl=yes")
   url2 = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt")
   url3 = requests.get("https://www.proxy-list.download/api/v1/get?type=http")
   url4 = requests.get("https://www.proxyscan.io/download?type=http")
   url5 = requests.get("https://premiumproxy.net/http-proxy-list")
   url6 = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt")
   url7 = requests.get("https://www.proxy-list.download/api/v1/get?type=https")
   url8 = requests.get("https://www.proxyscan.io/download?type=https")
   file_text = open("all_proxy.txt", "a")
   file_text.write(url.text.replace('\n\n', ''))
   file_text.write(url2.text.replace('\n\n', ''))
   file_text.write(url3.text.replace('\n\n', ''))
   file_text.write(url4.text.replace('\n\n', ''))
   file_text.write(url5.text.replace('\n\n', ''))
   file_text.write(url6.text.replace('\n\n', ''))
   file_text.write(url7.text.replace('\n\n', ''))
   file_text.write(url8.text.replace('\n\n', ''))
   file_text.close()
