import os
import json
from loguru import logger
from parsing_logic import retrieve_files
from parsing_logic import read_file
from parsing_logic import get_table_name
from parsing_logic import get_dbt_fields
from parsing_logic import get_sql_fields
from parsing_logic import get_where_fields

def main():

    # retrieve all .sql file in current dir
    path_to_files = os.getcwd()
    all_files = retrieve_files(path_to_files)

    # initialize dict for tracking relevant tables & fields
    relevant_data = {"tables": []}

    if all_files:
        for file in all_files:
            data = read_file(file)

            table_name = get_table_name(data)
            relevant_data["tables"].append(table_name)

            if not table_name in relevant_data:
                relevant_data[table_name] = []

            # if table exists already as dict key, then add to it
            relevant_data[table_name].extend(get_dbt_fields(data))
            relevant_data[table_name].extend(get_sql_fields(data))
            relevant_data[table_name].extend(get_where_fields(data))

            # go thru all the fields captured and remove the duplicate entries
            for key, values in relevant_data.items():
                if isinstance(values, list):
                    # todo: evaluate if case sensitivity is important to handle
                    # "fieldname" and "fieldName" in the de-duplication.
                    relevant_data[key] = list(set(relevant_data[key]))
                    logger.info("Removed possible duplicate fields "
                                + f"from table '{key}'")

        logger.success(f"Script found {len(relevant_data.keys())-1} "
                        + "tables in the .sql files:")
        logger.success(f"Tables:\t{relevant_data['tables']}")
        with open("result_file.json", 'w') as file:
            json.dump(relevant_data, file)
    else:
        logger.exception(f"No 'sql' file found in {path_to_files}")

if __name__=="__main__":
    main()
