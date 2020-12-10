# Задание №6
# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(text):
    """
    Функция int_func(), принимает слово из маленьких латинских букв и возвращает его же, но с прописной первой буквой
    :param text: слово из маленьких букв
    :return: входное слово с прописной первой буквой
    """
    return str(text).capitalize()


print(int_func('text'))

# Продолжим работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

string = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tenetur deleniti deserunt eius. ' \
         'Pariatur quasi qui, dolore unde. Quisquam mollitia aliquam vel nihil, rerum. Dolorum nam maiores, ' \
         'necessitatibus, magni saepe voluptates est optio distinctio dicta cum rem voluptatum libero natus nemo,' \
         ' ea quaerat consectetur aspernatur facere voluptas nisi alias beatae eligendi.'
cap_string = list()
for word in string.split():
    cap_string.append(int_func(word))
print(' '.join(cap_string))
