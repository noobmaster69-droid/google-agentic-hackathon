import os
import json
from vertexai.generative_models import GenerativeModel
import vertexai
import requests


PROJECT_ID = os.getenv("GCP_PROJECT_ID")
LOCATION = os.getenv("GCP_LOCATION")
vertexai.init(project=PROJECT_ID, location=LOCATION)
MODEL = GenerativeModel("gemini-1.5-pro-002")
def scrape_shopping_data(product_name, company_names_input):
    """
    Scrapes data from the Google Shopping API for the given product name and company names.
    """
    api_key = "67e19fc7eccb45caac0ab4bb"
    url = "https://api.scrapingdog.com/google_shopping"
    prompt = "Buy "+product_name+": "+company_names_input+" from Amazon"
    params = {
        "api_key": api_key,
        "query": prompt,
        "language": "en",
        "country": "us"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        data = filter_products_by_company(data, company_names_input)
        # print(data)
        return data
        # return data
    else:
        print(f"Request failed with status code: {response.status_code}")


# json_string = '{"filters": [], "ads": [], "shopping_results": [{"title": "Google Pixel 9 Pro", "product_link": "https://google.com/shopping/product/11426303279205904963", "product_id": "11426303279205904963", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=11426303279205904963&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Google Fi Wireless", "price": "$699.00", "extracted_price": 699, "old_price": "$999", "old_price_extracted": 999, "rating": 4.5, "reviews": "1.1K", "tag": "30% OFF", "thumbnail": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQ45qrPNsJO-5kewSghHmFExZzwn95Se218fY3VlobQZP5sa4pRvbX9gELS_FWyovuOj2cwcrcaUg-otQPHbG1yLgOtkNVlUGtOyHPhuhYf", "position": 1}, {"title": "Google Pixel 8a", "product_link": "https://google.com/shopping/product/7749446776959391844", "product_id": "7749446776959391844", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=7749446776959391844&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Google Store", "price": "$499.00", "extracted_price": 499, "old_price_extracted": null, "rating": 4.5, "reviews": "2.3K", "thumbnail": "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcS8M8tt3BU8WdVW6nVYiJ6EgFtVZ9KcJE8sljzprqYfFfq27Q4TLvgGitFGfC3YRGJERPqrHRBlDeVw8gk2aI3jjU-6tfmWuZ64jayuxZY", "position": 2}, {"title": "Samsung Galaxy A35 5G", "product_link": "https://google.com/shopping/product/16186381630926554796", "product_id": "16186381630926554796", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=16186381630926554796&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Google Fi Wireless", "price": "$199.99", "extracted_price": 199.99, "old_price": "$400", "old_price_extracted": 400, "rating": 4.6, "reviews": "1.3K", "tag": "50% OFF", "thumbnail": "https://encrypted-tbn2.gstatic.com/shopping?q\\u003dtbn:ANd9GcSOM5pnpkC5bfIW5U2pfIlbUUE6mGf9bf8J__CZhbi6JsuaO5tTa5lq5jLlwquQ579cy_jEhIapiSHi_c9K4ACIxZbIcPTZfi3lzH5gwTYlglDD8gucBgdv", "position": 3}, {"title": "Google Pixel 9", "product_link": "https://google.com/shopping/product/625513772960203147", "product_id": "625513772960203147", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=625513772960203147&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Google Store", "price": "$799.00", "extracted_price": 799, "old_price_extracted": null, "rating": 4.6, "reviews": "1.3K", "thumbnail": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcRZ8ufI7L4zgdG47J-EN_QuG9uvZLt6pZGk1yGnrSXxEwNqrtCu4BBm_Gxl4bccWJ_448RpTbJQHNbVNopFsnBXGBxh80QfeBcsdiyoS7E", "position": 4}, {"title": "Samsung Galaxy S25 with Google Fi Wireless - Mint - 128 GB (+ plan)", "product_link": "https://google.com/shopping/product/9598558369026043359", "product_id": "9598558369026043359", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=9598558369026043359&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Google Fi Wireless", "price": "$599.99", "extracted_price": 599.99, "old_price": "$800", "old_price_extracted": 800, "rating": 4.7, "reviews": "620", "tag": "25% OFF", "thumbnail": "https://encrypted-tbn1.gstatic.com/shopping?q\\u003dtbn:ANd9GcQcGbe89nPz1eOlzo2cklQeCqUE7sZdkgqPRADwSHbC1-PqN1HiafU9NGvplQONbzsBQBtFRStK-wqw7AgdHxvVB5ZJtS35iZH--S_p3Ufu7kCbmE7TZbyZ", "position": 5}, {"title": "Google Pixel 9 Pro Fold", "product_link": "https://google.com/shopping/product/1527625693224901749", "product_id": "1527625693224901749", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=1527625693224901749&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Google Store", "price": "$1,919.00", "extracted_price": 1919, "old_price_extracted": null, "rating": 4.5, "reviews": "521", "thumbnail": "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcTejZd8GpwycH8nFGpLCGbH4XlR2VZXbAacihYPrrzWQyqQkAliVTaPCqPIq96Je39VIPkDDr89eoh1G6gMYI0qToWzg2IpllB3RLyJ_QE", "position": 6}, {"title": "Samsung Galaxy S25 with Google Fi Wireless - Icyblue - 128 GB (+ plan)", "product_link": "https://google.com/shopping/product/5486555641990303225", "product_id": "5486555641990303225", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=5486555641990303225&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Google Fi Wireless", "price": "$599.99", "extracted_price": 599.99, "old_price": "$800", "old_price_extracted": 800, "rating": 4.7, "reviews": "620", "tag": "25% OFF", "thumbnail": "https://encrypted-tbn0.gstatic.com/shopping?q\\u003dtbn:ANd9GcT3L0DFyCQYrfeqvfzWOqP9sOoqJWeyUxrwAJJVVfs2mYw5lr0oH5-iNqg1IHUCD4cyI8uLaml2are4BuIKvWxRWsk7-gtFBN9bAS9vqTd1C3si2bdMW4UrQQ", "position": 7}, {"title": "Pixel 9 Peony 256GB (Fi)", "product_link": "https://www.google.com/shopping/product/1?gl=us&prds=pid:14984508770291598237", "product_id": "14984508770291598237", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=14984508770291598237&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Google Store", "price": "$899.00", "extracted_price": 899, "old_price_extracted": null, "rating": 4.6, "reviews": "1.3K", "thumbnail": "https://encrypted-tbn0.gstatic.com/shopping?q\\u003dtbn:ANd9GcSsPvLSHkCkOaG1p44Oj-BlME29N7HqDY1GE94lWlsKvCsbAJo0MlRAN_1mcPJ4EC-gIb0bBjFvJpUbdyj6fwq0Wk3xFP1ReCBO7DhDJDubJu1nGZ6DYaeR", "position": 8}, {"title": "Google Pixel 9 Pro XL", "product_link": "https://google.com/shopping/product/14767949130733293114", "product_id": "14767949130733293114", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=14767949130733293114&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Google Store", "price": "$1,199.00", "extracted_price": 1199, "old_price_extracted": null, "rating": 4.5, "reviews": "1.6K", "thumbnail": "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQE61DtePSTVnklaHNkfFIEkKxyBNBZO4uogZXbxWlKItj5k6sXAyJjftc4G1xjgR3pSDU9pw0J1L3Z-x-n3b-nRy7ayLFubG2R_jGKWEc", "position": 9}, {"title": "Samsung Galaxy S25 with Google Fi Wireless - Navy - 128 GB (+ plan)", "product_link": "https://google.com/shopping/product/1134659983706069422", "product_id": "1134659983706069422", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=1134659983706069422&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Google Fi Wireless", "price": "$599.99", "extracted_price": 599.99, "old_price": "$800", "old_price_extracted": 800, "rating": 4.7, "reviews": "620", "tag": "25% OFF", "thumbnail": "https://encrypted-tbn3.gstatic.com/shopping?q\\u003dtbn:ANd9GcQuo0O7E4iUffm8CnZvu4VDLb_tfcR-kCqk1sOjdq0QCXK3WAOwI4uG57Kzrhi5mwH73JSLytRzJkKVreveAoeJ0OpUuAQZ48vbJPdRRvhQ58iZCac0YxYvJw", "position": 10}, {"title": "Google Pixel 8", "product_link": "https://google.com/shopping/product/14487176227690374953", "product_id": "14487176227690374953", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=14487176227690374953&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Google Fi Wireless", "price": "$449.00", "extracted_price": 449, "old_price": "$699", "old_price_extracted": 699, "rating": 4.4, "reviews": "2.2K", "tag": "35% OFF", "thumbnail": "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQ822drggb0HivOmluU_2a_4oiUP4Gw98t4QtJ7WBjC2RpRddvLknK-GEjRMnC79xJlHuLtyi-osYnuShcomyWGERPPaeTHfXsRods5QmLj", "position": 11}, {"title": "Google Pixel 8 Pro", "product_link": "https://google.com/shopping/product/3614114586471414091", "product_id": "3614114586471414091", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=3614114586471414091&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Google Store", "price": "$999.00", "extracted_price": 999, "old_price_extracted": null, "rating": 4.5, "reviews": "3.3K", "thumbnail": "https://encrypted-tbn2.gstatic.com/shopping?q\\u003dtbn:ANd9GcRZN7DUowsTWePJdUjEjCy6qi_pfL6IZRjL-XTz_JKUlycMEi2RAUoyLFnm31FjkIHwes18_-1-GuOI3D7qmHZW7IoOQg0jtVy-1SA2pIu71N7h5BuQevD2", "position": 12}, {"title": "Restored Samsung G970u Galaxy S10e 128gb", "product_link": "https://google.com/shopping/product/11025385048326619742", "product_id": "11025385048326619742", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=11025385048326619742&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Google Fi Wireless", "price": "$699.99", "extracted_price": 699.99, "old_price": "$1,000", "old_price_extracted": 1000, "rating": 4.6, "reviews": "12K", "tag": "30% OFF", "thumbnail": "https://encrypted-tbn2.gstatic.com/shopping?q\\u003dtbn:ANd9GcQtto77jXPr4iS7u1uE7GRifC-4Ae7BYJ1iL9xd-hWB8_LJ4HknvZR79ot-fGzagzPRlioH-0Yq8v6AntUidz97yONuS4j41n-jvZe3UtLdQPIFLZCyU-Fz", "position": 13}, {"title": "Samsung Galaxy S25 Ultra Titanium", "product_link": "https://google.com/shopping/product/18407011980288807701", "product_id": "18407011980288807701", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=18407011980288807701&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Google Fi Wireless", "price": "$999.99", "extracted_price": 999.99, "old_price": "$1,300", "old_price_extracted": 1300, "rating": 4.8, "reviews": "37K", "tag": "23% OFF", "thumbnail": "https://encrypted-tbn2.gstatic.com/shopping?q\\u003dtbn:ANd9GcQLOesb7rdawEOkUX5RB83Lw-sSyRUgYhjL8qjOp88Si3Z1KKaNYpop9JA5NCrExuLBJopAFKGr9RUwNtc4vnk8yKggwixf1pJaeElj_EY5sVqyvM_D9aL1sw", "position": 14}, {"title": "Apple iPhone 13 128 GB Black / Midnight with Mobile Phone Plan", "product_link": "https://www.google.com/shopping/product/1?gl=us&prds=pid:7176948401546798593", "product_id": "7176948401546798593", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=7176948401546798593&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Boost Mobile", "price": "$99.99", "extracted_price": 99.99, "old_price": "$630", "old_price_extracted": 630, "rating": 4.7, "reviews": "66K", "tag": "84% OFF", "thumbnail": "https://encrypted-tbn3.gstatic.com/shopping?q\\u003dtbn:ANd9GcTrpeTylcYaCjgzlwjEi-6njI_F0uhyx8rdzLrMlqG41rIaS55LzU6Op0qIkh_Hm7mbf2Z0j1qSZ9P8O5WYhBpCqPNlIOnLiBxLZVLeDSK85VKZu0T86vSp", "position": 15}, {"title": "Samsung Galaxy S25 Ultra", "product_link": "https://google.com/shopping/product/12282010806018998187", "product_id": "12282010806018998187", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=12282010806018998187&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Samsung", "price": "$999.99", "extracted_price": 999.99, "old_price": "$1,300", "old_price_extracted": 1300, "rating": 4.8, "reviews": "38K", "tag": "23% OFF", "thumbnail": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcT0jL13dWLxn9BK8ErG8PHGluvpmguMlvWQ_s_wAOnaJd0CprnX-1oeEtUiP2OQZD-T7SodNGu3j-a3Gr_VsBR6jM5NiIIKCCoEnWyWv6k", "position": 16}, {"title": "Samsung Galaxy S25", "product_link": "https://google.com/shopping/product/2074928739575654812", "product_id": "2074928739575654812", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=2074928739575654812&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Samsung", "price": "$799.99", "extracted_price": 799.99, "old_price_extracted": null, "rating": 4.8, "reviews": "15K", "thumbnail": "https://encrypted-tbn2.gstatic.com/shopping?q\\u003dtbn:ANd9GcRNP6CcwtXvlEOZjhOFlmrMM171OqpSq20K74uiWJR3l2PgE0nm1SG0w8piYMjobWBgMO9HLSY-MCq5g8BM-99skRjArEdaK-qyk5-pnD9Rg5sq00QQYuTlkA", "position": 17}, {"title": "Samsung Galaxy A54 5G", "product_link": "https://google.com/shopping/product/12288856394612481297", "product_id": "12288856394612481297", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=12288856394612481297&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Cricket Wireless", "price": "$49.99", "extracted_price": 49.99, "old_price": "$300", "old_price_extracted": 300, "rating": 4.5, "reviews": "35K", "tag": "83% OFF", "thumbnail": "https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcTCkKC1YUMOTK29q59gUWMtLsnDcR3hUEcDPamU8TTl3jOAjOK80dGPC_HKUjBWkF2FAgAcMFEuKI9i3SE15js1wapzXaCy2VQ-IX8B1Ik", "position": 18}, {"title": "Samsung Galaxy A16 5G Cell Phone", "product_link": "https://www.google.com/shopping/product/1?gl=us&prds=pid:806062544197697108", "product_id": "806062544197697108", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=806062544197697108&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Amazon.com", "price": "$174.99", "extracted_price": 174.99, "old_price": "$200", "old_price_extracted": 200, "rating": 4.4, "reviews": "112K", "tag": "12% OFF", "thumbnail": "https://encrypted-tbn0.gstatic.com/shopping?q\\u003dtbn:ANd9GcSuZehPcPAwxbKszBZUYItgNUQ5bmbptuJ69e-f0DD2QfU1yjLss1z45zhoFE-lz-L6VhGkQVH-kT19ej_1XcAmr7eJCpMI-aJUufX41cKuHBQ11B7_vIsDAw", "position": 19}, {"title": "Samsung Galaxy S22 Ultra", "product_link": "https://google.com/shopping/product/7874620466364601793", "product_id": "7874620466364601793", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=7874620466364601793&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Best Buy", "price": "$739.99", "extracted_price": 739.99, "old_price_extracted": null, "rating": 4.5, "reviews": "30K", "thumbnail": "https://encrypted-tbn2.gstatic.com/shopping?q\\u003dtbn:ANd9GcTvpyM9zZXaOmIdzwcaX4QSJZfuYbCykeGHDAQRDiEIHZcRipWPbXdL3CFJCua73xmBWBHNarn2NFpTxSA7z-tvmvWDMzrkthgrdy2Cul0", "position": 20}, {"title": "Apple iPhone 16e", "product_link": "https://google.com/shopping/product/12611122636160472932", "product_id": "12611122636160472932", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=12611122636160472932&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Apple", "price": "$599.00", "extracted_price": 599, "old_price_extracted": null, "rating": 4.3, "reviews": "101", "thumbnail": "https://encrypted-tbn1.gstatic.com/shopping?q\\u003dtbn:ANd9GcSJ4JphUU79l7CYVrhZocM0ae-mWXOPahaVFtvmMvYqc2GqFYWO-SPLKXLtglvnkmnX4tJgpImRmbZSZklh8cYheq85bm-brJA7lvqOA9n4_K6WvK8x9O6q", "position": 21}, {"title": "Samsung Galaxy S24+ 256GB Onyx Black Unlocked", "product_link": "https://google.com/shopping/product/5115500404798631356", "product_id": "5115500404798631356", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=5115500404798631356&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Walmart", "price": "$798.00", "extracted_price": 798, "old_price": "$999", "old_price_extracted": 999, "rating": 4.6, "reviews": "25K", "tag": "20% OFF", "thumbnail": "https://encrypted-tbn0.gstatic.com/shopping?q\\u003dtbn:ANd9GcTpKnH9mcxqiX640-4Pt9LhSdbgpe99jm65GVbcrJ3L_66VzP6fcrNnOhp1-Nx9nFfXM14zLssBvtxQjNAjmpTljVayY7LTI9UJYpI8_tbCrwRxaT7oTJoM", "position": 22}, {"title": "Samsung Galaxy S24", "product_link": "https://google.com/shopping/product/13069735511210420842", "product_id": "13069735511210420842", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=13069735511210420842&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Samsung", "price": "$699.99", "extracted_price": 699.99, "old_price_extracted": null, "rating": 4.6, "reviews": "47K", "thumbnail": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcTfRa1jcfUsRonqi8BsgsWcr8KvxbSwxRDVeU7eAqm5_67XIGZDD7ywGLkJgKPIA12nSlQ-6hMi9OuXfMYKjtDPfCcY7oO9dhsTURrGG-UR", "position": 23}, {"title": "Samsung Galaxy Z Fold6", "product_link": "https://google.com/shopping/product/11074041034788291940", "product_id": "11074041034788291940", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=11074041034788291940&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Samsung", "price": "$1,899.99", "extracted_price": 1899.99, "old_price_extracted": null, "rating": 4.5, "reviews": "38K", "thumbnail": "https://encrypted-tbn1.gstatic.com/shopping?q\\u003dtbn:ANd9GcSF3iQevvfgDNPurZr8OaYM7QT9_nqb1mizSyWoGMopwuCrlZ1OzeX-TZjXCnyUKtHNnmG0ggWoasblwPTHk0foM9rRn6z6RazQ8YN1LmnsIBO50ow18zB0ZA", "position": 24}, {"title": "Apple Iphone Google Pixel Samsung Unlocked Phantom Black", "product_link": "https://www.google.com/shopping/product/1?gl=us&prds=pid:14285288582043425613", "product_id": "14285288582043425613", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=14285288582043425613&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "eBay", "price": "$1,599.99", "extracted_price": 1599.99, "old_price_extracted": null, "rating": null, "thumbnail": "https://encrypted-tbn1.gstatic.com/shopping?q\\u003dtbn:ANd9GcQARBryehMHJWq_ygFsllfKDn6X-cPG8c4WnM6dAdQGCOcUF1a_zpwNjGAgsgI5mZHuM4L_nEBhygfLWa0vgqJF-YITE_O-C3gpmMlKsrrx", "position": 25}, {"title": "Samsung Galaxy Z Flip6", "product_link": "https://google.com/shopping/product/17072897732494497385", "product_id": "17072897732494497385", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=17072897732494497385&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Consumer Cellular", "price": "$19.00 now", "extracted_price": 19, "old_price": "$45/mo x 24", "old_price_extracted": 45, "rating": 4.5, "reviews": "42K", "thumbnail": "https://encrypted-tbn2.gstatic.com/shopping?q\\u003dtbn:ANd9GcQoV-2ULDmrxyfuxuZb-vomYLD0xF1MXhwFmOWhgHDpVacOsOucVE4waWxPdPKQ9y46F-Him_Nq7HRG7Ek6Xn5u13FZRt-sRwDnXZvePxjoi4khgnO1EPRd", "position": 26}, {"title": "Apple iPhone 15 Pro Max", "product_link": "https://google.com/shopping/product/14573026088074580752", "product_id": "14573026088074580752", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=14573026088074580752&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "T-Mobile", "price": "$1,099.99", "extracted_price": 1099.99, "old_price_extracted": null, "rating": 4.6, "reviews": "28K", "thumbnail": "https://encrypted-tbn3.gstatic.com/shopping?q\\u003dtbn:ANd9GcTVBXKjIfh86EqN4p4nTC0IIX_zskuJx1ikd0PHZIAp2Gdo1rv5Yj3irNxS0SfX3_ObEXTTpAaoBOO1TYqTOgc2Sac6zCZj3g", "position": 27}, {"title": "Samsung Galaxy S25+", "product_link": "https://google.com/shopping/product/13776167595191177517", "product_id": "13776167595191177517", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=13776167595191177517&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Samsung", "price": "$849.99", "extracted_price": 849.99, "old_price": "$1,000", "old_price_extracted": 1000, "rating": 4.7, "reviews": "5.9K", "tag": "15% OFF", "thumbnail": "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQRmI0TEMM4qlQPRnhcs9CT45C8CKVExHC0CHLIqDskoVFj-lyAZq-Dhocl6oYabiIowfBSfgkIt89Xb_0M7cdsnJehFVfY3zGjMYmVZv0", "position": 28}, {"title": "Google Pixel 9", "product_link": "https://www.google.com/shopping/product/1?gl=us&prds=pid:17664135368062379740", "product_id": "17664135368062379740", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=17664135368062379740&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Visible", "price": "$799.00 now", "extracted_price": 799, "old_price": "$22.19/mo x 36", "old_price_extracted": 22.19, "rating": 4.6, "reviews": "60", "thumbnail": "https://encrypted-tbn0.gstatic.com/shopping?q\\u003dtbn:ANd9GcSreEtwklkM2p5hoDLaqKR0DQ2Lp5YSPp0CketKczhq3NUBzWBAg0Rh8nZyWAdEh3erd-Um8oQbLBirq_QTkbKPX7TFbvB63sKPaDMbf5lY1Xf3xk7NrZeGOA", "position": 29}, {"title": "Samsung Galaxy A16 5G", "product_link": "https://www.google.com/shopping/product/1?gl=us&prds=pid:1891148055347589998", "product_id": "1891148055347589998", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=1891148055347589998&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Mint Mobile", "price": "$360.00 now", "extracted_price": 360, "old_price": "$30/mo x 12", "old_price_extracted": 30, "rating": 4.4, "reviews": "112K", "thumbnail": "https://encrypted-tbn0.gstatic.com/shopping?q\\u003dtbn:ANd9GcTM85uKXGjX-LpDWbtoj66EqC2imRNO4vSB3gXVcNc4fpQkNBcLPEXvFz51JZJQwsw_lbmkCvP0aRe2QAIhimqSt7NRCmkWD4NhkfC4AZ92", "position": 30}, {"title": "Samsung Galaxy S22", "product_link": "https://google.com/shopping/product/4832290856924385835", "product_id": "4832290856924385835", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=4832290856924385835&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Best Buy", "price": "$499.99", "extracted_price": 499.99, "old_price_extracted": null, "rating": 4.2, "reviews": "22K", "thumbnail": "https://encrypted-tbn0.gstatic.com/shopping?q\\u003dtbn:ANd9GcQ1c1qrly8AoNy_gPlFj-SA6tA2jZjDuso9X6wndmlv9Q2BWhTmbgsRtoSsO3LY5AaQ_DYLVwK2RBg_1ouTEMdWeYOmVixEGfA84PJEl7px", "position": 31}, {"title": "Google Pixel 6a", "product_link": "https://google.com/shopping/product/16670268397732775288", "product_id": "16670268397732775288", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=16670268397732775288&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Amazon.com", "price": "$349.00", "extracted_price": 349, "old_price_extracted": null, "rating": 4.1, "reviews": "4.2K", "thumbnail": "https://encrypted-tbn2.gstatic.com/shopping?q\\u003dtbn:ANd9GcT9ulj-kvM1_GaWlzcXXebjdFn6wqtZ4r0qlVfYPxjDEvFjdR9F71fVBmCP_S7wMlHit5SfQe76WUfBPzE9BoMqdqtukosr2q3ckvLV7w8RB7S54_AwKT7M", "position": 32}, {"title": "Google Pixel 7 Pro", "product_link": "https://google.com/shopping/product/15169918534433587853", "product_id": "15169918534433587853", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=15169918534433587853&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Amazon.com - Seller", "price": "$395.99", "extracted_price": 395.99, "old_price_extracted": null, "rating": 4.3, "reviews": "3.6K", "thumbnail": "https://encrypted-tbn0.gstatic.com/shopping?q\\u003dtbn:ANd9GcQXenh2dd1tfP6qOGLehlo9xG3ZkCk1p1odFN8uK1pGjngTnFKK4uRevC25pnaeWyo5Vs_3zrvzognX1fpMU3iqqazDj3WKZ3_UfUjpXRqSMS245JHLT1ywJg", "position": 33}, {"title": "Google Pixel 7a", "product_link": "https://google.com/shopping/product/17398943938758290102", "product_id": "17398943938758290102", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=17398943938758290102&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Amazon.com - Seller", "price": "$337.00", "extracted_price": 337, "old_price": "$499", "old_price_extracted": 499, "rating": 4.3, "reviews": "2.5K", "tag": "32% OFF", "thumbnail": "https://encrypted-tbn0.gstatic.com/shopping?q\\u003dtbn:ANd9GcSzPxNP-cpts_fDZtVPv07Zo5PU8n66RMf4iVFz2QayAbIvjZNqYCpBOpu71xYlnvjNMdUzFAbtxr-JVfNXW_-SllPvcNQjJ5MR0l7nxgB3iubcaGtK9wO8Hw", "position": 34}, {"title": "Samsung Galaxy S24 FE", "product_link": "https://google.com/shopping/product/7250299206865938186", "product_id": "7250299206865938186", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=7250299206865938186&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Samsung", "price": "$649.99", "extracted_price": 649.99, "old_price_extracted": null, "rating": 4.5, "reviews": "50K", "thumbnail": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcREmcZd0RR-XKwWSG24uVu29YcqfTut625jSrjMhv9njqswNO74FWOOHk7XWoS0d3mqbnInSmwdHnBZNtJ-5Cu7T9nhG6FdYhMVAfax3dtU", "position": 35}, {"title": "Samsung Galaxy S25 128GB Silver Shadow", "product_link": "https://google.com/shopping/product/15590506391020776894", "product_id": "15590506391020776894", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=15590506391020776894&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Consumer Cellular", "price": "$23.00 now", "extracted_price": 23, "old_price": "$24/mo x 24", "old_price_extracted": 24, "rating": 5, "reviews": "2", "thumbnail": "https://encrypted-tbn3.gstatic.com/shopping?q\\u003dtbn:ANd9GcRhsDlr0ktkBLwuSNoeMi4ztyaZ__e04eeRKJZIU2ErvB1qcKRIr_01BEdptxIzOuvLLiotyKvlK5ldpBYLZXrN3pzaDAzj3i2BFFP58cZYTRf8XetYusgr", "position": 36}, {"title": "Apple iPhone 15 Pro", "product_link": "https://google.com/shopping/product/14557038552091671537", "product_id": "14557038552091671537", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=14557038552091671537&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Viaero Wireless", "price": "$27.75 now", "extracted_price": 27.75, "old_price": "$27.75/mo x 36", "old_price_extracted": 27.75, "rating": 4.5, "reviews": "13K", "thumbnail": "https://encrypted-tbn3.gstatic.com/shopping?q\\u003dtbn:ANd9GcShxSyZXtO7LF5LshITekkP2tyDopBe73pyil0kgUK6ExiJ8wi3W2JSxHmjOk1eLngOhFTdGRcUTYPrS1ZuqBMDQVZLy1vNwR-Re8ELzY98PMXt8ckV-HOn", "position": 37}, {"title": "Google Pixel 8A", "product_link": "https://www.google.com/shopping/product/1?gl=us&prds=pid:14925429418933782096", "product_id": "14925429418933782096", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=14925429418933782096&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "US Mobile", "price": "$24/mo", "extracted_price": 24, "old_price": "x 24", "old_price_extracted": 24, "rating": 4.5, "reviews": "2.3K", "thumbnail": "https://encrypted-tbn2.gstatic.com/shopping?q\\u003dtbn:ANd9GcQdRoGbRdqB0ntdRhw1b7CgCL0oyhkke-TOAWDW5oIoWtZnWzwzl_-v3js7aDsJ7kenREcqUaNbB-oYs9j-hDivcQPN96iUWb86VStkisZCk91uJy_Nx-cX", "position": 38}, {"title": "Apple iPhone 16 Pro", "product_link": "https://google.com/shopping/product/943693790761481110", "product_id": "943693790761481110", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=943693790761481110&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Apple", "price": "$999.00", "extracted_price": 999, "old_price_extracted": null, "rating": 4.2, "reviews": "4.9K", "thumbnail": "https://encrypted-tbn0.gstatic.com/shopping?q\\u003dtbn:ANd9GcTlknTkmCURtBXQFDV7OufLhBs_b8R4KnxwYr3zEqScadKiZZW4CIH_17TjG4Gyyp9Ync8aq1u3QvTxD67lntX6j6nld8JoFt-SdrRGWJamw1WLGFI7oWzI", "position": 39}, {"title": "Samsung Galaxy A35 5G Prepaid Smartphone", "product_link": "https://google.com/shopping/product/4541776675148166142", "product_id": "4541776675148166142", "scrapingdog_product_link": "https://api.scrapingdog.com/google_product?product_id=4541776675148166142&api_key=67dc27f097c7e2b909d494b4&country=us", "source": "Walmart", "price": "$199.00", "extracted_price": 199, "old_price": "$279", "old_price_extracted": 279, "rating": 4.2, "reviews": "71", "tag": "28% OFF", "thumbnail": "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcT8DhcoLbZiiUEvZXuPvtIgd2HKh1y7iO1XDZwSTQeLyKWG1G2dBpTatklxNPsgVmUy79uMEEhwgC1LNVfTMicTAr-9PGI4GQc-dzPMbFY1", "position": 40}]}'
# output_data = json.loads(json_string)
# # print(json.dumps(output_data))
#
# prompt = "Given here is a JSON of the format {\"filters\": [],\"ads\": [],\"shopping_results\": [{\"title\": "",\"product_link\": "",\"product_id\": "",\"scrapingdog_product_link\": "",\"source\": "",\"price\": "",\"extracted_price\": 0,\"old_price\": "",\"old_price_extracted\":0,\"rating\": 0,\"reviews\": "",\"tag\": "",\"thumbnail\": "",\"position\": 0}]} I want you to go over the data, and find Distinct values of 'title'. Please ignore repetitive ones, like, Apple iPhone 15 Midnight Black is the same as Apple iPhone 15 Oyester Green. In this case, just pick one and ignore the other in the final list. I want you to identify Distinct titles and return the result as a json to be used in python, but keep in mind that only five products of a company are supposed to be returned. For an example, if there are 7 products of Google, 6 products of Apple and 8 products of Samsung, then return a list containing only 5 products of Google, Apple and Samsung each, choose any 5 from the list of Distinct titles that you identified earlier. The output is required to be in this format: {\"distinct\": {filtered_product1, filtered_product2,etc}}, where filtered_product1 and filtered_product2, etc would be the comma separated value of the products from each company, but not exceeding five products respective to each company. This here is the Actual Data: "+json_string
# response = MODEL.generate_content(prompt).text
# # print(response)
# response = response[len('```json'):]
# response = response[:-len('```')]
# response.strip()
# response = json.loads(response)

def filter_products_by_company(output_data, company_names_input):
    """
    Filters the shopping results to include at most 5 distinct products per company
    specified in company_names_input.
    """
    try:
        max_products_per_company = 5
        shopping_results = output_data.get("shopping_results", [])
        company_names = [company.strip().lower() for company in company_names_input.split(",")]

        company_products = {company: [] for company in company_names}
        filtered_results = []

        for product in shopping_results:
            title = product.get("title", "").lower()
            for company in company_names:
                if company in title and len(company_products[company]) < max_products_per_company:
                    if product not in company_products[company]:
                        company_products[company].append(product)
                        filtered_results.append(product)
                        break  # Exit inner loop once a product is added

        output_data["shopping_results"] = filtered_results
        return json.dumps(output_data, indent=2)

    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON input"})
    except Exception as e:
        return json.dumps({"error": str(e)})

# filtered_data = filter_products_by_company(output_data, "Apple, Samsung, Google")
# final_data = json.loads(filtered_data)
# print(filtered_data)