# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests, json
from kuthaksik.models import Haksik

# Create your views here.

def get_haksik():
    myUrl = 'http://coop.koreatech.ac.kr/m_dorm/menu.php'
    # myUrl = 'http://coop.koreatech.ac.kr/m_dorm/menu.php?dt=20190403'

    req = requests.get(myUrl)
    source = req.content.decode('utf-8')
    soup = BeautifulSoup(source, 'html.parser')

    campus1 = soup.find('campus', {'name':'Campus1'}) # 한기대 본캠
    
    # 아침, 점심, 저녁
    # 한식, 일품, 특식, 능수관
    haksik = {
        'breakfast': {
            'korean': '',
            'onedish': '',
            'special': '',
            'western': '',
            'faculty': ''
        },
        'lunch': {
            'korean': '',
            'onedish': '',
            'special': '',
            'western': '',
            'faculty': ''
        },
        'dinner': {
            'korean': '',
            'onedish': '',
            'special': '',
            'western': '',
            'faculty': ''
        },
    }

    listed_mealtime = ['breakfast', 'lunch', 'dinner']
    listed_restaurant = ['korean', 'onedish', 'special', 'western', 'faculty']

    for m in range(3): # 아침, 점심, 저녁 별로 학식 메뉴 추가
        menu_tree = campus1.findAll(listed_mealtime[m])

        for r in range(5): # 능수관까지만 가져옴
            menu = str(menu_tree[r].dish.string).strip()
            haksik[listed_mealtime[m]][listed_restaurant[r]] = menu

    return haksik


def update_haksik():
    myJson = json.loads(json.dumps(get_haksik()))
    if myJson is not None:
        try:
            today_haksik = Haksik.objects.latest('updated_at')
            today_haksik.breakfast = myJson['breakfast']
            today_haksik.lunch = myJson['lunch']
            today_haksik.dinner = myJson['dinner']
            today_haksik.save()

        except Haksik.DoesNotExist:
            today_haksik = Haksik()
            today_haksik.breakfast = myJson['breakfast']
            today_haksik.lunch = myJson['lunch']
            today_haksik.dinner = myJson['dinner']
            today_haksik.save()