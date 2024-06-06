from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

class CompanyTable:
    __scripts = {
        "insert new": text("insert into company (\"name\", \"description\") values (:new_name, :new_description)"),
        "get max id": text("select MAX(\"id\") from company"),
        "delete by id": text("delete from company where id = :id_to_delete"),
        "select by id": text("select * from company where id = :select_id")
    }

    def __init__(self, connection_string: str) -> None:
        self.__db: Engine = create_engine(connection_string)

    def create(self, name: str, description: str = ""):
        with self.__db.connect() as conn:
            conn.execute(self.__scripts["insert new"], {"new_name": name, "new_description": description})

    def get_max_id(self):
        with self.__db.connect() as conn:
            return conn.execute(self.__scripts["get max id"]).fetchone()[0]

    def delete(self, id: int):
        with self.__db.connect() as conn:
            conn.execute(self.__scripts["delete by id"], {"id_to_delete": id})

    def get_by_id(self, id: int):
        with self.__db.connect() as conn:
            return conn.execute(self.__scripts["select by id"], {"select_id": id}).fetchone()