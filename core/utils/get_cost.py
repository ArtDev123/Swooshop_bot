import requests

def get_course_CNY():
    responce = requests.get('https://api.nbrb.by/exrates/rates/462')
    text = responce.json()
    return text['Cur_OfficialRate']

def get_final_cost(cost_item, cost_weight):
    # тут формула
    result = f'cost:{cost_item}, weight:{cost_weight}, course: {get_course_CNY()}'
    return result

