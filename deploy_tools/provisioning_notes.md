Обеспечение работы нового сайта
================================
## Необходимые пакеты:
* nginx
* Python 3.7
* virtualenv + pip
* Git

Например, в Ubuntu:
	sudo apt-get install nginx git python3.7 python3-venv

## Конфигурация виртуального узла Nginx

* см. nginx.template.conf
* заменить SITENAME на свой домен

## Служба Systemd

* см. gunicorn-systemd.template.service
* заменить SITENAME на свой домен

## Структура папок:

/home/username
|__sites
   |__SITENAME
      |-database
      |-source
      |-static
      |-virtualenv
