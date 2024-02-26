"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


if __name__ == '__main__':
    with psycopg2.connect(host="localhost", database="north", user="postgres", password="test123") as connect:
        with connect.cursor() as cursor:
            with open('north_data/customers_data.csv', 'r') as file:
                csvreader = csv.DictReader(file)
                for row in csvreader:
                    cursor.execute("INSERT INTO customers VALUES (%s, %s, %s)", tuple(row.values()))
                cursor.execute("SELECT * FROM customers")

            with open('north_data/employees_data.csv', 'r') as file:
                csvreader = csv.DictReader(file)
                for row in csvreader:
                    cursor.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", tuple(row.values()))
                cursor.execute("SELECT * FROM employees")

            with open('north_data/orders_data.csv', 'r') as file:
                csvreader = csv.DictReader(file)
                for row in csvreader:
                    cursor.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", tuple(row.values()))
                cursor.execute("SELECT * FROM orders")

            connect.commit()