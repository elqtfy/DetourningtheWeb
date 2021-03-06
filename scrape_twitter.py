import requests
from pprint import pprint

headers = {
    'cookie': 'mobile_metrics_token=146889237145790527; twitter_ads_id=v1_37845728080542402; netpu="FvS1gPr1VQA="; eu_cn=1; kdt=4E9S6cjgBcy1TIEIpAZTD72PnTyEFeL2gDkaIwMM; co=us; __utma=43838368.1848699191.1463281269.1510612442.1511912569.4; __utmz=43838368.1510612442.3.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.1848699191.1463281269; tfw_exp=0; _mobile_sess=BAh7ByIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNoSGFzaHsABjoKQHVzZWR7ADoQX2NzcmZfdG9rZW4iJTg1MTliMmZiNmMyYzdmZDg1ZGEzNzkxMTE4NDI5MGZh--1f875c3e5a526a10e534f1e2b6662abc3d28207f; zrca=5; d=32; remember_checked_on=0; dnt=1; personalization_id="v1_/lWE/F8XET6bVksIZHVN0Q=="; guest_id=v1%3A151883434324135452; ads_prefs="HBESAAA="; _twitter_sess=BAh7DSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCNvGqWNgAToMY3NyZl9p%250AZCIlMGYyMjZiYTg5YjI3MGVkNDdlZjFmY2QxMGIyNGI3ZTg6B2lkIiVjZDlj%250AZjU1N2Y5OGNmZWQ0OGVhNmRmNDY0MzI0ZDU1NzofbG9naW5fdmVyaWZpY2F0%250AaW9uX3VzZXJfaWRsKwf8By2hOiJsb2dpbl92ZXJpZmljYXRpb25fcmVxdWVz%250AdF9pZCIlaFQwazM4MEd1TEtIR3lwbk9RS3NDazRuQXAwZGFPU3c6CXVzZXJs%250AKwkAgNdBOayPDCIJcHJycCIA--aeb818ed5e42a39a6d61ab65bdfb3140ba4602e1; twid="u=905131412042514432"; auth_token=2a1172fae2d6e53ea3485511c0a4645f249a23c0; lang=en; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; ct0=4aa9d9fa63deb1f465e76195f0ec61a6',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'referer': 'https://twitter.com/search?q=%23sigh&src=typd',
    'authority': 'twitter.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-twitter-active-user': 'yes',
}

params = (
    ('vertical', 'default'),
    ('q', '#sigh'),
    ('src', 'typd'),
    ('include_available_features', '1'),
    ('include_entities', '1'),
    ('max_position', 'TWEET-965773679501045760-965773679501045760-BD1UO2FFu9QAAAAAAAAVfAAAAAcAAABWAJDBAAAAAAEQQoAAAhYQAAACAAAAJgAgIBAAEIAIAAAAAAIAAAAAHAEACARAQIABAAAAAAAAAAAABAAQQBBAAAASgQBCAAQAAAIAiAwAAAAAIBKAICCAhACISAAAACQAAAKCCAAAAQAAEAAAgCAUACAEAAAAwAAAAAQAAACQIAAAAAAMhAAgAEAECAAAgEAEAAAAAEEAIgAAQAAAAAQABAAAAAgAAEIQAAAgAAAgAAAAgAAAAEAKABABAEAAAAAAAAAAAAAgAACAFIAABAoQAEAAAAgAAQAAIQCAAAAAAAAAAAAACACAAAAAAABAECAAAAAMBAEgAAAgCAAKBAAACCEAAEABAAAACQCABAABICAAAAAAAAAEAgAYBAQAAEAQAIAAAAgMAAAAECIAAAAEAABIAAEgAVAAACAAAAAIACAAAAAAICIAUABACAAOAAgCAIAGQgBAAQAAAdA0CAQEAAAICSBQABAAAAAABIAAAAAKAAAAFIEECAAAgAAAAQRAAAAEAACCgAQIEAECUgAAAAAEQAAAQAAQAAQAAAAAAAAQAAgCAAAAAAAAAAAGAoEAGEAARAAAAAAgAgAiIEAAAAAAAAAhBACAAEAADAAAAAAACAACAAAAAAAAAAAAAQCAAAQQAAAACIAAAAAIAAIAAhgAIAAAAAAAAAAAAAIAAAQEAAAABAAAAAIAAAAAAASIQgAAEiAAAAAAAAAABADIAAABAgESACQIAAIRIAAAAACCAIAAAABAAAQAAAIBABAAAYAAEAgAAYCAEABAAAAAUAAAAQAkgAEAAAACAAACAAAQAAQBAIIwBAAAAggAAAAAAAAAAEAFAEAAgAAAEADAAAAAAAABoAAAAADAACAAAAAsAIQAACAAAAAAAQQFCAAEBABCAAAAIAECCMCBAgAAAA==-T-0-1'),
    ('oldest_unread_id', '0'),
    ('reset_error_state', 'false'),
)

response = requests.get('https://twitter.com/i/search/timeline', headers=headers, params=params)
pprint(response.json())
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://twitter.com/i/search/timeline?vertical=default&q=%23sigh&src=typd&include_available_features=1&include_entities=1&max_position=TWEET-965773679501045760-965773679501045760-BD1UO2FFu9QAAAAAAAAVfAAAAAcAAABWAJDBAAAAAAEQQoAAAhYQAAACAAAAJgAgIBAAEIAIAAAAAAIAAAAAHAEACARAQIABAAAAAAAAAAAABAAQQBBAAAASgQBCAAQAAAIAiAwAAAAAIBKAICCAhACISAAAACQAAAKCCAAAAQAAEAAAgCAUACAEAAAAwAAAAAQAAACQIAAAAAAMhAAgAEAECAAAgEAEAAAAAEEAIgAAQAAAAAQABAAAAAgAAEIQAAAgAAAgAAAAgAAAAEAKABABAEAAAAAAAAAAAAAgAACAFIAABAoQAEAAAAgAAQAAIQCAAAAAAAAAAAAACACAAAAAAABAECAAAAAMBAEgAAAgCAAKBAAACCEAAEABAAAACQCABAABICAAAAAAAAAEAgAYBAQAAEAQAIAAAAgMAAAAECIAAAAEAABIAAEgAVAAACAAAAAIACAAAAAAICIAUABACAAOAAgCAIAGQgBAAQAAAdA0CAQEAAAICSBQABAAAAAABIAAAAAKAAAAFIEECAAAgAAAAQRAAAAEAACCgAQIEAECUgAAAAAEQAAAQAAQAAQAAAAAAAAQAAgCAAAAAAAAAAAGAoEAGEAARAAAAAAgAgAiIEAAAAAAAAAhBACAAEAADAAAAAAACAACAAAAAAAAAAAAAQCAAAQQAAAACIAAAAAIAAIAAhgAIAAAAAAAAAAAAAIAAAQEAAAABAAAAAIAAAAAAASIQgAAEiAAAAAAAAAABADIAAABAgESACQIAAIRIAAAAACCAIAAAABAAAQAAAIBABAAAYAAEAgAAYCAEABAAAAAUAAAAQAkgAEAAAACAAACAAAQAAQBAIIwBAAAAggAAAAAAAAAAEAFAEAAgAAAEADAAAAAAAABoAAAAADAACAAAAAsAIQAACAAAAAAAQQFCAAEBABCAAAAIAECCMCBAgAAAA%3D%3D-T-0-1&oldest_unread_id=0&reset_error_state=false', headers=headers)
