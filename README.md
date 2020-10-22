
<h1 align="left">:computer: QA-APITesting-Python -- IN PROGRESS  </h1>

Simple structured API Testing using Python

## Introduction
This project contains an automated API test suite for the web application <a href="http://165.227.93.41/lojinha-web/"> Lojinha </a> present in the course Teste De Software Para Iniciantes (TSPI) instructed by <a href="https://www.juliodelima.com.br/"> Julio de Lima </a>.

The tests will cover the main functionalities in the <a href="http://165.227.93.41/lojinha">Lojinha API </a>. The <a href="http://165.227.93.41/lojinha-arquivos/Swagger.pdf"> API Swagger</a> contains all functionalities supported by the API to be tested.

## Environment Setup
**Prerequisites:** 
* Python 3+ 
* pip3


1. Clone the project

2. Create and activate a virtualenv:
```
virtualenv --python=/usr/bin/python3.7 api_python 
```
```
source api_python/bin/activate
```

3. To install the required dependencies issue the below command in project root directory.
```
pip3 install -r requirements.txt
```

## How to run?

- Run the whole suite:
Issue the below commands in project root directory
```
python3 tests/suite.py
```

- Run specific test cases: 
Issue the below commands in project root directory
```
py.test tests/test_user.py -vv
```


## Author
<a target="_blank" href="https://github.com/diegohdb/diegohdb">👤 Diego Bezerra </a>

<a target="_blank" href="https://www.linkedin.com/in/diegohdb/">
  <img align="left" alt="LinkdeIN" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a target="_blank" href="https://www.instagram.com/diegohdb/">
  <img align="left" alt="Instagram" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />
</a>
<a target="_blank" href="mailto:diegohdb@gmail.com">
  <img align="left" alt="Gmail" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/gmail.svg" />
</a>
