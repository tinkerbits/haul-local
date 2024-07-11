import requests, json
from bs4 import BeautifulSoup
from celery import shared_task

@shared_task
def get_shopify_products():

    domain = "https://art-the-duck.myshopify.com"

    endpoint = "/admin/api/2024-04/products.json?"

    product_fields = "limit=2"

    base_url = domain + endpoint + product_fields
    header_values = {'Content-Type':'application/json', 'X-Shopify-Access-Token':'enter token here'}

    response = requests.get(base_url, headers=header_values)
    soup = BeautifulSoup(response.content, 'html.parser')
    decodedsoup = json.loads(soup.text)


    for value in decodedsoup.values():
        for product in value:

            product_id = product['id']
            print(f'ID: {product_id}')

            product_title = product['title']
            print(f'Title: {product_title}')

            product_images = product['images'][0]['src']
            print(f'Images: {product_images}')


