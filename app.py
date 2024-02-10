import json

PHONEBOOK_FILE = 'phonebook.json'
ENTRIES_PER_PAGE = 5


def load_phonebook() -> dict:
    """
    Загружает данные из файла phonebook.json и возвращает список записей в справочнике.
    """
    try:
        with open(PHONEBOOK_FILE, 'r') as file:
            data: dict = json.load(file)
            return data
    except FileNotFoundError:
        return []


def save_phonebook(data) -> None:
    """
    Сохраняет список записей в справочнике в файл phonebook.json.
    """
    with open(PHONEBOOK_FILE, 'w') as file:
        json.dump(data, file, indent=2)


def display_entries(entries, page) -> None:
    """
    Выводит на экран постранично записи из справочника.
    """
    start_index = (page - 1) * ENTRIES_PER_PAGE
    end_index = start_index + ENTRIES_PER_PAGE
    page_entries = entries[start_index:end_index]

    print(f'Записи {start_index + 1}-{end_index} из {len(entries)}:')
    for entry in page_entries:
        print(entry)


def add_entry(entries) -> None:
    """
    Добавляет новую запись в справочник.
    """
    entry: dict = {}
    entry['фамилия'] = input('Введите фамилию: ')
    entry['имя'] = input('Введите имя: ')
    # Здесь можно запросить и другие поля, например, отчество, организацию, телефоны и т.д.
    entries.append(entry)
    print('Запись успешно добавлена!')


def edit_entry(entries, index):
    """
    Редактирует запись с указанным индексом в справочнике.
    """
    if (index >= 0) and (index < len(entries)):
        entry = entries[index]
        # Здесь можно предоставить пользователю возможность редактирования полей записи
        entry['фамилия'] = input('Введите новую фамилию: ')
        entry['имя'] = input('Введите новое имя: ')
        # Здесь можно запросить и другие поля для редактирования
        print('Запись успешно отредактирована!')
    else:
        print('Неверный индекс записи.')


def search_entries(entries, criteria):
    """
    Осуществляет поиск записей справочника по указанным критериям.
    """
    search_results = []
    for entry in entries:
        # Здесь можно указать условия для поиска, например, по фамилии или телефону
        if entry['фамилия'] == criteria:
            search_results.append(entry)
    if search_results:
        print('Результаты поиска:')
        for entry in search_results:
            print(entry)
    else:
        print('По заданным критериям записи не найдены.')


# Основной код программы
def main():
    # Загрузка данных из файла
    entries = load_phonebook()

    # Главный цикл программы
    while True:
        print('1. Вывод записей')
        print('2. Добавление записи')
        print('3. Редактирование записи')
        print('4. Поиск записей')
        print('0. Выход')
        choice = input('Выберите действие: ')

        if choice == '1':
            page = input('Введите номер страницы: ')
            display_entries(entries, int(page))
        elif choice == '2':
            add_entry(entries)
        elif choice == '3':
            index = input('Введите индекс записи: ')
            edit_entry(entries, int(index))
        elif choice == '4':
            criteria = input('Введите критерии поиска: ')
            search_entries(entries, criteria)
        elif choice == '0':
            break
        else:
            print('Неверный ввод. Попробуйте ещё раз.')

    # Сохранение данных в файл перед выходом
    save_phonebook(entries)


# Запуск программы
if __name__ == '__main__':
    main()
