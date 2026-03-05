def even_or_odd(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def number_to_string(num):
    

    return str(num)


def no_space(x):
    return x.replace(" ", "")

def get_count(string):
  return sum(1 for char in string if char in 'aeiouAEIOU')