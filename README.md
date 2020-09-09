# edvPayerChecker

## Installation:
```
pip install -r requirements.txt
```

## Usage:
```
gurbanli@home:~# python main.py
usage: main.py [-h] [--voen VOEN]

ƏDV ÖDƏYİCİSİNİN AXTARIŞI

optional arguments:
  -h, --help   show this help message and exit
  --voen VOEN  Vergi ödəyicisinin eyniləşdirmə nömrəsi
  
  

gurbanli@home:~# python main.py --voen 123
VOEN 123 üçün sorğu göndərilir...

Incorrect VOEN


gurbanli@home:~# python main.py --voen 2100090341
VOEN 2100090341 üçün sorğu göndərilir...

VOEN is not registered for VAT
```
