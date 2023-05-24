import requests
from pprint import pprint

class VK:

   def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

   def get_photos_info(self):
       url = 'https://api.vk.com/method/photos.get'
       params = {'user_ids': self.id,
                 'album_id': 'wall',
                 'rev': 1,
                 'extended': 1,
                 'photo_sizes': 1}
       photo_inf = requests.get(url, params={**self.params, **params}).json()
       return photo_inf

# if __name__ == '__main__':
#     access_token = 'vk1.a.LI8l1U-Grlx70bUorkGiwztgU5GOpjDL7qdJh4y0fQFQpsS6l9q8f-K6sS0z9EiwBNfH1PrFQoL2SBBEwBKjiKvmGvebvbnxz1BNOF-hvnu-eOF0jgQl2DZeUFndPcGVmzINIvSok5YHv7JDvSHOEVxphib_YUH-6D-thCpv6by_Adgj-rECGZ3DqpKovGdWTqc7ZJu_xeJ5v2y0p8sdXQ'
#     user_id = '798893247'
#     vk = VK(access_token, user_id)
#     pprint(vk.get_photos_info())
