import json


def update_storage(actions, store):
    """
    Updates the JSON store with any action within actions that is not already in the store

    :param actions: JSON string containing actions that may be added
    :param store: Kivy JSON store
    :return: does not return, updates JSON storage file
    """

    # JSON keys (for reference)
    # Action and Category, Repeat?, Drive, Knowledge, Strategy, Action, Maximum?, Times Completed
    actions = json.loads(actions)
    for action in actions:
        try:
            store.put(action['Action and Category'], Repeat=action['Repeat?'], Drive=action['Drive'],
                      Knowledge=action['Knowledge'], Strategy=action['Strategy'], Action=action['Action'],
                      Maximum=action['Maximum?'], Completed=action['Times Completed'])
        except Exception as e:
            print("Unable to add action to store: {}".format(e))



