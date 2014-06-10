time_tracker
============

Створюємо новий virtualenv
```code
virtualenv env --no-site-packages
```
Після того, як процес завершиться, додамо налаштування $PYTHONPATH.
`nano env/bin/activate` та в кінці файлу додаємо:
```code
PYTHONPATH="${PYTHONPATH}:`pwd`"
export PYTHONPATH
```
Тепер віртуальне середовище можна активувати
`source env/bin/activate`

І от, коли нове "віртуальне оточення" створено та активовано можна поставити усі необхідні пакети командою:
`pip install -r req.txt`
