def bank(X, Y):
    r = 0.1
    
    S = X * (1 + r) ** Y
    
    return S

initial_deposit = 1000
years = 5 
final_amount = bank(initial_deposit, years)
print("Итоговая сумма на счету пользователя спустя", years, "лет:", final_amount)