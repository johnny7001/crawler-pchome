import requests
from bs4 import BeautifulSoup
import json
from pandas import json_normalize
# 爬取家樂福網站商品, switch為例
# 一頁以24為單位, start=0, 24, 36...也可以抓取總頁數再跑迴圈
url = 'https://online.carrefour.com.tw/zh/search/?q=switch&start=24#'
main_url = 'https://online.carrefour.com.tw/'

data_dict = {}
# 存放各商品字典
data_list = []

r = requests.get(url)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')
items = soup.find_all('div', class_='hot-recommend-item line')
for item in items:
    prod_dict = {}
    # 商品名稱
    item_name = item.find('div', class_='commodity-desc').find('a').text
    prod_dict['name'] = item_name
    # print(item_name)
    # 商品價格
    item_price = item.find(
        'div', class_='current-price').text.replace('$', '').replace(',', '')
    prod_dict['price'] = item_price
    # print(item_price)
    # 商品圖片
    item_img = item.find('img', class_='m_lazyload').get('src')
    prod_dict['item_img'] = item_img
    # print(item_img)
    # 商品鏈結
    item_url = main_url + \
        item.find('a', class_='gtm-product-alink').get('href')
    prod_dict['url'] = item_url
    # print(item_url)
    # print('='*100)
    data_list.append(prod_dict)

data_dict['Results'] = data_list
# 將 dict 轉成 json
data_json = json.dumps(data_dict, indent=4, ensure_ascii=False)
# 將json寫成檔案
with open('Carrefour_switch.json', 'w', encoding='utf-8') as f:
    f.write(data_json)

# 將json轉成dataFrame,
info = json.loads(data_json)
df = json_normalize(info['Results'])
print(df)


# payload = {'pid': '4413348200101%2C4413111500201%2C4413111500101%2C4413316900101%2C4413301900101%2C4413313500101%2C4413347200101%2C4413337000101%2C4413320100101%2C4413334300101%2C4413305500101%2C4413309800101%2C4413443600101%2C4413339000101%2C4413444200101%2C4413443800101%2C4413459100101%2C4413456900101%2C4413323000101%2C4413457200101%2C4413109400101%2C4413339200101%2C4413341800101%2C4413334800101&sid=108'}
# url = "https://online.carrefour.com.tw/on/demandware.store/Sites-Carrefour-Site/default/Product-StockValidate?pid=4413348200101%2C4413111500201%2C4413111500101%2C4413316900101%2C4413301900101%2C4413313500101%2C4413347200101%2C4413337000101%2C4413320100101%2C4413334300101%2C4413305500101%2C4413309800101%2C4413443600101%2C4413339000101%2C4413444200101%2C4413443800101%2C4413459100101%2C4413456900101%2C4413323000101%2C4413457200101%2C4413109400101%2C4413339200101%2C4413341800101%2C4413334800101&sid=108"
# header = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
#     'referer': 'https://online.carrefour.com.tw/zh/search/?q=switch',
#     'x-requested-with': 'XMLHttpRequest'
# }
# r = requests.get(url, headers=header, params=payload)
# r.encoding = 'utf-8'
# # data = r.text
# rawData = r.json()
# prod_data = rawData['data']
# # 拿到
# prod_idList = prod_data['id'].replace('%2C', ',').split(',')  # type = list
