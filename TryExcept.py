try:
    x = 10 / 0  # ⚠️ ZeroDivisionError
except Exception as e:
    print("You can't divide by zero!", e)