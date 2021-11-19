import re
import sys
from os import listdir
from os.path import isfile
from typing import List
from loguru import logger

def retrieve_files(dir_path: str) -> List[str]:
    """Retrieve a list of filenames in the current dir path.

    Args:
        dir_path: A string representing the current working directory.

    Returns:
        List of '.sql' format files for review.
    """
    try:
        logger.info(f"Fetching '.sql' files in '{dir_path}'")
        return [file for file in listdir(dir_path)
            if isfile(file) and file.endswith(".sql")
            ]

    except FileNotFoundError:
        logger.exception(f"Did not find the directory '{dir_path}'")
        sys.exit()


def read_file(file: str) -> str:
    """Open the file to read its content.

    Args:
        file: the name of file to read.

    Returns:
        The content of the file.
    """
    with open(f"{file}", "r") as f:
        logger.info(f"Reading data from file '{file}'")
        return f.read()


def get_table_name(file_data: str) -> str:
    """Parses the SQL query content to extract tablename.

    Args:
        file_data: The content/SQL query body in the file.

    Returns:
        cleaned_table_name: The name of the table from query.
    """
    if "from {{ source" in file_data:
        # assumes DBT follows this patterns for "FROM" clauses:
        # from {{ source('<<VALUE>>', '<<FIELD_WE_WANT>>') }}
        table_line = re.search(r"from \{\{ source\(.*'\) \}\}", file_data)
        cleaned_table_name = re.sub(r"from \{\{ source\(|'|\s|\) \}\}", "", table_line[0])
        cleaned_table_name = cleaned_table_name.split(",")[1]
        logger.info(f"Found DBT table name '{cleaned_table_name}'")

    # todo: additional logic if we have to extract more tables due to `JOIN`
    # logic to check for `FROM` and `JOIN` in the file_data

    # todo: addtl logic if we were to test a file with a pure SQL FROM clause
    elif "from " in file_data:
        # assumes the `FROM` line is on its own, after newline
        table_line = re.search(r"\nfrom\s.*\s", file_data)
        cleaned_table_name = re.sub(r"from\s|\s", "", table_line[0])
        logger.info(f"Found SQL table name '{cleaned_table_name}'")

    else:
        logger.info("Did not find a DBT or SQL table name")

    return cleaned_table_name

def reserved_words() -> List[str]:
    """Read the list of reserved words from the file `reserved_words.txt`.

    Returns:
        The list of reserved word in MySQL.
    """
    # using reserved word list for MySQL, could be changed to relevant dialect
    # https://dev.mysql.com/doc/refman/8.0/en/keywords.html
    with open("reserved_words.txt") as f:
        list_reserved_words = f.read().split()
    return [i.lower() for i in list_reserved_words]

def get_dbt_fields(file_data: str) -> List[str]:
    """Parses the SQL and extract Table fields from DBT notation.

    Args:
        file_data: The content/SQL query body in the file.

    Returns:
        dbt_fields: The list of fields extracted from DBT Jinja2.
    """
    ## DBT fields with format: `{{ null_if ('id') }}`
    dbt_fields = re.findall(r"\{\{.*\}\}", file_data)
    dbt_fields = [
        re.sub(r"\{\{\s{0,1}.*\s{0,1}\(\s{0,1}'|'\s{0,1}\)\s{0,1}\}\}", "", i)
        for i in dbt_fields
        ]
    dbt_fields = [i for i in dbt_fields if len(i.split(",")) < 2]
    dbt_fields = [re.sub(r"\(|'|\)", "", i) for i in dbt_fields]
    logger.info("Retrieving 'DBT' fields'")

    # Assumption: DBT Jinja synthax isn't subject to similar keywords
    # If that is incorrect, we can uncomment the line below
    # dbt_fields = [i for i in dbt_fields if not i.lower() in reserved_words()]
    return dbt_fields


def get_sql_fields(file_data: str) -> List[str]:
    """Parses the SQL and extract Table fields from SQL notation.

    Args:
        file_data: The content/SQL query body in the file.

    Returns:
        sql_fields: The list of fields extracted from the query.
    """
    # SQL fields with format: `field_name as field`
    sql_fields = re.findall(r",[_a-zA-Z0-9]{1,}\s{0,1}", file_data)
    sql_fields = [i for i in sql_fields if not "()" in i]
    sql_fields = [re.sub(r",|\s|\n", "", i) for i in sql_fields]
    sql_fields = [
        i for i in sql_fields
        if not i.lower() in reserved_words() and not i.isnumeric()
        ]
    logger.info("Retrieving 'SQL' fields'")
    return sql_fields

def get_where_fields(file_data: str) -> List[str]:
    """Parses the SQL and extract Table fields from WHERE clause.

    Args:
        file_data: The content/SQL query body in the file.

    Returns:
        where_fields: The list of fields extracted from the where clause.
    """
    where_fields = re.findall(r"where .*", file_data)
    where_fields = [re.sub(r"where\s", "", i.lower()) for i in where_fields]
    where_fields = [
        re.split(r"\=|in|\>|\<|\>\=|\<\=", i) for i in where_fields
        ]

    # In current deployment of the queries, the relevant table fields are
    # only in the left part of the where clause: where <<field>> <<condition>>
    where_fields = [i[0].strip() for i in where_fields]
    logger.info("Retrieving 'WHERE' fields'")
    return where_fields
 