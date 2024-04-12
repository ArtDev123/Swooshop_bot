import requests
from .weight import WEIGHT_RUB_COST_KG, SDACK

def get_course_CNY():
    responce = requests.get('https://api.nbrb.by/exrates/rates/462')
    text = responce.json()
    course = float(text['Cur_OfficialRate'])/10
    return course

def get_course_RUB():
    responce = requests.get('https://api.nbrb.by/exrates/rates/456')
    text = responce.json()
    course = float(text['Cur_OfficialRate'])/100
    return course


def get_final_cost(cost_item, weight, profit):
    
    course_ya = get_course_CNY()
    course_rub = get_course_RUB()

    weight_rub_cost = weight*(WEIGHT_RUB_COST_KG+SDACK)

    cost_item = (cost_item*1.03)*course_ya
    weight_cost = weight_rub_cost*course_rub +5
    
    result = cost_item + weight_cost + profit

    return int(result)

