from src.operations import search_by_string
from src.processing import filters_by_state, sort_by_data
from src.transactions import transactions_csv, transactions_excel
from src.utils import transactions_function
from src.widget import get_date, mask_account_card


def checking_exceptions_sorting(dict_: dict) -> bool:
    try:
        if dict_["currency_code"] == "RUB":
            return True
        else:
            return False
    except KeyError:
        if dict_["operationAmount"]["currency"]["code"] == "RUB":
            return True
        else:
            return False


def main():
    select_file_for_processing = int(input(
    "Привет! Добро пожаловать в программу работы с банковскими транзакциями. "
    "\nВыберите необходимый пункт меню: "
    "\n1.Получить информацию о транзакциях из JSON-файла"
    "\n2.Получить информацию о транзакциях из CSV-файла"
    "\n3.Получить информацию о транзакциях из XLSX-файла"
    "\nВвод: "))
    if select_file_for_processing == 1:
        print("Для обработки выбран JSON-файл.")
        transactions = transactions_function("../data/operations.json")
    elif select_file_for_processing == 2:
        print("Для обработки выбран CSV-файл.")
        transactions = transactions_csv("../data/transactions.csv")
    elif select_file_for_processing == 3:
        print("Для обработки выбран XLSX-файл.")
        transactions = transactions_excel("../data/transactions_excel.xlsx")

    print(
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )

    list_status = ["EXECUTED", "CANCELED", "PENDING"]

    input_user_status = ""
    while input_user_status not in list_status:
        input_user_status = input("Введите статус: ").upper()

    status = filters_by_state(transactions, input_user_status)

    print("Отсортировать операции по дате? 'Да' или 'Нет'")

    input_user_date = input("Введите 'Да' или 'Нет': ")

    if input_user_date.lower() == "да":
        print("Отсортировать по возрастанию или по убыванию?")

        input_user_ascending = input("Введите 'по возрастанию' или 'по убыванию': ").lower()
        if input_user_ascending == "по возрастанию":
            sorted_list = sort_by_data(status, False)
        elif input_user_ascending == "по убыванию":
            sorted_list = sort_by_data(status, True)
        else:
            sorted_list = sort_by_data(status)
    else:
        sorted_list = status

    print("Выводить только рублевые транзакции? 'Да' или 'Нет'")

    input_user_filter = input("Введите 'Да' или 'Нет': ").lower()

    if input_user_filter == "да":
        filter_rub = list(filter(lambda x: checking_exceptions_sorting(x), sorted_list))
    else:
        filter_rub = sorted_list

    print("Отфильтровать список транзакций по определенному слову в описании? 'Да' или 'Нет'?: ")

    input_user_word = input("Введите 'Да' или 'Нет': ").lower()

    if input_user_word == "да":
        word = input("Введите слово по которому пройдет фильтрация: ")
        filter_word = search_by_string(filter_rub, word)

        if filter_word == "Совпадений не найдено!":
            print("Совпадений не найдено!")
            filter_word = filter_rub
    else:
        filter_word = filter_rub

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filter_word)}")

    if len(filter_word) == 0:
        for trans in filter_word:
            if trans["description"] in "Открытие вклада" in trans["description"]:
                print(f"{get_date(trans['date'])} Открытие вклада\n{mask_account_card(trans['to'])}"
                      f"\nСумма:{trans['amount']}\n")
            else:
                print(f"{get_date(trans['date'])} {trans['description']}\n{mask_account_card(trans['from'])} -> "
                      f"{mask_account_card(trans['to'])}\nСумма: {trans['amount']} {trans['currency_code']}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


print(main())
