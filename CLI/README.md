# Shell

## Установка
Для работы программы необходима библиотека Lark (используется для парсинга)

```pip install lark-parser```

## Запуск
```python3 main.py```
## Доступные команды
Есть 2 типа команд: 
* Команды которые исполняет Shell
    - `cat [FILE]`
    - `wc [FILE]`
    - `echo`
    - `pwd`
    - `grep [-i] [-w] [-A A] PATTERN [FILE]`
    - `exit`
* Команды которые отдаются на исполнение subprocess
    - все остальные

## Внутреннее устройство

[Диаграмма](https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#R7V3fc5s4EP5rPJO7mWYQ4udj7KTXh3Qmc%2Bldr4%2FUEMMVIx9W6qR%2F%2FUkg2SDJBhyB86A%2BuGgRArTffrsSWmUGF%2BuXP8pok35GcZLPbCt%2BmcHbmW0D6LrkPyp5rSW%2BzQSrMotZpYPgMfuVMKHFpM9ZnGxbFTFCOc42beESFUWyxC1ZVJZo1672hPL2XTfRKpEEj8sol6VfsxinTAq88HDiU5KtUnbrwPbrE%2BuIV2Zvsk2jGO0aIng3g4sSIVwfrV8WSU47j%2FdLfd3HI2f3D1YmBe5zwQJ%2F%2FZV%2Burn%2F8u1b%2Ft%2Fm9d%2F00%2BLvDwDWzfyM8mf2xuxp8SvvgqSIb2hPklKcRWtUxF%2FSrJjBOTnxMSP3gLegLjH12Q4ppnh9OIPL139Iwbp2XI8LvtGz1wC4XHBLQWPtS6%2FN0kNSZusEJyUXvmS4btFlpW%2BNM4eWaIE3VL9YEksKP%2FQgE23Rc7lMTnQbUz6OylWCT9QL9nomBpIg8gblK7lu10CSx%2BBRJnmEs5%2FtZ4sYelf7a%2FfNPaCMPLVtMUuD3GCYnbmW1W6ifid2VRMmQkOO39FQ%2FdJSQ%2BSg8Y4HUYXCIYh0pkWk7YiIdJ1zEKkRXW5PdDmTocsJ26CA56LLczsaGhtd4bToCjSznX0RugPvD5G%2B1waS7Z%2BJyNDuaGhkRNoy3y0iLIFyu8vWeVSQ0vwJFfiRnaFwi%2FJsReB5uyR6pZCZ%2F0xKnJEQ5oadwGhDpMs0y%2BP76BU9Uw1ucbT8wUvzFJXZL9JsxCFMTpeYw9tr1XikVzKMlcmW1HngkAKC6HP00qp4H20xEyxRnkebbfZ9%2Fxpr0s9ZMUcYo3ULwvR1kpfTIJYxxwkHCu7MYeUGJm0uSxuBnGcdh2QLA4MV7nVTUJ5Vmt7iEv3Yx520k54I%2FyxQjigzFKiqxNWfJ09Yofx1Fsd51dgmWmbF6gsFw%2B0HcJDcVxfewoPkT9YNVFQiHOGoVhPVSR59T%2FIHtM1whmj7ZV13vqEGUvWVO5%2B5t5WkxAtUkJeIskpZCVH%2FLqEQ6KfZE%2FYi65ubr9dPvcFY2vUV2iWvaxGjvqJdsZ7Zi0rZZcKP74qfWYmKNX1xfrJYkX78nXTkbxI4SJfhPTgEMAzHR00ObSg4MhSoCJFrn%2FLKMaYEVUmhgEcbBnPS8wsaoxNAkDdz5%2BBQvhxGoNMPIxxL2kECAwkkd8R1G9LXRPoAioMYpyctjMb6sEfgaVi%2Fw2LeLevze0msT83a0P5EtN8BkovTvgMklPxV%2FCjQrjDMr435hQkGByrifX9K5ndsw%2FxvMGrniMJPML9KvaMxv2oCnTI%2Fs2xD%2FhORfwdOVOSvwslo5G%2FLIcICrddREW8N%2B2ti%2F8DrQf7WpJM9hvzfNJC31Po%2BQf4q9Y422XOM%2FP9IMDNuyv%2Bkk3%2BbwRs6CVQLDb3rRoKK3lVIGI3e5dD%2BMa0uM9Suhdpd4fs2AD3n8YPRHPoR229GdpXRt0I9Y%2FgDDX94%2BD%2FtVK7x76Mp17V7mvhIulWtRJlXuiWkemUGabr17fWk9NGM2ZUUTvzflvhi48X1eHFbWEdkBz1n50bz4vLH%2BA80fi8jEqiXtf%2BuI3hj7YOt3R3suiedkVF9qTeuW49yVa57ymlZ%2BQN77borPq9GZvdEtVePzLSFGVnj2nXjQeXaJzV2%2BfP752iVLY1nH8mzO648IwPCKT07kCfcjWvXZe3hUNeu1P14s3HydJzx7bq0q%2FDtasseS7nHZt4qRr%2FaGp8%2BDQ4UPn1aK3f6j9fTaEMPn9f5R8L%2FVJ27NMPJI1EOle%2FKiGqvkcOhwyUKU9b7TMBGh8FA0WFQTEHQ12M9xjxvT3%2FZZ6t4rXSVD9a1xcvqlBVakHJfDsk0lr%2FPnmHpNKE9OyedJl4lPLAjdpOiFSqi%2FO4grcMy3gtoU1loJWMdYAmhG7BnWhNueFJIZ8JN%2FQVykoybQEiU2X%2BRGZxxE3Q0dCTjhugjem1UYxR59IF98T7QOvlcge%2Beqk8O6ifQmv7jqEaq2i3yYEPAbtvQOPZzoABYm%2BibKODi1hi8P2sU09a8czMyg0BAveVchyEI9%2F8E763JOMXbeixxZlRjsxV5F8sUyeGCmQQ4K%2BIRGddTTfu4iohnvLQL1cJ8MxDsvepmeNqFSr1jjQShaphfrcEgVm1W3k61NGt42oUKJOMNEyfJ%2Be8fEzXiocP2Jepo6KzIpxHtQUccMZ23AYHGYAq%2Bw6GNFEx5%2FnnBVMjTfwdunjI0egrF3V4C%2F%2FRzCfWdEI4fbbk9fK%2B%2BoQ1oAp1vlHEK50pztEewR43GwzPIuo3nyHLZEYwHAEcA17lDEbDfDeZYSyPvxeH2%2BGygcXoMEJppgs%2Fal3V6g1NzaoLRdNpMp5PT6Sje4ahbTi8MzsU6gB0taXIVwBF9BTg9DQYs7%2BQF4zgLaEum97CLJeszI%2FPzRuahgNvLb4MDzcrpN%2BW622p9v5MNEXiULy%2FA2sVmYD7VfginMXLx%2FRCg%2FP32q1mRpW0rBDHCgJfnfLP12ZvsefiC6kk5%2F9jWZ1%2BXhvKnovzTELk45fO1YxfZf5WMsIF%2F1rTQWLO0w7%2BszzQOsPvu6jrlZJK4jhieu8oEWFZHS2NPJk28tbofNrEOri2%2FE%2Bvvca9hPhXfiUow3ebqvjjrY58JSmkeXmxo7O2v5Yj7z%2BeiMBmO%2BpZACKxjq7agAVMG3cDkub0pZXl40K1S72iL4Y9luhG7vrp72RBD2NKOk0Lv5rGJtLXjQhVpq3AxXqSt2Ff%2B6H5jg5fH89cKqT727%2BNoIlFPcJNQQaLAUi0iccQgT19%2FKuYuCBpD8gtmAaDHcwIJq1GsT32sjv3qN6gqVAf0d8GuotXuql%2BbV7ipivWxxU7R49vq947fpZaTX2rGgO9CJBuy5LNFp95F46dJW8kTlzbbjr3iBIyplipqMlhSPPyZpzqUO%2FyxLHj3Pw%3D%3D)

### Основной класс `Shell`. 
* В констукторе создается environment и 
инициализируются потоки ввода и вывода.
* Паблик метод `start()`. В цикле выполняет:
    - Читает строку из входного потока
    - При помощи `Lark` востанавливает дерево вычислений.
    - Исполняет команды

#### Парсинг
##### Грамматика строки
* `LINE` это `PIPE` или `SIMPLE`
    * `PIPE` это `SIMPLE | LINE`
    * `SIMPLE` это `DECLARATION` или `COMMAND`
        * `COMMAND` это `STR+`
        * `DECLARATION` это `STR=STR`
            * `STR` это строка без пробелов, строка в одинарных кавычках, 
            строка в двойных кавычках или любая не пустая их комбинация.

##### Немного про переменные в командах
Переменные заменяются на свои значения во время парсинга строки и обработки 
синтаксического дерева.

При этом можно выделить 2 этапа:
* В самом начале, еще до основного парсинга. Из строки выдергиваются все переменные
за исключением тех что находятся внутри кавычек любого типа. В результате получается
выражение которое можно корректно парсить на синтаксические составляющие и оно уже
никак не поменяет свою труктуру.
* Уже после парсинга, переменные внутри двойных кавычек заменяются на свои значения.

#### Выполнение            
##### PIPE
Последовательно выполняет все комманды входным потоком для каждой следующей является
выходной поток предыдущей.

##### Команды
Все команды имеют интерфейс:
* Входной поток
* Выходной поток
* Окружение
* ARGV - список аргументов первым из которых является имя команды

##### Для парсинга аргументов `grep` я использую `argparse`
