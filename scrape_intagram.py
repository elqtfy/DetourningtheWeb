import requests

headers = {
    'cookie': 'mid=Vx3FWgAEAAFVcOj9Dq6cLneokTgq; datr=p6sLWjJlWMoynCYtB3dsqQJT; sb=qKsLWmITtnLzpvDEFf_dam05; c_user=100001434125109; xs=182%3AdiPYXlChbPk9FQ%3A2%3A1510714280%3A2971%3A10119; fr=0xvJTTwHisWurFaxO.AWX3hc8frU9CQJFbsytxhXY27YI.BaC6uo.Ab.AAA.0.0.BaC6uo.AWUG4ELC; pl=n; sessionid=45050229%3A6p2u1kY58FGaW1%3A19; csrftoken=ulQlrudDG7DFnhGeKmahRbz0TA9kGcDW; ds_user_id=45050229; rur=FTW; ig_pr=2; ig_or=landscape-primary; ig_vw=1436; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=XtHpERKcV_LJR-c-idBpWAXR7tFPazwkpN3J-IV7rHQ.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUFVZzJ3Sm5SSW1oWEJDZnpDY3J5cVVtRGFLNnBweTYtTDNpcXZXaXJta2JRbnlOVDh2OGZycDhNZ2JmUzdKazVBWkpnLUhDWG4xUnFUV3ZHUlFYSlVlSEJCcFZfanJvd1lsMjBSaE9JdjhPUU5NcjlCUzI2VThuNVhta0Vad2gteHdqa1o1TUNHLXNJekswMmp2VVNFRDB6M0tlN2FwWWZlcXh5UmtEOS02Q09CYWh5NmhuZlJVaE1EYU9PanNUU3lMSDAxLXEyNDlMUXN2Q3E5UTlKYS1XaFZ6MUdQWkZ6V2UzcmZpVkNJbG1rdDZSNlllaHRyeXBQaDd4MC1oRmFHbTM0REZjekQxeEU0bkhkclY0eHZHQ1ZuazdqNEtwakVRY0Vxcy1kRUFJa1EwTHoyVmVuS1AySHZOVklxeU45WVIzaVZOV2RoYVhEZ0RlYlhIVjcwSSIsImlzc3VlZF9hdCI6MTUxNzg3NjI0NSwidXNlcl9pZCI6IjEwMDAwMTQzNDEyNTEwOSJ9; ig_vh=150; urlgen="{\\"time\\": 1517876241\\054 \\"216.165.95.186\\": 12}:1eiqx6:O1vfuYQSx0AcSQ0os4B5F1O2UeE"',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'accept': '*/*',
    'referer': 'https://www.instagram.com/',
    'authority': 'www.instagram.com',
    'x-requested-with': 'XMLHttpRequest',
}

params = (
    ('query_hash', '7c0e77784c942e9ae4afb3a9469c5a31'),
    ('variables', '{"only_stories":false}'),
)

response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)
#print response.json()
photos = response.
pprint(response.json())
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.instagram.com/graphql/query/?query_hash=7c0e77784c942e9ae4afb3a9469c5a31&variables=%7B%22only_stories%22%3Afalse%7D', headers=headers)
