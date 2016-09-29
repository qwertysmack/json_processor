#! Python35
import json
from threading import Thread, Lock, Timer
import json_string_examples as jse

"""
JSON processor receives json strings. if "action" = "apply",
adds contents of "template" to priority queue.
Processes queue each second, writing templates to file.
"""

# container for template data ready for writing to file
priority_queue = ["ham", "eggs", "spam"]


def get_json():
    """
    generator simulates receiving some data
    :return: yields a string
    """
    for string in jse.json_strings:
        yield string


def is_json(json_string):
    """
    check json_string is string and valid JSON
    :param json_string: input string
    :return: True/False
    """
    if isinstance(json_string, str):
        try:
            json.loads(json_string)
        except ValueError:
            return False
        return True
    else:
        return False


def convert_json_to_dict(json_string):
    """
    converts json string to python dictionary
    :param json_string: json string
    :return: json_dict
    """
    json_dict = json.loads(json_string)
    return json_dict


def process_json_dict(json_dict):
    """
    checks 'action' key for 'apply'. If found, returns 'template' value
    :param json_dict: dictionary
    :return: template value if action = apply, else None
    """
    if json_dict["action"].lower() == "apply":
        return json_dict["template"]
    else:
        return None


class PriorityQueue(Thread):
    """
    PriorityQueue inherits from Thread to run concurrently to json functions
    Writes oldest available template data to file
    """
    def __init__(self):
        super().__init__()
        self.lock = Lock()

    def run(self):
        """
        Overrides run method of Thread, called with .start()
        Uses Lock to stop main thread whilst processing data
        Prioritises first (oldest) item in list
        """
        with self.lock:
            while priority_queue:
                self.write_data_to_file(priority_queue[0])
                # remove item from queue after processing
                priority_queue.remove(priority_queue[0])
        Timer(1, self.run).start()  # calls self every second

    def write_data_to_file(self, data):
        """
        Write (append) template data to template.txt
        Creates file name using a file counter
        """
        filename = "template_data.txt"
        with open(filename, 'a') as outfile:
            outfile.writelines(data + '\n')


def main():
    # start priority queue thread
    queue_thread = PriorityQueue()
    queue_thread.start()

    # main thread
    for j_string in get_json():
        if is_json(j_string):
            json_dict = convert_json_to_dict(j_string)
            data = process_json_dict(json_dict)
            if data is not None:
                priority_queue.append(data)  # append data to list
        else:
            # handle non-json string
            print("{} is not json format".format(j_string))

if __name__ == "__main__":
    main()
