import requests
from requests.exceptions import JSONDecodeError, HTTPError

class EmployeeApi:
    def __init__(self, url: str) -> None:
        self.url = url
        self.token = None
    
    def get_token(self, user: str = 'raphael', password: str = 'cool-but-crude') -> str:
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(f'{self.url}/auth/login', json=creds)
        resp.raise_for_status() 
        self.token = resp.json().get("userToken")
        return self.token
    
    def get_headers(self) -> dict:
        if not self.token:
            self.get_token()
        return {"x-client-token": self.token}
    
    def get_employee_list(self, company_id: int = 0) -> tuple:
        try:
            resp = requests.get(f'{self.url}/employee', params={'company': company_id})
            resp.raise_for_status()
            json_data = resp.json()
        except (HTTPError, JSONDecodeError):
            json_data = {}
        return json_data, resp.status_code
    
    def get_employee(self, employer_id: int) -> tuple:
        try:
            resp = requests.get(f'{self.url}/employee/{employer_id}')
            resp.raise_for_status()
            json_data = resp.json()
        except (HTTPError, JSONDecodeError):
            json_data = {}
        return json_data, resp.status_code
    
    def create_employee(self, company_id: int, employee: dict) -> tuple:
        employee["companyId"] = company_id
        headers = self.get_headers()
        try:
            resp = requests.post(f'{self.url}/employee', json=employee, headers=headers)
            resp.raise_for_status()
            json_data = resp.json()
        except (HTTPError, JSONDecodeError):
            json_data = {}
        return json_data, resp.status_code
    
    def patch_employee(self, employer_id: int, updated_data: dict) -> tuple:
        headers = self.get_headers()
        try:
            resp = requests.patch(f'{self.url}/employee/{employer_id}', json=updated_data, headers=headers)
            resp.raise_for_status()
            json_data = resp.json()
        except (HTTPError, JSONDecodeError):
            json_data = {}
        return json_data, resp.status_code
