# 데이터 검색 API
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
