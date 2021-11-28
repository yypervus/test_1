documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def add_new_doc(documents_1, directories_1, user_type, user_number, user_name, user_shelf):
    '''Функция добавления в каталог'''
    new_dict_doc = {}
    new_dict_doc.setdefault('type', user_type)
    new_dict_doc.setdefault('number', user_number)
    new_dict_doc.setdefault('name', user_name)
    documents_1.append(new_dict_doc)
    return documents_1


def get_name_doc(documents_1, user_input):
    '''Функция поиска ФИО по номеру документа'''
    for document in documents_1:
        if user_input == document['number']:
            doc_name = document['name']
            return doc_name
        else:
            number_shelf = 'Нет такого номера документа'
    return number_shelf


def get_number_doc(directories_1, user_input):
    '''Функция поиска полки по номеру документа'''
    for id, number_doc in enumerate(directories_1.values()):
        if user_input in number_doc:
            number_id = id
            number_shelf = list(directories_1.keys())[number_id]
            return number_shelf
        else:
            number_shelf = 'Нет такого номера документа'
    return number_shelf


def get_all_doc(documents_1):
    '''Функция вывода всех документов'''
    f = ''
    for document in documents_1:
        doc_file = list(document.values())
        res = ' '
        all_doc = res.join(doc_file)
        f += all_doc
    return f




