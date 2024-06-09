from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from typing import List, Dict, Any

class EmployeeTable:
    """
    Класс для работы с таблицей сотрудников в базе данных.
    """
    __scripts = {
        "select": text("select * from employee where company_id = :company_id"),
        "select only active": text("select * from employee where \"is_active\" = true"),
        "delete by id": text("delete from employee where id = :id_to_delete"),
        "insert new": text("insert into employee (\"first_name\", \"last_name\", \"middle_name\", \"email\", \"avatar_url\","
                           " \"phone\", \"birthdate\", \"is_active\", \"company_id\")"
                           " values (:first_name, :last_name, :middleName, :email, :url,"
                           ":phone, :birthdate, :isActive, :company_id)"),
        "get max id": text("select MAX(\"id\") from employee"),
        "select by id": text("select * from employee where id = :select_id")
    }

    def __init__(self, connection_string: str) -> None:
        """
        Инициализация класса.

        :param connection_string: Строка подключения к базе данных.
        :type connection_string: str
        """
        self.__db: Engine = create_engine(connection_string)

    def get_employee_list(self, company_id: int) -> List[Dict[str, Any]]:
        """
        Получить список сотрудников компании.

        :param company_id: ID компании.
        :type company_id: int
        :return: Список сотрудников.
        :rtype: List[Dict[str, Any]]
        """
        with self.__db.connect() as conn:
            return [dict(row) for row in conn.execute(self.__scripts["select"], {"company_id": company_id}).fetchall()]
    
    def get_employee_by_id(self, id: int) -> Dict[str, Any]:
        """
        Получить сотрудника по ID.

        :param id: ID сотрудника.
        :type id: int
        :return: Данные сотрудника.
        :rtype: Dict[str, Any]
        """
        with self.__db.connect() as conn:
            return dict(conn.execute(self.__scripts["select by id"], {"select_id": id}).fetchone())

    def delete_employee(self, id: int) -> None:
        """
        Удалить сотрудника.

        :param id: ID сотрудника.
        :type id: int
        :return: None
        """
        with self.__db.connect() as conn:
            conn.execute(self.__scripts["delete by id"], {"id_to_delete": id})

    def create_employee(self, first_name: str, last_name: str, middleName: str, email: str, url: str, phone: str, birthdate: str, isActive: bool, company_id: int) -> None:
        """
        Создать сотрудника.

        :param first_name: Имя сотрудника.
        :type first_name: str
        :param last_name: Фамилия сотрудника.
        :type last_name: str
        :param middleName: Отчество сотрудника.
        :type middleName: str
        :param email: Email сотрудника.
        :type email: str
        :param url: URL аватара сотрудника.
        :type url: str
        :param phone: Телефон сотрудника.
        :type phone: str
        :param birthdate: Дата рождения сотрудника.
        :type birthdate: str
        :param isActive: Состояние активности сотрудника.
        :type isActive: bool
        :param company_id: ID компании.
        :type company_id: int
        :return: None
        """
        with self.__db.connect() as conn:
            conn.execute(self.__scripts["insert new"], {
                "first_name": first_name,
                "last_name": last_name,
                "middleName": middleName,
                "email": email,
                "url": url,
                "phone": phone,
                "birthdate": birthdate,
                "isActive": isActive,
                "company_id": company_id
            })

    def get_max_id_employee(self) -> int:
        """
        Получить максимальный ID сотрудника.

        :return: Максимальный ID сотрудника.
        :rtype: int
        """
        with self.__db.connect() as conn:
            return conn.execute(self.__scripts["get max id"]).fetchone()[0]
