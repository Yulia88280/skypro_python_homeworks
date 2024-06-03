import requests
from typing import Any, Dict, Optional

class CompanyApi:
    # Инициализация
    def __init__(self, url: str) -> None:
        self.url = url

    # Получить список компаний
    def get_company_list(self, params_to_add: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        resp = requests.get(self.url + '/company', params=params_to_add)
        return resp.json()
    
    # Получить токен авторизации
    def get_token(self, user: str = 'raphael', password: str = 'cool-but-crude') -> str:
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
    
    # Создать заголовки с токеном
    def _create_headers(self) -> Dict[str, str]:
        return {"x-client-token": self.get_token()}
    
    # Добавить компанию
    def create_company(self, name: str, description: str = "") -> Dict[str, Any]:
        company = {
            "name": name,
            "description": description
        }
        headers = self._create_headers()
        resp = requests.post(self.url + '/company', json=company, headers=headers)
        return resp.json()
    
    # Получение конкретной компании
    def get_company(self, id: int) -> Dict[str, Any]:
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()

    # Редактирование компании
    def edit(self, company_id: int, new_name: str, new_descr: str) -> Dict[str, Any]:
        headers = self._create_headers()
        company = {
            "name": new_name,
            "description": new_descr
        }
        resp = requests.patch(self.url + '/company/' + str(company_id), headers=headers, json=company)
        return resp.json()
    
    # Удаление компании
    def delete(self, id: int) -> Dict[str, Any]:
        headers = self._create_headers()
        resp = requests.get(self.url + '/company/delete/' + str(id), headers=headers)
        return resp.json()
    
    # Установить состояние активности компании
    def set_active_state(self, id: int, isActive: bool) -> Dict[str, Any]:
        headers = self._create_headers()
        resp = requests.patch(self.url + '/company/status/' + str(id), headers=headers, json={"isActive": isActive})
        return resp.json()
    
    # Получить список сотрудников в компании
    def get_employee_list(self, company_id: int) -> Dict[str, Any]:
        resp = requests.get(self.url + '/employee', params={'company': str(company_id)})
        return resp.json()
    
    # Получить сотрудника по id
    def get_employee(self, employee_id: int) -> Dict[str, Any]:
        resp = requests.get(self.url + '/employee/' + str(employee_id))
        return resp.json()
    
    # Добавить сотрудника
    def create_employee(self, company_id: int, firstName: str, lastName: str, middleName: str, email: str, phone: str, birthdate: str) -> Dict[str, Any]:
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
    
    # Изменить информацию о сотруднике
    def patch_employee(self, employee_id: int, lastName: str, email: str, phone: str, isActive: bool = True) -> Dict[str, Any]:
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