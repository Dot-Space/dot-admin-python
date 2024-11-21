# Dot. Admin
## Описание
Библиотека упрощающая работу и содержащая в себе базовые паттерны проектирования API для сайтов.
Включает в себя как базовый функционал (авторизация, логирование, работа с правами),
так и дополнительные (работа с кэшем, асинхронными задачами и очередями, генерация отчётов)

## Модули
Библиотека содержит следующие модули:

- `core` - Базовые модули на основе которых работает вся библиотека
- `authentication` - Модуль для работы с авторизацией
- `adapter` - Работа с переводом разных типов данных
- `analytics` - Модуль для работы с аналитикой веб-сайта
- `filters` - Модуль работы с кастомной фильтрацией
- `permissions` - Модуль для работы с правами
- `reports` - Модуль для генерации отчётов
- `tasks` - Модуль для работы с асинхронными задачами и очередями
- `email` - Модуль для работы с оповещениями и рассылками
- `ecommerce` - Базовые компоненты работы с коммерцией
- `cli` - Консольные утилиты

### Core
    