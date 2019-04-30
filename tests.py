import json

from load_spreadsheet import get_actions, get_spreadsheet
from storage import store_to_excel


def test_get_actions():
    actions = json.loads(get_actions("CQ Point System.xlsx"))

    workbook = get_spreadsheet("CQ Point System.xlsx")

    # Assures that get_spreadsheet is working because we know the file exists
    # which means workbook should not be None
    assert workbook is not None

    # Use first sheet
    worksheet = workbook[workbook.sheetnames[0]]

    headers = []
    first_row = tuple(worksheet.rows)[0]
    for cell in first_row:
        if cell.value is not None:
            headers.append(cell.value.strip())

    action_idx = 0
    for row in worksheet.iter_rows(min_row=2, max_col=len(headers)):
        action = actions[action_idx]
        action_idx += 1

        for i in range(len(headers)):
            keys = action.keys()

            for key in keys:
                if key != 'Times Completed':
                    assert key in headers

            assert action[str(headers[i])] == str(row[i].value)


def test_store_to_excel():
    # test.json was created by a test application
    # test.xlsx was created by running store_to_excel() in the test application
    store = json.load(open("test.json"))
    excel_data = get_spreadsheet("test.xlsx").active

    # How the headers look in the excel file
    ws_headers = ["Action and Category", "Repeat?", "Drive", "Knowledge", "Strategy", "Action",
                  "Maximum?", "Times Completed"]

    # How the headers were entered into the store
    store_keys = ["Action and Category", "Repeat", "Drive", "Knowledge", "Strategy", "Action",
                  "Maximum", "Completed"]

    # Check that column headers are correct
    header_idx = 0
    for cell in tuple(excel_data.rows)[0]:
        assert cell.value == ws_headers[header_idx]
        header_idx += 1

    for row_idx in range(1,excel_data.max_row):
        cell_idx = 0
        for cell in tuple(excel_data.rows)[row_idx]:
            if cell_idx == 0:
                action = cell.value
                assert cell.value in store.keys()
            else:
                assert store[action][store_keys[cell_idx]] == cell.value
            cell_idx += 1




