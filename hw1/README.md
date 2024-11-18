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

## Вывод:

```
$ make

Demonstratibg nl single file
===================================
./nl -f input/nl
1) first line
2) second line
3) third line
4) fourth line
5) 
6) 
7) 
8) eights line
Demonstratibg nl with stdin
===================================
cat input/nl_stdin | ./nl
1) line 1
2) line 2
3) line 3
4) line 4
5) line 5
6) line 6
7) line 7
8) line 8
9) line 9
10) line 10
11) line 11
12) line 12
Demonstratibg tail single file
===================================
./tail -f input/nl
first line
second line
third line
fourth line



eights line

Demonstratibg tail multiple files
===================================
./tail -f input/tail1 -f input/tail2
==> input/tail1 <==
line 3
line 4
line 5
line 6
line 7
line 8
line 9
line 10
line 11
line 12

==> input/tail2 <==
line 3
line 4
line 5
line 6
line 7
line 8
line 9
line 10
line 11
line 12

Demonstratibg tail with stdin
===================================
cat input/tail_stdin | ./tail
blandit vestibulum. Vivamus luctus magna sit amet bibendum
tortor. Nulla facilisi. Proin suscipit, sapien vitae
dignissim dapibus, orci arcu luctus ligula, id dignissim
mi ipsum sit amet purus. Sed id turpis ut magna cursus
ultricies. Quisque rutrum egestas nisi, et bibendum erat
aliquam at. In hac habitasse platea dictumst. Mauris rutrum
tortor eu ligula pharetra, sed posuere massa facilisis.
Curabitur aliquam justo non odio egestas, at tincidunt ligula
pulvinar. Donec consequat, lacus ut sodales laoreet, nulla
lacinia quam at pulvinar mollis, neque erat ultrices nunc.
Vivamus vitae velit vitae purus vehicula vulputate. Mauris
et sagittis magna, ut consequat odio. Fusce at dolor sit
amet dolor aliquet tempor et ut nisi. Aliquam erat volutpat.
Integer sed libero ligula. Donec bibendum erat vitae turpis
mattis, at consequat magna pretium. Duis vel arcu eu urna
finibus tincidunt eu vel ante.

Demonstratibg wc single file
===================================
./wc -f input/wc
2 4 14 input/wc
Demonstratibg wc multiple files
===================================
./wc -f input/wc1 -f input/wc2
7 13 44 input/wc1
11 22 79 input/wc2
18 35 123 Итого
Demonstratibg wc with stdin
===================================
cat input/wc_stdin | ./wc
17 134 899 Итого
```
