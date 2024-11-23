import os

BASE_DIR = os.path.dirname(__file__) # 현재 파일의 경로를 저장함
print("BASE_DIR:",BASE_DIR)
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
print("SQLALCHEMY_DATABASE_URI:",SQLALCHEMY_DATABASE_URI)
# sqlite:///는 sqlite://에 절대 경로인 / 을 설정함
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 이벤트 처리 옵션으로 필요하지 않아 False로 셋팅함.
SECRET_KEY="dev"