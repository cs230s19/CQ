import json

import openpyxl


def update_storage(actions, store):
    """
    Updates the JSON store with the actions contained in the actions paramete

    :param actions: list of Python dictionaries containing actions that may be added
    :param store: Kivy JSON store
    :return: does not return, updates JSON storage file
    """

    # Excel headers (for reference)
    # Action and Category, Repeat?, Drive, Knowledge, Strategy, Action, Maximum?, Times Completed
    for action in actions:
        try:
            store.put(action['Action and Category'], Repeat=action['Repeat?'], Drive=action['Drive'],
                      Knowledge=action['Knowledge'], Strategy=action['Strategy'], Action=action['Action'],
                      Maximum=action['Maximum?'], Completed=action['Times Completed'])
        except Exception as e:
            print("Unable to add action to store: {}".format(e))


def store_to_excel(store, filename):
    """
    Converts the contents of the JSON store to an excel file and
    saves the excel file in the current directory

    :param store: kivy JSON store
    :param filename: name of excel file to export
    :return: does not return - creates an excel file in the current directory
    """
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = "CQ"
    worksheet.insert_rows(0)
    worksheet.insert_cols(0, 7)

    # How the headers look in the excel file
    ws_headers = ["Action and Category", "Repeat?", "Drive", "Knowledge", "Strategy", "Action",
                  "Maximum?", "Times Completed"]

    # How the headers were entered into the store
    store_keys = ["Action and Category", "Repeat", "Drive", "Knowledge", "Strategy", "Action",
                  "Maximum", "Completed"]

    header_idx = 0
    for cell in tuple(worksheet.rows)[0]:
        cell.value = ws_headers[header_idx]
        header_idx += 1

    for key, entry in store.find():
        cell_idx = 0
        row = []
        for cell in tuple(worksheet.rows)[worksheet.max_row - 1]:
            if cell_idx == 0:
                row.append(key)
            else:
                row.append(entry[store_keys[cell_idx]])
            cell_idx += 1
        worksheet.append(row)

    workbook.save(filename)


def dump_store(store):
    """
    Converts contents of a kivy JSON store to a list of dictionaries

    :param store: kivy JSON store
    :return: list of dictionaries
    """
    data = []
    for key, entry in store.find():
        data.append({key: entry})

    return data
