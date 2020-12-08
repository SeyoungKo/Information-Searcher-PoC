# 데이터베이스 정보 검색기 API 서버
linewalks data searcher miniintern project 

### 1. 프로젝트 소개 & 환경
- PostgreSQL
 ```bash
 PostgreSQL 12.4 on x86_64-apple-darwin18.7.0
 ```
- Python
 ```bash
 Python 3.7.3
 ```
- Flask
 ```bash
Flask 1.1.2
 ``` 

![그림1](https://user-images.githubusercontent.com/39934875/95008824-18ece880-0658-11eb-8551-28ee5e4c7733.png)

### 2. 파일 구조
```bash
.
├── README.md
├── __pycache__
├── app
│   ├── __init__.py
│   ├── main
│   │   ├── __init__.py
│   │   ├── controllers
│   │   │   ├── __init__.py
│   │   │   ├── disease_controller.py
│   │   │   ├── drug_controller.py
│   │   │   ├── lab_controller.py
│   │   │   ├── patient_controller.py
│   │   │   └── visit_controller.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── disease.py
│   │   │   ├── drug.py
│   │   │   ├── lab.py
│   │   │   ├── patient.py
│   │   │   └── visit.py
│   │   └── util
│   │       └── dto.py
│   └── test
├── config.ini
├── requirements.txt
├── run.py
├── test
│   └── test_api.py
└── 
```

### 3. 구동 방식
* Swagger (http://localhost:5000/)

![스크린샷 2020-10-04 오후 3 53 20](https://user-images.githubusercontent.com/39934875/95009110-5d798380-065a-11eb-9ff5-dcadadb3bf31.png)

![스크린샷 2020-10-04 오후 3 53 41](https://user-images.githubusercontent.com/39934875/95009122-72561700-065a-11eb-93c5-5315ee36399e.png)

대표적인 예시로 namespace가 patient이고 path='/patients/'인 요청에 대한 설명입니다.

request  | description
------------ | ------------- 
/patients/ | 특정 컬럼 내 모든 데이터를 조회합니다.
/patients/attr/ | 검색에 포함한 특정 속성명으로 데이터를 조회합니다.
/patients/page/{offset}/{limit} | 페이지네이션을 위해 offset과 limit값으로 데이터를 조회합니다.
/patients/{text} | 검색에 포함한 속성과 값으로 데이터를 조회합니다.

### 4. API 테스트 결과

![스크린샷 2020-10-04 오후 4 26 38](https://user-images.githubusercontent.com/39934875/95009944-a2a0b400-0660-11eb-9259-0a6de3aad4d9.png)

![스크린샷 2020-10-04 오후 4 42 36](https://user-images.githubusercontent.com/39934875/95009946-a8969500-0660-11eb-9523-7f7e6255c8b1.png)

![스크린샷 2020-10-04 오후 4 41 17](https://user-images.githubusercontent.com/39934875/95009971-d54aac80-0660-11eb-801c-e34de97573f9.png)

![스크린샷 2020-10-04 오후 4 41 24](https://user-images.githubusercontent.com/39934875/95009974-daa7f700-0660-11eb-8104-27a65c2d52e7.png)
