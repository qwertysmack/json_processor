# json_processor
Processes JSON format strings and adds to a priority queue.

"Write a python module that can receive a JSON string and if the action is “apply”, 
it adds the contents of the “template” into a priority queue.
The module also processes the queue every second and saves the template to a file."

Example JSON string:

{“action”: “apply”, “when”: “2016-4-19 10:00:00”, “template”: …}
