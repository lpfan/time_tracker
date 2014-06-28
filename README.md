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
`export PATH=$PATH:/usr/local/mysql/bin` - якщо у вас мікісь (OS X)
`pip install -r req.txt`

Налаштування бази даних для проекту:
```code
CREATE DATABASE time_tracker CHARACTER SET 'utf8';
GRANT ALL PRIVILEGES ON time_tracker.* To 'tracker'@'localhost' IDENTIFIED BY '123456';
```
