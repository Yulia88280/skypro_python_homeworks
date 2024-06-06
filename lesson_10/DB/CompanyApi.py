import requests
from typing import Any, Dict, Optional

class CompanyApi:
    """
    Класс для работы с API компании.
    """

    def __init__(self, url: str) -> None:
        """
        Инициализация класса.

        :param url: URL API.
        :type url: str
        """
        self.url = url

    def get_company_list(self, params_to_add: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Получить список компаний.

        :param params_to_add: Дополнительные параметры для запроса.
        :type params_to_add: Optional[Dict[str, Any]]
        :return: Список компаний.
        :rtype: Dict[str, Any]
        """
        resp = requests.get(self.url + '/company', params=params_to_add)
        return resp.json()

    def get_token(self, user: str = 'raphael', password: str = 'cool-but-crude') -> str:
        """
        Получить токен авторизации.

        :param user: Имя пользователя.
        :type user: str
        :param password: Пароль пользователя.
        :type password: str
        :return: Токен авторизации.
        :rtype: str
        """
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]

    def _create_headers(self) -> Dict[str, str]:
        """
        Создать заголовки с токеном.

        :return: Заголовки с токеном.
        :rtype: Dict[str, str]
        """
        return {"x-client-token": self.get_token()}

    def create_company(self, name: str, description: str = "") -> Dict[str, Any]:
        """
        Добавить компанию.

        :param name: Название компании.
        :type name: str
        :param description: Описание компании.
        :type description: str
        :return: Данные созданной компании.
        :rtype: Dict[str, Any]
        """
        company = {
            "name": name,
            "description": description
        }
        headers = self._create_headers()
        resp = requests.post(self.url + '/company', json=company, headers=headers)
        return resp.json()

    def get_company(self, id: int) -> Dict[str, Any]:
        """
        Получение конкретной компании.

        :param id: ID компании.
        :type id: int
        :return: Данные компании.
        :rtype: Dict[str, Any]
        """
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()

    def edit(self, company_id: int, new_name: str, new_descr: str) -> Dict[str, Any]:
        """
        Редактирование компании.

        :param company_id: ID компании.
        :type company_id: int
        :param new_name: Новое название компании.
        :type new_name: str
        :param new_descr: Новое описание компании.
        :type new_descr: str
        :return: Данные обновленной компании.
        :rtype: Dict[str, Any]
        """
        headers = self._create_headers()
        company = {
            "name": new_name,
            "description": new_descr
        }
        resp = requests.patch(self.url + '/company/' + str(company_id), headers=headers, json=company)
        return resp.json()

    def delete(self, id: int) -> Dict[str, Any]:
        """
        Удаление компании.

        :param id: ID компании.
        :type id: int
        :return: Результат удаления компании.
        :rtype: Dict[str, Any]
        """
        headers = self._create_headers()
        resp = requests.get(self.url + '/company/delete/' + str(id), headers=headers)
        return resp.json()

    def set_active_state(self, id: int, isActive: bool) -> Dict[str, Any]:
        """
        Установить состояние активности компании.

        :param id: ID компании.
        :type id: int
        :param isActive: Состояние активности.
        :type isActive: bool
        :return: Данные обновленной компании.
        :rtype: Dict[str, Any]
        """
        headers = self._create_headers()
        resp = requests.patch(self.url + '/company/status/' + str(id), headers=headers, json={"isActive": isActive})
        return resp.json()

    def get_employee_list(self, company_id: int) -> Dict[str, Any]:
        """
        Получить список сотрудников в компании.

        :param company_id: ID компании.
        :type company_id: int
        :return: Список сотрудников.
        :rtype: Dict[str, Any]
        """
        resp = requests.get(self.url + '/employee', params={'company': str(company_id)})
        return resp.json()

    def get_employee(self, employee_id: int) -> Dict[str, Any]:
        """
        Получить сотрудника по ID.

        :param employee_id: ID сотрудника.
        :type employee_id: int
        :return: Данные сотрудника.
        :rtype: Dict[str, Any]
        """
        resp = requests.get(self.url + '/employee/' + str(employee_id))
        return resp.json()

    def create_employee(self, company_id: int, firstName: str, lastName: str, middleName: str, email: str, phone: str, birthdate: str) -> Dict[str, Any]:
        """
        Добавить сотрудника.

        :param company_id: ID компании.
        :type company_id: int
        :param firstName: Имя сотрудника.
        :type firstName: str
        :param lastName: Фамилия сотрудника.
        :type lastName: str
        :param middleName: Отчество сотрудника.
        :type middleName: str
        :param email: Email сотрудника.
        :type email: str
        :param phone: Телефон сотрудника.
        :type phone: str
        :param birthdate: Дата рождения сотрудника.
        :type birthdate: str
        :return: Данные созданного сотрудника.
        :rtype: Dict[str, Any]
        """
        employee = {
            "id": 0,
            "firstName": firstName,
            "lastName": lastName,
            "middleName": middleName,
            "companyId": company_id,
            "email": email,
            "url": "URL image",
            "phone": phone,
            "birthdate": birthdate,
            "isActive": True
        }
        headers = self._create_headers()
        resp = requests.post(self.url + '/employee', json=employee, headers=headers)
        return resp.json()

    def patch_employee(self, employee_id: int, lastName: str, email: str, phone: str, isActive: bool = True) -> Dict[str, Any]:
        """
        Изменить информацию о сотруднике.

        :param employee_id: ID сотрудника.
        :type employee_id: int
        :param lastName: Фамилия сотрудника.
        :type lastName: str
        :param email: Email сотрудника.
        :type email: str
        :param phone: Телефон сотрудника.
        :type phone: str
        :param isActive: Состояние активности сотрудника.
        :type isActive: bool
        :return: Данные обновленного сотрудника.
        :rtype: Dict[str, Any]
        """
        employee = {
            "lastName": lastName,
            "email": email,
            "url": "URL image",
            "phone": phone,
            "isActive": isActive
        }
        headers = self._create_headers()
        resp = requests.patch(self.url + '/employee/' + str(employee_id), json=employee, headers=headers)
        return resp.json()
