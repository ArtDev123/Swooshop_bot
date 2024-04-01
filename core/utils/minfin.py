import requests

def get_course_CNY():
    responce = requests.get('https://api.nbrb.by/exrates/rates/462')
    text = responce.json()
    return text['Cur_OfficialRate']

