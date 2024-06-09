import requests
from requests.exceptions import JSONDecodeError, HTTPError
from typing import Tuple, Dict, Any

class EmployeeApi:
    """
    Класс для работы с API сотрудников.
    """

    def __init__(self, url: str) -> None:
        """
        Инициализация класса.

        :param url: URL API.
        :type url: str
        """
        self.url = url
        self.token = None
    
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
        resp = requests.post(f'{self.url}/auth/login', json=creds)
        resp.raise_for_status()
        self.token = resp.json().get("userToken")
        return self.token
    
    def get_headers(self) -> Dict[str, str]:
        """
        Создать заголовки с токеном.

        :return: Заголовки с токеном.
        :rtype: Dict[str, str]
        """
        if not self.token:
            self.get_token()
        return {"x-client-token": self.token}
    
    def get_employee_list(self, company_id: int = 0) -> Tuple[Dict[str, Any], int]:
        """
        Получить список сотрудников компании.

        :param company_id: ID компании.
        :type company_id: int
        :return: Список сотрудников и статус код.
        :rtype: Tuple[Dict[str, Any], int]
        """
        try:
            resp = requests.get(f'{self.url}/employee', params={'company': company_id})
            resp.raise_for_status()
            json_data = resp.json()
        except (HTTPError, JSONDecodeError):
            json_data = {}
        return json_data, resp.status_code
    
    def get_employee(self, employer_id: int) -> Tuple[Dict[str, Any], int]:
        """
        Получить данные сотрудника по ID.

        :param employer_id: ID сотрудника.
        :type employer_id: int
        :return: Данные сотрудника и статус код.
        :rtype: Tuple[Dict[str, Any], int]
        """
        try:
            resp = requests.get(f'{self.url}/employee/{employer_id}')
            resp.raise_for_status()
            json_data = resp.json()
        except (HTTPError, JSONDecodeError):
            json_data = {}
        return json_data, resp.status_code
    
    def create_employee(self, company_id: int, employee: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        """
        Создать сотрудника.

        :param company_id: ID компании.
        :type company_id: int
        :param employee: Данные сотрудника.
        :type employee: Dict[str, Any]
        :return: Данные созданного сотрудника и статус код.
        :rtype: Tuple[Dict[str, Any], int]
        """
        employee["companyId"] = company_id
        headers = self.get_headers()
        try:
            resp = requests.post(f'{self.url}/employee', json=employee, headers=headers)
            resp.raise_for_status()
            json_data = resp.json()
        except (HTTPError, JSONDecodeError):
            json_data = {}
        return json_data, resp.status_code
    
    def patch_employee(self, employer_id: int, updated_data: Dict[str, Any]) -> Tuple[Dict[str, Any], int]:
        """
        Обновить данные сотрудника.

        :param employer_id: ID сотрудника.
        :type employer_id: int
        :param updated_data: Обновленные данные сотрудника.
        :type updated_data: Dict[str, Any]
        :return: Данные обновленного сотрудника и статус код.
        :rtype: Tuple[Dict[str, Any], int]
        """
        headers = self.get_headers()
        try:
            resp = requests.patch(f'{self.url}/employee/{employer_id}', json=updated_data, headers=headers)
            resp.raise_for_status()
            json_data = resp.json()
        except (HTTPError, JSONDecodeError):
            json_data = {}
        return json_data, resp.status_code
