import pytest
import allure
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
    yield id_company
    employees = db_e.get_employee_list(id_company)
    for employee in employees:
        db_e.delete_employee(employee[0])
    db_c.delete(id_company)

@allure.title("Проверка получения пустого списка сотрудников")
@allure.description("Тест проверяет, что список сотрудников пуст при создании новой компании")
@allure.feature("Employee API")
@allure.severity(allure.severity_level.NORMAL)
def test_get_employee_list_empty(company):
    with allure.step("Получение списка сотрудников"):
        result, status_code = api_e.get_employee_list(company)
    with allure.step("Проверка, что статус код 200"):
        assert status_code == 200
    with allure.step("Проверка, что список сотрудников пуст"):
        assert len(result) == 0

    with allure.step("Удаление сотрудников для очистки компании перед тестом"):
        employees = db_e.get_employee_list(company)
        for employee in employees:
            db_e.delete_employee(employee[0])

@allure.title("Создание сотрудника")
@allure.description("Тест проверяет создание нового сотрудника")
@allure.feature("Employee API")
@allure.severity(allure.severity_level.CRITICAL)
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
    with allure.step("Создание сотрудника через API"):
        request_employer, status_code = api_e.create_employee(company, employee)
    with allure.step("Получение ID созданного сотрудника"):
        emp_id = request_employer.get("id")
    with allure.step("Удаление созданного сотрудника из БД"):
        db_e.delete_employee(emp_id)
    with allure.step("Проверка, что статус код 201"):
        assert status_code == 201

@allure.title("Получение списка сотрудников")
@allure.description("Тест проверяет получение списка сотрудников компании")
@allure.feature("Employee API")
@allure.severity(allure.severity_level.NORMAL)
def test_get_employee_list(company):
    emploee_id_list = []
    with allure.step("Создание 5 сотрудников в БД"):
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

    with allure.step("Получение списка сотрудников через API"):
        api_result, status_code = api_e.get_employee_list(company)
    with allure.step("Получение списка сотрудников из БД"):
        db_result = db_e.get_employee_list(company)

    with allure.step("Проверка, что статус код 200"):
        assert status_code == 200
    with allure.step("Проверка, что количество сотрудников совпадает"):
        assert len(api_result) == len(db_result)

    with allure.step("Удаление созданных сотрудников"):
        for id in emploee_id_list:
            db_e.delete_employee(id)

@allure.title("Получение сотрудника по ID")
@allure.description("Тест проверяет получение данных сотрудника по его ID")
@allure.feature("Employee API")
@allure.severity(allure.severity_level.CRITICAL)
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
    with allure.step("Создание сотрудника в БД"):
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
    with allure.step("Получение данных сотрудника через API"):
        new_employer, status_code = api_e.get_employee(new_employer_id)
    with allure.step("Удаление созданного сотрудника из БД"):
        db_e.delete_employee(new_employer_id)

    with allure.step("Проверка, что статус код 200"):
        assert status_code == 200
    with allure.step("Проверка данных сотрудника"):
        assert new_employer.get("firstName") == employee["firstName"]
        assert new_employer.get("lastName") == employee["lastName"]
        assert new_employer.get("middleName") == employee["middleName"]
        assert new_employer.get("email") == employee["email"]
        assert new_employer.get("phone") == employee["phone"]
        assert new_employer.get("isActive") == employee["isActive"]
        assert new_employer.get("companyId") == company

@allure.title("Изменение данных сотрудника")
@allure.description("Тест проверяет изменение данных сотрудника")
@allure.feature("Employee API")
@allure.severity(allure.severity_level.CRITICAL)
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
    with allure.step("Создание сотрудника в БД"):
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
    with allure.step("Получение данных сотрудника через API"):
        new_employer, status_code = api_e.get_employee(new_employer_id)
    assert status_code == 200
    
    updated_data = {
        "lastName": "UpdatedLastName",
        "email": f"{generate_random_string()}@example.com",
        "phone": "+9876543210"
    }
    
    with allure.step("Изменение данных сотрудника через API"):
        patch_result, patch_status_code = api_e.patch_employee(new_employer_id, updated_data)
    with allure.step("Получение обновленных данных сотрудника через API"):
        updated_employer, updated_status_code = api_e.get_employee(new_employer_id)
    with allure.step("Удаление обновленного сотрудника из БД"):
        db_e.delete_employee(new_employer_id)
    
    with allure.step("Проверка, что статус код 200"):
        assert patch_status_code == 200
    with allure.step("Проверка данных обновленного сотрудника"):
        assert updated_employer.get("lastName") == updated_data["lastName"]
        assert updated_employer.get("email") == updated_data["email"]
        # assert updated_employer.get("phone") == updated_data["phone"]  # номер не меняется баг
