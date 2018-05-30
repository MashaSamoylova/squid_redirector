# Squid Url Rewriter
>Перезапись запросов на заданные сайты

## Установка Squid:
```
apt-get install squid
```

## Настройка
- скопируйте `redirector.py` в директорию конфигураци squid
```
cp redirector.py /etc/squid/
```
- создайте файл с правилами перенаправлений в `/etc/squid/config.json`. Пример `config.json`
- добавьте конфигураци для squid в `/etc/squid/squid.conf`:
  ```
  url_rewrite_children 3 
  url_rewrite_program /etc/squid/redirector.py /etc/squid/config.json
  ```

## Дополнительная документация
  - http://wiki.squid-cache.org/Features/Redirectors
  - http://www.squid-cache.org/Doc/config/url_rewrite_program
