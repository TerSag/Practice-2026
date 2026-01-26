def int_to_string(number):
    if number == 0:
        return "0"
    
    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number) 
    
    digits = "0123456789"
    result = ""
    
    while number > 0:
        digit = number % 10 
        result = digits[digit] + result 
        number //= 10
    
    if is_negative:
        result = "-" + result
        
    return result

my_num = -456
string_res = int_to_string(my_num)

print("Число:", my_num)
print("Тип результату:", type(string_res))
print("Рядок у лапках:", f"'{string_res}'")