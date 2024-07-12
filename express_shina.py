import requests
from bs4 import BeautifulSoup
import csv

while True:
    print('Выберите категорию товара: легковые шины, грузовые шины, внедорожные шины')
    name = str(input())
    get_name = ''
    if name == 'легковые шины':
        get_name = 'https://samara.express-shina.ru/search/legkovyie-shinyi'
    elif name == 'грузовые шины':
        get_name = 'https://samara.express-shina.ru/search/gruzovyie-shinyi'
    elif name == 'внедорожные шины':
        get_name = 'https://samara.express-shina.ru/search/vnedorozhnyie-shinyi'
    else:
        print('Такой категории нет')

    print('Введите название файла латинскими буквами')
    file_name = str(input())

    count = 1
    while count <= 5:
        url = f'{get_name}?num={count}'
        data = requests.get(url).text
        block = BeautifulSoup(data, 'lxml')
        heads = block.find_all('div', class_='b-offer__boxes')
        for i in heads:
            get_url = i.find_next('a').get('href')
            # print('https://samara.express-shina.ru'+get_url)
            w = ('https://samara.express-shina.ru' + get_url)
            seac = requests.get(w).text
            look = BeautifulSoup(seac, 'lxml')
            leen = look.find('div', class_='header_product_page').find('h1')
            print(leen.text.strip())
            nazvan = (leen.text.strip())
            price = look.find('span', class_='price_new')
            print(price.text.strip())
            cena = (price.text.strip())
            articul = look.find('span', class_='articul')
            print(articul.text.strip())
            codde = (articul.text.strip())
            img = look.find('div', class_='inner_images').find('img').get('src')
            print('https://samara.express-shina.ru' + img)
            pixx = ('https://samara.express-shina.ru' + img)
            params = look.find('div', class_='main_characteristic').find_all('div', class_='list_parameter')
            print(' '.join(params[0].text.strip().split()).replace('"', ''))
            param_1 = (' '.join(params[0].text.strip().split()).replace('"', ''))
            print(' '.join(params[1].text.strip().split()).replace('"', ''))
            param_2 = (' '.join(params[1].text.strip().split()).replace('"', ''))
            print(' '.join(params[2].text.strip().split()).replace('"', ''))
            param_3 = (' '.join(params[2].text.strip().split()).replace('"', ''))
            print(' '.join(params[3].text.strip().split()).replace('"', ''))
            param_4 = (' '.join(params[3].text.strip().split()).replace('"', ''))
            print('\n')

            storage = {'zagol': nazvan,
                       'cena': cena,
                       'param_1': param_1,
                       'param_2': param_2,
                       'param_3': param_3,
                       'param_4': param_4,
                       'articul': codde,
                       'img': pixx,
                       'URL': w}

            with open(f'{file_name}.csv', 'a+', newline='', encoding='utf-16') as f:
                pisar = csv.writer(f, delimiter=';', lineterminator="\r")
                pisar.writerow([storage['zagol'],
                                storage['cena'],
                                storage['articul'],
                                storage['param_1'],
                                storage['param_2'],
                                storage['param_3'],
                                storage['param_4'],
                                storage['img'],
                                storage['URL']])
        count += 1
