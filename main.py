from credentials import user_login,user_password, client_secret, token
# import warnings
# warnings.filterwarnings('ignore')
import vk_api
import pandas as pd
import time
from tqdm import tqdm

session = vk_api.VkApi(token = token)
vk = session.get_api()


def get_vk_posts(owner_id,offset):
    status = session.method("wall.get",{'owner_id':owner_id,'count':50_000,'offset':offset})
    return status


texts = []

# for i in tqdm(range(40_000)):
#
#     try:
#         posts = get_vk_posts('-92876084',i)['items']
#
#         texts.append(list(map(lambda x: x['text'],posts)))
#     except:
#         pass
#
# flat_list = [item for sublist in texts for item in sublist]
# print('parsing finished')
# print(f'we got {len(flat_list)} rows')
#
# data = pd.DataFrame({'texts':flat_list})
# # print(data.head(50))
# data = data.dropna().drop_duplicates()
# print('-'* 80)
# print(f'got {len(data)} clear rows')
# data.to_csv('temp_data.csv')
# print('data saved as temp_data.csv')