from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

class EmployeeTable:
    __scripts = {
        "select": text("select * from employee where company_id =:company_id"),
        "select only active": text("select * from employee where \"is_active\" = true"),
        "delete by id": text("delete from employee where id =:id_to_delete"),
        "insert new": text("insert into employee (\"first_name\", \"last_name\", \"middle_name\", \"email\", \"avatar_url\","
                           " \"phone\", \"birthdate\", \"is_active\", \"company_id\")"
                           " values (:first_name, :last_name, :middleName, :email, :url,"
                           ":phone, :birthdate, :isActive, :company_id)"),
        "get max id": text("select MAX(\"id\") from employee"),
        "select by id": text("select * from employee where id =:select_id")
    }

    def __init__(self, connection_string: str) -> None:
        self.__db: Engine = create_engine(connection_string)

    def get_employee_list(self, company_id: int):
        with self.__db.connect() as conn:
            return conn.execute(self.__scripts["select"], {"company_id": company_id}).fetchall()
    
    def get_employee_by_id(self, id: int):
        with self.__db.connect() as conn:
            return conn.execute(self.__scripts["select by id"], {"select_id": id}).fetchall()

    def delete_employee(self, id: int):
        with self.__db.connect() as conn:
            conn.execute(self.__scripts["delete by id"], {"id_to_delete": id})

    def create_employee(self, first_name: str, last_name: str, middleName: str, email: str, url: str, phone: str, birthdate: str, isActive: bool, company_id: int):
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

    def get_max_id_employee(self):
        with self.__db.connect() as conn:
            return conn.execute(self.__scripts["get max id"]).fetchone()[0]