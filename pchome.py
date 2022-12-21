import requests
import json
from pandas import json_normalize

img_url = "https://cs-a.ecimg.tw"
prodMain_url = "https://24h.pchome.com.tw/prod/"
# search switch 為例
url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=switch&page=2&sort=sale/dc"
r = requests.get(url)
r.encoding = 'utf-8'
jsonData = r.json()
# print(jsonData)
# 總頁數
totalPage = jsonData['totalPage']
# print(totalPage)
products = jsonData['prods']  # type = list

data_dict = {}
# 存放各商品字典
data_list = []

for prod_data in products:
    prod_dict = {}
    # print(prod_data)
    # 商品ID (進入商品頁面會用到)
    prod_id = prod_data['Id']
    prod_dict['Id'] = prod_id
    # 商品圖片
    prod_img = img_url + prod_data['picS']
    prod_dict['image'] = prod_img
    # 商品名稱
    prod_name = prod_data['name']
    prod_dict['name'] = prod_name
    # 商品描述
    prod_describe = prod_data['describe']
    prod_dict['describe'] = prod_describe
    # 商品售價
    prod_price = prod_data['price']
    prod_dict['price'] = prod_price
    # 商品鏈結
    prod_url = prodMain_url + prod_id
    prod_dict['url'] = prod_url
    # print(f'id: {prod_id}, img: {prod_img}, name: {prod_name}, \
    #     describe: {prod_describe}, price: {prod_price}, url: {prod_url}')
    # print(prod_dict)  # dict
    data_list.append(prod_dict)

data_dict['Results'] = data_list
# 將 dict 轉成 json
data_json = json.dumps(data_dict, indent=4, ensure_ascii=False)
# 將json寫成檔案
with open('switch.json', 'w', encoding='utf-8') as f:
    f.write(data_json)

# 將json轉成dataFrame,
info = json.loads(data_json)
df = json_normalize(info['Results'])

# 可以對dataFrame進行一些篩選的動作
# 篩選出價格最便宜的五個, 並顯示商品名稱,價格,鏈結 (關於dataFrame相關操作請看 ml資料夾)
filter_df = df[['name', 'price', 'url']].sort_values(
    'price', ascending=True)[0:5]


# 將filter_df輸出成csv
def df_CSV(file_name):
    file_name = 'pchome_switch.txt'
    filter_df.to_csv(file_name, encoding='utf-8', index=False)
