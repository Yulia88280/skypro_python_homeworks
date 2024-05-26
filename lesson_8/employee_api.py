import requests

BASE_URL = "https://x-clients-be.onrender.com"
AUTH_URL = f"{BASE_URL}/auth/login"
COMPANY_URL = f"{BASE_URL}/company"
EMPLOYEE_URL = f"{BASE_URL}/employee"

USERNAME = "leonardo"
PASSWORD = "leads"

class EmployeeAPI:
    def __init__(self):
        self.auth_token = self.authenticate()
        self.headers = {
            "x-client-token": self.auth_token,
            "Content-Type": "application/json"
        }

    def authenticate(self):
        """Метод для получения токена авторизации"""
        response = requests.post(AUTH_URL, json={"username": USERNAME, "password": PASSWORD})
        response.raise_for_status()
        return response.json()["userToken"]

    def create_company(self, company_data):
        """Метод для создания новой компании"""
        response = requests.post(COMPANY_URL, json=company_data, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_employees(self, company_id):
        """Метод для получения списка сотрудников"""
        response = requests.get(EMPLOYEE_URL, params={"company": company_id}, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_employee(self, employee_data):
        """Метод для создания нового сотрудника"""
        response = requests.post(EMPLOYEE_URL, json=employee_data, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_employee_by_id(self, employee_id):
        """Метод для получения сотрудника по ID"""
        response = requests.get(f"{EMPLOYEE_URL}/{employee_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_employee(self, employee_id, update_data):
        """Метод для обновления информации о сотруднике"""
        response = requests.patch(f"{EMPLOYEE_URL}/{employee_id}", json=update_data, headers=self.headers)
        response.raise_for_status()
        return response.status_code
