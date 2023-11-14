import psycopg2, os, csv
from pathlib import Path


SETTING_CONNECT_DATABASE = {
    "host": "localhost",
    "database": "north",
    "user": "postgres",
    "password": "sc1or6"
}


def get_data_from_csv(file_name='customers_data.csv'):
    path = os.path.join(Path(__file__).parent.parent, f"homework-1/north_data/{file_name}")
    data = []
    with open(path, encoding='utf8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data


def clear_table(name_table):
    with psycopg2.connect(**SETTING_CONNECT_DATABASE) as conn:
        with conn.cursor() as cur:
            request_text = f'DELETE FROM {name_table}'
            cur.execute(request_text)
        conn.commit()


def fill_table_database(name_table, data_csv):

    # Проверка на постой список
    if len(data_csv) == 0:
        return None

    with psycopg2.connect(**SETTING_CONNECT_DATABASE) as conn:
        with conn.cursor() as cur:
            for row in data_csv:
                col_values = ['%s' for i in range(len(row))]
                col_values = ", ".join(col_values)
                request_text = f'INSERT INTO {name_table} VALUES ({col_values})'
                value_cur = tuple(row.values())
                cur.execute(request_text, value_cur)
        conn.commit()


def main():

    # Получение данных их фалов csv
    customers = get_data_from_csv('customers_data.csv')
    employees = get_data_from_csv('employees_data.csv')
    orders = get_data_from_csv('orders_data.csv')

    # Очистить таблицы
    clear_table('orders')
    clear_table('employees')
    clear_table('customers')

    # Заполнение таблиц
    fill_table_database('customers', customers)
    fill_table_database('employees', employees)
    fill_table_database('orders', orders)


if __name__ == '__main__':
    main()
