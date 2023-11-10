
def data_type_checker(val):
    res = type(val).__name__
    return str(res)

final_result = data_type_checker(12)
print(final_result)