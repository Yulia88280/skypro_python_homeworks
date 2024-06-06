from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from typing import Dict, Any

class CompanyTable:
    """
    Класс для работы с таблицей компаний в базе данных.
    """
    __scripts = {
        "insert new": text("insert into company (\"name\", \"description\") values (:new_name, :new_description)"),
        "get max id": text("select MAX(\"id\") from company"),
        "delete by id": text("delete from company where id = :id_to_delete"),
        "select by id": text("select * from company where id = :select_id")
    }

    def __init__(self, connection_string: str) -> None:
        """
        Инициализация класса.

        :param connection_string: Строка подключения к базе данных.
        :type connection_string: str
        """
        self.__db: Engine = create_engine(connection_string)

    def create(self, name: str, description: str = "") -> None:
        """
        Создать компанию.

        :param name: Название компании.
        :type name: str
        :param description: Описание компании.
        :type description: str
        :return: None
        """
        with self.__db.connect() as conn:
            conn.execute(self.__scripts["insert new"], {"new_name": name, "new_description": description})

    def get_max_id(self) -> int:
        """
        Получить максимальный ID компании.

        :return: Максимальный ID компании.
        :rtype: int
        """
        with self.__db.connect() as conn:
            return conn.execute(self.__scripts["get max id"]).fetchone()[0]

    def delete(self, id: int) -> None:
        """
        Удалить компанию.

        :param id: ID компании.
        :type id: int
        :return: None
        """
        with self.__db.connect() as conn:
            conn.execute(self.__scripts["delete by id"], {"id_to_delete": id})

    def get_by_id(self, id: int) -> Dict[str, Any]:
        """
        Получить компанию по ID.

        :param id: ID компании.
        :type id: int
        :return: Данные компании.
        :rtype: Dict[str, Any]
        """
        with self.__db.connect() as conn:
            return dict(conn.execute(self.__scripts["select by id"], {"select_id": id}).fetchone())
