import requests, re

fb = requests.get("https://p.facebook.com/").text

m_ts = re.search('name="m_ts" value="(.*?)"', fb).group(1)
li = re.search('name="li" value="(.*?)"', fb).group(1)
jazoest = re.search('name="jazoest" value="(.*?)"', fb).group(1)
lsd = re.search('name="lsd" value="(.*?)"', fb).group(1)

data = {
    'm_ts': m_ts,
    'li': li,
    'try_number': '0',
    'unrecognized_tries': '0',
    'email': ids, # Replace with actual ids variable
    'prefill_contact_point': ids, # Replace with actual ids variable
    'prefill_source': 'browser_dropdown',
    'prefill_type': 'contact_point',
    'first_prefill_source': 'browser_dropdown',
    'first_prefill_type': 'contact_point',
    'had_cp_prefilled': 'True',
    'had_password_prefilled': 'False',
    'is_smart_lock': 'False',
    'bi_xrwh': '0',
    'encpass': f"#PWD_BROWSER:0:{m_ts}:{pas}", # Replace with actual pas variable
    'bi_wvdp': '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
    'jazoest': jazoest,
    'lsd': lsd,
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64 10;  TL-tl; SM-T231|KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.4486.95 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Host': 'p.facebook.com',
    'Content-Length': str(len('&'.join([f"{key}={value}" for key, value in data.items()]))),
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
    'sec-ch-ua-mobile': '?1',
    'x-response-format': 'JSONStream',
    'Content-Type': 'application/x-www-form-urlencoded',
    'x-fb-lsd': lsd,
    'viewport-width': '360',
    'sec-ch-ua-platform-version': '""',
    'x-requested-with': 'XMLHttpRequest',
    'x-asbd-id': '129477',
    'dpr': '2',
    'sec-ch-ua-full-version-list': '',
    'sec-ch-ua-model': '""',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua-platform': '"Android"',
    'Origin': 'https://p.facebook.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'Referer': 'https://p.facebook.com/',
    'Accept-Language': 'en-IE,en-US;q=0.9,en;q=0.8',
    'Cookie': 'datr=E9GMZhrmi8CesVpyFbMkw0Ho; sb=E9GMZpbYinn_vtJuenPhBmrQ'
}

url = "https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"

print(data)
print(headers)

response = requests.post(url, data=data, headers=headers)
