from urllib.parse import urlparse
from dotenv import load_dotenv
import requests
import os
import argparse


def is_bitlink(token, url):
    bitly_checking_url = 'https://api-ssl.bitly.com/v4/bitlinks/'
    parsed_url = urlparse(url)
    url = f'{bitly_checking_url}{parsed_url.netloc}{parsed_url.path}'
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(url, headers=headers)
    return response.ok


def shorten_link(token, url):
    bitly_shorting_url = 'https://api-ssl.bitly.com/v4/bitlinks'

    headers = {
        'Authorization': f'Bearer {token}',
    }

    payload = {
        'long_url': url
    }

    response = requests.post(
        bitly_shorting_url,
        headers=headers,
        json=payload,
        )
    response.raise_for_status()
    bitlink = response.json()['link']
    return bitlink


def clicks_count(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    parsed_url = urlparse(url)
    bitlink = f'{parsed_url.netloc}{parsed_url.path}'
    bitly_counting_url =\
        f'''https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'''

    response = requests.get(bitly_counting_url, headers=headers)
    response.raise_for_status()
    clicks = response.json()['total_clicks']
    return clicks


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='''Программа сокращает средствами API bit.ly url,\
            полученный в аргументе. Либо выводит кол-во кликов, если в\
            аргуменет передан bit link.'''
        )
    parser.add_argument('url', help='URL для сокращения или подсчета кликов.')
    args = parser.parse_args()
    token = os.environ['BITLY_ACCESS_TOKEN']

    if is_bitlink(token, args.url):
        try:
            print(f'Кол-во кликов по ссылке {args.url}:',
                  f'{clicks_count(token, args.url)}')
        except requests.exceptions.HTTPError:
            print('Ошибка при получении кол-ва кликов.')
    else:
        try:
            print('Битлинк: ', shorten_link(token, args.url))
        except requests.exceptions.HTTPError:
            print('Введенный URL невозможно сократить.')


if __name__ == '__main__':
    main()
