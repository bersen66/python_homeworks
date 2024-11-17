# Дз 1:
## Окружение(Ubuntu 22.04)

```
python -m venv env
source env/bin/activate
```

## Запуск и проверка:

```
make nl_single -- запуск nl на одном файле
make nl_multiple -- запуск nl на нескольких файлах
make nl_stdin -- запуск nl с чтением из stdin

make tail_single -- запуск tail на одном файле
make tail_multiple -- запуск tail на нескольких файлах
make tail_stdin -- запуск tail с чтением из stdin

make wc_single -- запуск wc на одном файле
make wc_multiple -- запуск wc на нескольких файлах
make wc_stdin -- запуск wc с чтением из stdin
```
