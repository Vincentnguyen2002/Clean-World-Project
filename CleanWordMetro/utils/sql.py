from config import connection

def executeSql(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

import importlib.util
import sys

# For illustrative purposes.
# name = 'city'
#
# if name in sys.modules:
#     print(f"{name!r} already in sys.modules")
# elif (spec := importlib.util.find_spec(name)) is not None:
#     # If you chose to perform the actual import ...
#     module = importlib.util.module_from_spec(spec)
#     sys.modules[name] = module
#     spec.loader.exec_module(module)
#     print(f"{name!r} has been imported")
# else:
#     print(f"can't find the {name!r} module")

