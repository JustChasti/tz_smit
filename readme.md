1) Развертывание проекта
    1. Настроить файл конфигурации (api/config.py) и docker-compose, при необходимости удалить существующие docker контейнеры, если названия дублируются
    2. Проверить на соответствие параметры базы данных в файле конфигурации и параметры docker-compose файла
    3. Собрать проект (ввести команду docker-compose build) и запустить проект (ввести команду docker-compose up)
2) Описание взаимодействия
Взаимодействие с проектом осуществляется через swagger по адресу: http://127.0.0.1:8000/docs#/
    1. Функция /set_rate позволяет загрузить json файл с тарифами на стоимость страхования. Пример такого файла можно найти в папке api/examples. После загрузки сервер отправит сообщение либо об успехе (rate updated) либо об ошибке (error in updating rate)
    2. Функция /get_current_rate позволяет определить значения текущего тарифа. Соответственно при запросе к ней выведется либо json структура аналогичная example.json, либо если ничего не загружено соответственно пустой список, либо сообщение об ошибке (error in getting rate)
    3. Функция /calculate_rate Позволяет рассчитать стоимость товара со страховкой отправиви дату его перевозки и его тип в соответствующих полях json запроса. Соответственно реузльтатом запроса будет json документ, с информацией о ставке тарифа и итоговой стоимостью товара вместе со страховкой. В случае внутренней ошибки, будет получена информация с ошибкой (error in calculating rate), если же пользователь ввел некорректные данные в запросе - ошибка (422 Error: Unprocessable Entity), сформированная во время валидации модлеи fastapi