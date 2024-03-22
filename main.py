import requests
import json
from tg_master import message, get_status_400, start_iteration, reduction_list_message, error_message, oskol_new_district, oskol_del_district, list_oskol_districts
import time
from datetime import datetime


headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://cabinet.bik31.ru',
    'referer': 'https://cabinet.bik31.ru/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

params = {
    'type': 'RESIDENTIAL_PLOTS',
}


def scrapper(url, local_oskol=False):
    api_response = requests.get(url, params=params, headers=headers)

    if api_response.status_code == 200:
        response_dict = json.loads(api_response.text)
        dirty_list = response_dict['data']
        districts = [dirty_district['name'] for dirty_district in dirty_list]

        current_time = str(datetime.now()).split('.')[0]
        if not local_oskol:
            with open('response.txt', 'w') as file:
                file.write(current_time + f'Количество районов - {len(districts)}' + '\n' + '\n'.join(districts))
        else:
            with open('oskol_response.txt', 'w') as file:
                file.write(current_time + f'Количество микрорайонов - {len(districts)}' + '\n' + '\n'.join(districts))
        return districts
    else:
        get_status_400()
        time.sleep(60)


def checker(districts_list_, last_districts_):
    flag = False
    for district in districts_list_:
        if district in last_districts_:
            continue
        else:
            if not last_districts_:
                last_districts_ = districts_list_
                continue
            last_districts_.append(district)
            message(district)
            flag = True
    if not flag and last_districts_ is True:
        last_diff = list(set(districts_list_).difference(last_districts_))
        reduction_list_message(last_diff[0])


if __name__ == "__main__":
    oskol_url = 'https://bik31.ru/api/map/microdistricts/29/'
    belg_obl_url = 'https://bik31.ru/api/map/municipalities/'
    try:
        districts_list = scrapper(belg_obl_url)
        start_iteration(len(districts_list), ', '.join(districts_list))
        time.sleep(30)

        oskol_last_district = []
        region_last_district = []
        oskol_empty_flag = False
        while True:
            if oskol_empty_flag:
                districts = scrapper(belg_obl_url)
                if 'Старооскольский ГО' in districts:
                    oskol_empty_flag = False
                if region_last_district:
                    new_district = list(set(districts).difference(region_last_district))
                    if new_district:
                        message(', '.join(new_district))
                    del_district = list(set(region_last_district).difference(districts))
                    if del_district:
                        reduction_list_message(', '.join(del_district))
                region_last_district = districts

            else:
                oskol_districts = scrapper(oskol_url, local_oskol=True)
                if oskol_districts:
                    oskol_empty_flag = False
                    if oskol_last_district:
                        new_district = list(set(oskol_districts).difference(oskol_last_district))
                        if new_district:
                            oskol_new_district(', '.join(new_district))
                        del_district = list(set(oskol_last_district).difference(oskol_districts))
                        if del_district:
                            oskol_del_district(', '.join(del_district))
                    oskol_last_district = oskol_districts
                else:
                    oskol_empty_flag = True
            time.sleep(30)
    except Exception as e:
        error_message(e)
