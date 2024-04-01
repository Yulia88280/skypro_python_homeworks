def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
    
result_2024 = is_year_leap(2024)
print("год 2024:", result_2024)

result_2023 = is_year_leap(2023)
print("год 2023:", result_2023)