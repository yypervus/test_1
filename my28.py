# -*- coding: cp1251 -*-
from my27 import get_name_doc, get_all_doc, get_number_doc, add_new_doc, documents, directories
import pytest
documents_new = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "polis", "number": "77-77", "name": 'Peter Parker'}
]



PARAMETRS1 = [(documents,documents[0]["number"], documents[0]["name"]),(documents,documents[1]["number"], documents[1]["name"]),(documents
,documents[2]["number"], documents[2]["name"])]
PARAMETRS2 = [(directories, '2207 876234', '1'), (directories, '11-2', '1'), (directories, '10006', '2')]
PARAMETRS3 = [(documents, directories, 'polis', '77-77', 'Peter Parker', '3', documents_new)]

class TestSomething:
    @pytest.mark.parametrize('document, user_input, expected', PARAMETRS1)
    def test_get_name_doc(self, document, user_input, expected):
        assert get_name_doc(document, user_input) == expected, 'Нет такого номера документа'


    def test_get_all_doc(self):
        assert get_all_doc(documents) == 'passport 2207 876234 Василий Гупкинinvoice 11-2 Геннадий Покемоновinsurance 10006 Аристарх Павлов'

    @pytest.mark.parametrize('document, user_input, expected', PARAMETRS2)
    def test_get_number_doc(self, document, user_input, expected):
        assert get_number_doc(document, user_input) == expected, 'Нет такого номера документа'

    @pytest.mark.parametrize('document1, document2, user_input1, user_input2,user_input3,user_input4, expected', PARAMETRS3)
    def test_add_new_doc(self, document1, document2, user_input1, user_input2,user_input3,user_input4, expected):
        assert add_new_doc(document1, document2, user_input1, user_input2,user_input3,user_input4) == expected