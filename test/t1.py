import httpx

headers = {
    'authority': 'duo1.dns33.top:39988',
    'sec-ch-ua':
    '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'accept': '*/*',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.57',
    'sec-ch-ua-platform': '"macOS"',
    'origin': 'https://duo1.dns33.top:39988',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://duo1.dns33.top:39988/search?word=91',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

data = {'word': '91', 'pageSize': '3', 'pageNo': '1'}

response = httpx.post('https://duo1.dns33.top:39988/ad/list0',
                      headers=headers,
                      data=data).json()
print(response)
