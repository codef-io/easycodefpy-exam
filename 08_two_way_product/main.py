import json
from easycodefpy import Codef, ServiceType


def setup_two_way_info(parameter, result):
    json_data = json.loads(result)
    data = json_data['data']

    two_way_info = {
        'jobIndex': int(data['jobIndex']),
        'threadIndex': int(data['threadIndex']),
        'twoWayTimestamp': int(data['twoWayTimestamp']),
        'jti': data['jti'],
    }

    parameter['twoWayInfo'] = two_way_info
    parameter['is2Way'] = True


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
# - 각 상품별 파라미터를 설정(https://developer.codef.io/products)
parameter = {
    'organization': '0001',
    'userName': '이름',
    'identity': '199101011',
    'phoneNo': '01000000000',
    'telecom': '0',
    'timeout': '120',
    'authMethod': '0',
    'applicationType': '0',
    'phoneNo1': '',
}

# 코드에프 정보 조회 요청
# - 서비스타입(0:정식, 1:데모, 2:샌드박스)
product_url = '/v1/kr/public/ft/do-not-call/set-register' # 공정거래위원회 수신거부 등록/해제 신청 URL
service_type = ServiceType.SANDBOX

# * 정보 조회 요청 메소드 사용
res = codef.request_product(product_url, service_type, parameter)

# 결과 확인
print(res)

# 추가인증 정보 설정
secure_no = input('보안숫자 입력 : ')
parameter['secureNo'] = secure_no
parameter['secureNoRefresh'] = '0'
setup_two_way_info(parameter, res)

res = codef.request_certification(product_url, service_type, parameter)

# 결과 확인
print(res)

# 추가인증 정보 설정
sms_auth_no = input('SMS인증숫자 입력 : ')
parameter['smsAuthNo'] = sms_auth_no
setup_two_way_info(parameter, res)

res = codef.request_certification(product_url, service_type, parameter)

print(res)