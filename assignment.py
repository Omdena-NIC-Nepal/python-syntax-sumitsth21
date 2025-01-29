def format_string(name, age):
    return (f"My name is {name} and I am {age} years old")


def conditional_check(number):
    if (number > 10):
        return ("Greater")
    elif (number < 10):
        return ("Lesser")
    else:
        return("Equal")


def loop_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum    


def list_operations(numbers):
    if not numbers:
        return (0,None,None)
    return (sum(numbers), max(numbers), min(numbers))


def dict_operations(students_dict):
    result = []
    for name,score in students_dict.items():
        if score > 80:
            result.append(name)
    return result       


def set_operations(list1, list2):
    common_elements = set()
    for item in list1:
        if item in list2:
            common_elements.add(item)
    return common_elements        


def arithmetic_ops(a, b):
    arithmetic_results = {
        'sum': a+b,
        'difference': a-b,
        'product':  a*b,
        'quotient': a/b
    }
    return arithmetic_results


def logical_ops(x, y):
    logical_results = {
        'and': x and y,
        'or': x or y,
        'not_x': not x,
        'not_y': not y,
    }
    return logical_results


def bitwise_ops(a, b):
    bitwise_results = {
        'and': a & b,
        'or': a | b,
        'xor': a ^ b,
    }
    return bitwise_results
