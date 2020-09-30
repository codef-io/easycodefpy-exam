from easycodefpy import Codef, ServiceType, encrypt_rsa, encode_to_file_string

demo_client_id = ''
demo_client_secret = ''

client_id = ''
client_secret = ''

public_key = ''

# 코드에프 인스턴스 생성
codef = Codef()
codef.public_key = public_key

# 데모 클라이언트 정보 설정
# - 데모 서비스 가입 후 코드에프 홈페이지에 확인 가능(https://codef.io/#/account/keys)
# - 데모 서비스로 상품 조회 요청시 필수 입력 항목
codef.set_demo_client_info(demo_client_id, demo_client_secret)

# 정식 클라이언트 정보 설정
# - 정식 서비스 가입 후 코드에프 홈페이지에 확인 가능(https://codef.io/#/account/keys)
# - 정식 서비스로 상품 조회 요청시 필수 입력 항목
codef.set_client_info(client_id, client_secret)

# 요청 파라미터 설정
# - 계정관리 파라미터를 설정(https://developer.codef.io/cert/account/cid-overview)
account_list = []
account = {
    'countryCode':  'KR',
    'businessType': 'BK',
    'clientType':   'P',
    'organization': '0004',
    'loginType':    '0',
}

# 비밀번호 설정
pwd = encrypt_rsa("password", codef.public_key)
account['password'] = pwd
account_list.append(account)

# 인증서 정보 가져오기
cert = encode_to_file_string('CERT_FILE_PATH')
key = encode_to_file_string('KEY_FILE_PATH')
account['derFile'] = cert
account['keyFile'] = key

parameter = {
    'accountList': account_list,
    'connectedId': '8PQI4dQ......hKLhTnZ',
}

# 요청
res = codef.add_account(ServiceType.SANDBOX, parameter)
print(res)