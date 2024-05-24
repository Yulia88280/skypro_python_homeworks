import pytest
import requests
from employee_api import EmployeeAPI

@pytest.fixture(scope="class")
def api():
    return EmployeeAPI()

def test_get_employees(api):
    response = api.get_employees(company_id=1)
    assert isinstance(response, list)

def test_create_employee(api):
    new_employee = {
        "firstName": "John",
        "lastName": "Doe",
        "middleName": "A",
        "companyId": 1,
        "email": "john.doe@example.com",
        "url": "http://example.com",
        "phone": "1234567890",
        "birthdate": "1990-01-01T00:00:00.000Z",
        "isActive": True
    }
    response = api.create_employee(new_employee)
    assert "id" in response

def test_get_employee_by_id(api):
    """Позитивный тест для метода GET /employee/{id}"""
    # Сначала создадим нового сотрудника для теста
    new_employee = {
        "firstName": "John",
        "lastName": "Doe",
        "middleName": "A",
        "companyId": 1,
        "email": "john.doe@example.com",
        "url": "http://example.com",
        "phone": "1234567890",
        "birthdate": "1990-01-01T00:00:00.000Z",
        "isActive": True
    }
    created_employee = api.create_employee(new_employee)
    employee_id = created_employee["id"]

    # Теперь тестируем получение сотрудника по ID
    employee = api.get_employee_by_id(employee_id)
    assert employee["id"] == employee_id

def test_update_employee(api):
    """Позитивный тест для метода PATCH /employee/{id}"""
    # Сначала создадим нового сотрудника для теста
    new_employee = {
        "firstName": "Jane",
        "lastName": "Doe",
        "middleName": "B",
        "companyId": 1,
        "email": "jane.doe@example.com",
        "url": "http://example.com",
        "phone": "0987654321",
        "birthdate": "1991-01-01T00:00:00.000Z",
        "isActive": True
    }
    created_employee = api.create_employee(new_employee)
    employee_id = created_employee["id"]

    # Теперь тестируем обновление данных сотрудника
    update_data = {
        "lastName": "Smith",
        "email": "jane.smith@example.com",
        "url": "http://example.com",
        "phone": "1122334455",
        "isActive": False
    }
    updated_employee = api.update_employee(employee_id, update_data)
    assert updated_employee["lastName"] == update_data["lastName"]

def test_create_employee_without_required_fields(api):
    """Тест для проверки обязательности полей в методе POST /employee"""
    incomplete_employee = {
        "firstName": "John"
    }
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        api.create_employee(incomplete_employee)
    assert excinfo.value.response.status_code == 400

def test_get_employee_with_invalid_id(api):
    """Тест для проверки получения сотрудника с несуществующим ID"""
    invalid_id = 9999  # Несуществующий ID
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        api.get_employee_by_id(invalid_id)
    assert excinfo.value.response.status_code == 404

if __name__ == "__main__":
    pytest.main()
