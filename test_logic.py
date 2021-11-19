import os
from parsing_logic import retrieve_files
from parsing_logic import read_file
from parsing_logic import reserved_words
from parsing_logic import get_table_name
from parsing_logic import get_dbt_fields
from parsing_logic import get_sql_fields
from parsing_logic import get_where_fields


class TestParsingServices():

    path_to_files = os.getcwd()

    def test_retrieve_files(self):
        working_results = retrieve_files(TestParsingServices.path_to_files)
        assert len(working_results) == 5
        for file in working_results:
            assert file.endswith('.sql')

    def test_read_file(self):
        results = retrieve_files(TestParsingServices.path_to_files)
        for file in results:
            content = read_file(file)
            assert isinstance(content, str)
            assert content.lower().startswith('select')
            assert not "join" in content.lower()

    def test_get_table_name(self):
        results = retrieve_files(TestParsingServices.path_to_files)
        for file in results:
            content = read_file(file)
            table_name = get_table_name(content)
            assert isinstance(table_name, str)
            assert table_name
            assert "," not in table_name
    
    def test_reserved_words(self):
        list_reserved_words = reserved_words()
        assert list_reserved_words
        assert len(list_reserved_words) == 750

    def test_get_dbt_fields(self):
        results = retrieve_files(TestParsingServices.path_to_files)
        for file in results:
            content = read_file(file)
            dbt_fields = get_dbt_fields(content)
            assert dbt_fields
            for field in dbt_fields:
                assert isinstance(field, str)
                assert not field.isnumeric()
                assert not "{{" in field and not "}}" in field
                assert not "(" in field and not ")" in field
                assert not "'" in field and not '"' in field

    def test_get_sql_fields(self):
        results = retrieve_files(TestParsingServices.path_to_files)
        for file in results:
            content = read_file(file)
            sql_fields = get_sql_fields(content)
            assert sql_fields
            for field in sql_fields:
                assert isinstance(field, str)
                assert not field.isnumeric()
                assert not "{{" in field and not "}}" in field
                assert not "(" in field and not ")" in field
                assert not "'" in field and not '"' in field

    def test_get_where_fields(self):
        results = retrieve_files(TestParsingServices.path_to_files)
        for file in results:
            content = read_file(file)
            where_fields = get_where_fields(content)
            assert where_fields
            for field in where_fields:
                assert isinstance(field, str)
                assert not field.isnumeric()
                assert not "{{" in field and not "}}" in field
                assert not "(" in field and not ")" in field
                assert not "'" in field and not '"' in field