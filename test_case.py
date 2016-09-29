import unittest

import json_processor


class TestJSONFunctions(unittest.TestCase):

    example_json_string = """
    {"action": "apply",
     "when": "2016-4-19 10:00:00",
     "template": "(template information)"}
     """

    expected_output = {"action": "apply",
                       "when": "2016-4-19 10:00:00",
                       "template": "(template information)"
                       }

    test_dict_no_apply = {"action": "something else",
                          "when": "2016-4-19 10:00:00",
                          "template": "(template information)"
                          }

    def test_is_json_true(self):
        """ should return True with known json string"""
        result = json_processor.is_json(self.example_json_string)
        self.assertTrue(result)

    def test_is_json_false(self):
        """ should return False with known non-json string (python dict)"""
        result = json_processor.is_json(self.expected_output)
        self.assertFalse(result)

    def test_json_converter(self):
        """ convert_json_to_dict should give known result with known input """
        result = json_processor.convert_json_to_dict(self.example_json_string)
        self.assertEqual(self.expected_output, result)

    def test_process_json_dict(self):
        """ process_json_dict should return template information if action
        is 'apply'"""
        result = json_processor.process_json_dict(self.expected_output)
        self.assertEqual(self.expected_output["template"], result)

    def test_process_json_dict_no_apply(self):
        """ process_json_dict should return None if action is not 'apply'"""
        result = json_processor.process_json_dict(self.test_dict_no_apply)
        self.assertEqual(None, result)

# TODO: create test(s) for PriorityQueue class
# harder to unit test... would come back to this

if __name__ == '__main__':
    unittest.main()
