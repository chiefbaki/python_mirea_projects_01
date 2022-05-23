# import openpyxl
# import vk_api
# import re
# from weather import *
# from five_day_weather import *
# from vk_api.keyboard import VkKeyboard, VkKeyboardColor
# from vk_api.longpoll import VkLongPoll, VkEventType
# from vk_api.utils import get_random_id


def main():

    vk_session = vk_api.VkApi(token='token')
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Погода', color=VkKeyboardColor.POSITIVE)


    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
            text = event.text
            user_id = event.user_id
            msg = re.match("^[А-Я]{4}[-]{1}[0-9]{2}[-]{1}[0-9]{2}$", text.upper())
            print(f'New form {user_id}, text {text}')
            if (text == 'Привет') or (text == 'привет') or (text == 'начать'):
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message='Привет ' +\
                                 vk.users.get(user_id=event.user_id)[0]['first_name'])
            elif text.lower() == 'показать погоду на сегодня':
                t = Weather()
                vk.messages.send(user_id=event.user_id, random_id = get_random_id(), message=t.get_description)
            elif text.lower() == 'показать погоду в Москве на 5 дней'.lower():
                w = Weather5Day()
                attachment = 'photo100172_166443618_accessKey'
                vk.messages.send(user_id=event.user_id, attachment=attachment, random_id=get_random_id(), message=w.get_info)
            elif text.lower() == 'погода на завтра':
                t = Weather5Day()
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=t.get_info_tomorrow)
            elif msg:
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message='Расписание')
            else:
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message='Неизвестная команда')


if __name__ == '__main__':
    main()
