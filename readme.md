###  Описание проекта

Информационный бот. Производит поиск по [сайту][1] и выдаёт информацию пользователю.<br/>
Поиск происходит с набором критериев, которые определяет пользователь.


### Инструкция по запуску
* Должен быть установлен **Telegram**.
* Выполненены условия, описанные в файле ***.env.template.***
* Запустить исполняемый файл ***main.py***
    
### Описание архитектуры:
1. Папка **config_data** содержит файл ***config.py.***
    - ***config.py*** подгружает токен бота и ключ для пользования API из файла ***.env.***
    - содержит список базовых комманд, в которые можно легко внести изменения.
1. Папка **database** содержит 3 файла
   1. ***history.db*** (появляется после первого использования бота)
      + является простой базой данных, которая сохраняет
      введённую команду, время её ввода и найденные отели,
      если пользователь дошёл до конца сценария.
   1. ***hotels_data.py*** и ***users_data.py***
      + хранят временную информацию о отеле и пользователе соответственно.
1. Папка **handlers** содержит папки **custom** и **default_handlers**
   1. ***default_handlers*** содержит в себе базовые команды для бота: */start* - приветствие, */help* - выводит список команд, и эхо-команда для всех неопределнных сообщений.
   1. ***custom*** содержит в себе основные функции бота
      + Все команды для поиска отелей начинаются с base, далее идут по пользовательскому сценарию и попадают в *lowprice*,
      *highprice*, *bestdeal* или *history*. 
1. Папка **keyboards** содержит в себе 2 вида клавиатур: *inline* и *reply*
   1. В этом проекте используется только ***reply***:
      * По сути обычная клавиатура, только в виде кнопок для удобства.
   1. ***inline*** клавитура более сложный и гибкий инструмент, но здесь она не используется.
1. В папке **states** прописаны состояния пользователя через класс.
   * Используется для простоты и удобства при прохождении опроса.
1. В папке **utils** содержатся все функции для обработки запросов и вывода результатов, а так же некоторые переменные и магические числа.
1. Файл ***.env*** нужно создать исходя из инструкции в файле ***.env.template.***
1. В файл ***.gitignore*** занесены папки и файлы, изменения в которых не должны отслеживаться гитом или средой разработки. 
1. Файл ***loader.py*** инициализирует бота.
1. Файл ***main.py*** является исполняемым, то есть запускать нужно именно его, если хотите запустить бота. 
1. В файл ***requirements.txt*** занесены библиотеки, которые нужно скачать перед использованием бота.

### Скриншоты с работой бота:
* Команда /lowprice без фотографий<br/>
![](utils/lowprice_screenshots/lowprice_without_photo.png)<br/>
* Команда /lowprice с фотографиями<br/>
![](utils/lowprice_screenshots/lowprcie_photo3.png)<br/>
![](utils/lowprice_screenshots/lowprcie_photo2.png)<br/>
![](utils/lowprice_screenshots/lowprcie_photo.png)<br/>
* Команда /highprice без фотографий<br/>
![](utils/highprice_screenshots/highprice_without_photo.png)<br/>
* Команда /highprice с фотографиями<br/>
![](utils/highprice_screenshots/highprice1.png)<br/>
![](utils/highprice_screenshots/highprice2.png)<br/>
* Команда /bestdeal без фотографий<br/>
![](utils/bestdeal_screenshots/bestdeal_without_photo.png)<br/>
* Команда /bestdeal с фотографиями<br/>
![](utils/bestdeal_screenshots/bestdeal1.png)<br/>
![](utils/bestdeal_screenshots/bestdeal2.png)<br/>
* Команда /history<br/>
![](utils/history/history.png)<br/>
(Исправлено: каждый отель выводится с новой строки)

[1]: https://www.hotels.com