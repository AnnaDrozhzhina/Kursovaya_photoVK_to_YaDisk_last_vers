import VK
import YaDisk


if __name__ == '__main__':
    access_token = 'vk'
    user_id = '7'
    TOKEN = 'y0'
    vk = VK.VK(access_token, user_id)
    ya = YaDisk.YaDisk(token=TOKEN, count_photos=5)
    ya._create_folder()
    response = vk.get_photos_info()
    if response:
        ya.info_loading(response)
