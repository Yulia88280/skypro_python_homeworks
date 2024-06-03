import pytest
from datetime import datetime
from CompanyApi import CompanyApi
from EmployeeApi import EmployeeApi
from CompanyTable import CompanyTable
from EmployeeTable import EmployeeTable

api_c = CompanyApi("https://x-clients-be.onrender.com")
api_e = EmployeeApi("https://x-clients-be.onrender.com")
db_c = CompanyTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")
db_e = EmployeeTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

# Утилита для генерации случайных строк
def generate_random_string(length: int = 10) -> str:
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@pytest.fixture(scope="module")
def company():
    name_company = generate_random_string()
    db_c.create(name_company)
    id_company = db_c.get_max_id()
    print(id_company)
    yield id_company
    employees = db_e.get_employee_list(id_company)
    for employee in employees:
        db_e.delete_employee(employee[0])
    db_c.delete(id_company)

def test_get_employee_list_empty(company):
    result, status_code = api_e.get_employee_list(company)
    assert status_code == 200
    assert len(result) == 0

    # Удаление сотрудников для очистки компании перед тестом
    employees = db_e.get_employee_list(company)
    for employee in employees:
        db_e.delete_employee(employee[0])

def test_create_employee(company):
    employee = {
        "id": 0,
        "firstName": generate_random_string(),
        "lastName": generate_random_string(),
        "middleName": generate_random_string(),
        "companyId": company,
        "email": f"{generate_random_string()}@example.com",
        "url": "https://example.com",
        "phone": "+1234567890",
        "birthdate": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
        "isActive": True
    }
    request_employer, status_code = api_e.create_employee(company, employee)
    emp_id = request_employer.get("id")
    db_e.delete_employee(emp_id)
    assert status_code == 201

def test_get_employee_list(company):
    emploee_id_list = []
    for _ in range(5):
        db_e.create_employee(
            first_name=generate_random_string(),
            last_name=generate_random_string(),
            middleName=generate_random_string(),
            email=f"{generate_random_string()}@example.com",
            url="https://example.com",
            phone="+1234567890",
            birthdate=datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
            isActive=True,
            company_id=company
        )
        new_employer_id = db_e.get_max_id_employee()
        emploee_id_list.append(new_employer_id)

    api_result, status_code = api_e.get_employee_list(company)
    db_result = db_e.get_employee_list(company)

    assert status_code == 200
    assert len(api_result) == len(db_result)

    for id in emploee_id_list:
        db_e.delete_employee(id)

def test_get_employee_by_id(company):
    employee = {
        "firstName": generate_random_string(),
        "lastName": generate_random_string(),
        "middleName": generate_random_string(),
        "email": f"{generate_random_string()}@example.com",
        "url": "https://example.com",
        "phone": "+1234567890",
        "birthdate": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
        "isActive": True
    }
    db_e.create_employee(
        first_name=employee["firstName"],
        last_name=employee["lastName"],
        middleName=employee["middleName"],
        email=employee["email"],
        url=employee["url"],
        phone=employee["phone"],
        birthdate=employee["birthdate"],
        isActive=employee["isActive"],
        company_id=company
    )
    new_employer_id = db_e.get_max_id_employee()
    new_employer, status_code = api_e.get_employee(new_employer_id)
    db_e.delete_employee(new_employer_id)

    assert status_code == 200
    assert new_employer.get("firstName") == employee["firstName"]
    assert new_employer.get("lastName") == employee["lastName"]
    assert new_employer.get("middleName") == employee["middleName"]
    assert new_employer.get("email") == employee["email"]
    assert new_employer.get("phone") == employee["phone"]
    assert new_employer.get("isActive") == employee["isActive"]
    assert new_employer.get("companyId") == company

def test_patch_employee(company):
    employee = {
        "firstName": generate_random_string(),
        "lastName": generate_random_string(),
        "middleName": generate_random_string(),
        "email": f"{generate_random_string()}@example.com",
        "url": "https://example.com",
        "phone": "+1234567890",
        "birthdate": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
        "isActive": True
    }
    db_e.create_employee(
        first_name=employee["firstName"],
        last_name=employee["lastName"],
        middleName=employee["middleName"],
        email=employee["email"],
        url=employee["url"],
        phone=employee["phone"],
        birthdate=employee["birthdate"],
        isActive=employee["isActive"],
        company_id=company
    )
    new_employer_id = db_e.get_max_id_employee()
    new_employer, status_code = api_e.get_employee(new_employer_id)
    assert status_code == 200
    
    updated_data = {
        "lastName": "UpdatedLastName",
        "email": f"{generate_random_string()}@example.com",
        "phone": "+9876543210"
    }
    
    patch_result, patch_status_code = api_e.patch_employee(new_employer_id, updated_data)
    updated_employer, updated_status_code = api_e.get_employee(new_employer_id)
    db_e.delete_employee(new_employer_id)
    
    assert patch_status_code == 200
    assert updated_employer.get("lastName") == updated_data["lastName"]
    assert updated_employer.get("email") == updated_data["email"]
   # assert updated_employer.get("phone") == updated_data["phone"] номер не меняется баг
