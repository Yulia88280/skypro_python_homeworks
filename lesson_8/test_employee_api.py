import pytest
from employee_api import EmployeeAPI

@pytest.fixture(scope="session")
def api():
    return EmployeeAPI()

def test_authentication(api):
    """Тест для проверки авторизации"""
    assert api.auth_token is not None

def test_create_company(api):
    """Тест для метода создания компании"""
    company_data = {
        "name": "Test Company"
    }
    company = api.create_company(company_data)
    assert "id" in company
    return company

def test_get_employees(api):
    """Тест для метода получения списка сотрудников компании"""
    company_data = {
        "name": "Test Company for Employees"
    }
    company = api.create_company(company_data)
    employees = api.get_employees(company["id"])
    assert isinstance(employees, list)
    assert len(employees) == 0  # Предполагаем, что компания новая и сотрудников нет

def test_create_employee(api):
    """Тест для метода создания сотрудника"""
    company_data = {
        "name": "Test Company for Employee Creation"
    }
    company = api.create_company(company_data)
    employee_data = {
        "firstName": "Jane",
        "lastName": "Doe",
        "middleName": "B",
        "companyId": company["id"],
        "email": "jane.doe@example.com",
        "url": "http://example.com",
        "phone": "1234567890",
        "birthdate": "1990-01-01T00:00:00.000Z",
        "isActive": True
    }
    employee = api.create_employee(employee_data)
    assert "id" in employee
    return employee

def test_get_employee_by_id(api):
    """Тест для метода получения сотрудника по ID"""
    company_data = {
        "name": "Test Company for Get Employee"
    }
    company = api.create_company(company_data)
    employee_data = {
        "firstName": "John",
        "lastName": "Doe",
        "middleName": "A",
        "companyId": company["id"],
        "email": "john.doe@example.com",
        "url": "http://example.com",
        "phone": "0987654321",
        "birthdate": "1990-01-01T00:00:00.000Z",
        "isActive": True
    }
    employee = api.create_employee(employee_data)
    employee_id = employee["id"]
    fetched_employee = api.get_employee_by_id(employee_id)
    assert fetched_employee["id"] == employee_id
    assert fetched_employee["firstName"] == "John"
    assert fetched_employee["lastName"] == "Doe"
    return employee

def test_update_employee(api):
    """Тест для метода изменения информации о сотруднике"""
    company_data = {
        "name": "Test Company for Update Employee"
    }
    company = api.create_company(company_data)
    employee_data = {
        "firstName": "Alice",
        "lastName": "Smith",
        "middleName": "C",
        "companyId": company["id"],
        "email": "alice.smith@example.com",
        "url": "http://example.com",
        "phone": "1112223333",
        "birthdate": "1985-05-05T00:00:00.000Z",
        "isActive": True
    }
    employee = api.create_employee(employee_data)
    employee_id = employee["id"]
    update_data = {
        "lastName": "Johnson",
        "email": "alice.johnson@example.com",
        "url": "http://example.com",
        "phone": "1122334455",
        "isActive": False
    }
    status_code = api.update_employee(employee_id, update_data)
    assert status_code == 200
    fetched_employee = api.get_employee_by_id(employee_id)
    assert fetched_employee["lastName"] == "Johnson"
    assert fetched_employee["email"] == "alice.johnson@example.com"
    assert not fetched_employee["isActive"]

if __name__ == "__main__":
    pytest.main()