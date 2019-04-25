import json

from load_spreadsheet import get_actions, get_spreadsheet


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




