import os
# For Task 1 and 2
path = os.path.join(os.getcwd(), 'recipes.txt')
# For Task 3
file_path_first = os.path.join(os.getcwd(), '1.txt')
file_path_second = os.path.join(os.getcwd(), '2.txt')
file_path_third = os.path.join(os.getcwd(), '3.txt')
file_path_sorted_result = os.path.join(os.getcwd(), 'sorted_result.txt')


def get_data(file_path):
    with open(file_path, encoding='UTF-8') as file:
        result = {}
        for food in file:
            food_name = food.strip()
            ing_num = int(file.readline().strip())
            temp_data = []
            for _ in range(ing_num):
                ingredient_name, quantity, measure = file.readline().split('|') 
                temp_data.append({'ingredient_name': ingredient_name.strip(), 
                'quantity': int(quantity.strip()), 'measure': measure.strip()})
            result[food_name] = temp_data
            file.readline()
        return result

# Task 1 cook_book is ready
cook_book = get_data(path)

def get_shop_list_by_dishes(dishes, person_count, xbook=cook_book):
    result = {}
    for item in range(len(dishes)):
        if dishes[item] in xbook:
          for list_ing in xbook[dishes[item]]:
            if list_ing['ingredient_name'] in result:
              r = result[list_ing['ingredient_name']]['quantity'] + list_ing['quantity'] * person_count
              result[list_ing['ingredient_name']].update({'quantity': r})
            else:
              result[list_ing['ingredient_name']] = {'measure': list_ing['measure'], 
              'quantity': list_ing['quantity'] * person_count }
    return result         
# Task 2
print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 5))



# Task 3 
def get_data(file_path):
  try:
    file_name = os.path.basename(file_path)
    without_extension = os.path.splitext(file_name)[0]
  except:
    'Wrong Path File'
  with open(file_path, encoding='UTF-8') as file:
    temp_list, count = [], 1
    for _ in file:
      temp_list.append(f'Строка номер {count} файла номер {without_extension}')
      count +=1
    return {file_name: {count - 1: temp_list}}


def sorting_data(*args):
  try:
    num_lines = [key for arg in args for line_num in arg.values() for key in line_num]
    num_lines.sort()
    result = [fl for num in range(len(num_lines)) for fl in args for data in fl.values() 
    for key in data if num_lines[num] == key]
    return result
  except ValueError:
    return 'data not defined'
  except AttributeError:
    return'data must be dict based, AttributeError :('


def load(file_path, data):
  with open(file_path, mode='a', encoding='utf-8') as load:
    for item in range(len(data)):
      for file_name, values in data[item].items():
        load.write(file_name)
        load.write('\n')
        for key, lines in values.items():
          load.write(str(key))
          load.write('\n')
          for line in lines:
            load.write(line)
            load.write('\n')

# Getting all data from files
first_data_file = get_data(file_path_first)
third_data_file = get_data(file_path_third)
second_data_file = get_data(file_path_second)
# Sorting those tables
sorted_one = sorting_data(third_data_file, second_data_file, first_data_file)
# Loading to sorted_result file            
load(file_path_sorted_result, sorted_one)
