import uuid
import random

M4_URL = "https://graph.facebook.com/auth/login"

M4_DATA = {
    'adid': str(uuid.uuid4()),
    'format': 'json',
    'device_id': str(uuid.uuid4()),
    'email': ids, # Replace with actual ids variable
    'password': pas, # Replace with actual pas variable
    'generate_analytics_claims': '1',
    'community_id': '',
    'cpl': 'true',
    'try_num': '1',
    'family_device_id': '2',
    'credentials_type': 'device_based_login_password',
    'source': 'device_based_login',
    'error_detail_type': 'button_with_disabled',
    'enroll_misauth': 'false',
    'generate_session_cookies': '1',
    'generate_machine_id': '1',
    'currently_logged_in_userid': '0',
    'locale': 'en_US',
    'client_country_code': 'US',
    'fb_api_req_friendly_name': 'authenticate',
    'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32'
}

Content = '&'.join([f"{key}={value}" for key, value in M4_DATA.items()]) # Replace with actual Data variable

M4_HEADERS = {
    'User-Agent': '[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/FB4A;FBAV/413.0.0.30.104;FBBV/441615153;FBDM/{density=2.0,width=720,height=1590};FBLC/en_US;FBRV/441615153;FBCR/;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1804;FBSV/7.0.0;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'graph.facebook.com',
    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    'X-FB-Connection-Type': 'WIFI',
    'X-Tigon-Is-Retry': 'False',
    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
    'x-fb-device-group': '5120',
    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
    'X-FB-Request-Analytics-Tags': 'graphservice',
    'X-FB-HTTP-Engine': 'Liger',
    'X-FB-Client-IP': 'True',
    'X-FB-Server-Cluster': 'True',
    'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
    'Content-Length': str(len(Content))
}

print(M4_URL)
print(M4_DATA)
print(M4_HEADERS)
