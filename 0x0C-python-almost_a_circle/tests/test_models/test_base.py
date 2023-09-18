import unittest
import models.base

class TeastBase(unittest.TestCase):
    """
    testing the module models.base
    """
    def setUp(self):
        """
        setting the stage
        """
        samp1 = base()
        samp2 = base()
        samp3 = base(20)

    def test_to_json_string(list_dictionaries):
        pass

    def test_from_json_string(json_string):
        pass

    def test_save_to_file(cls, list_objs):
        pass

    def test_load_from_file(cls):
        pass

    def test_create(cls, **dictionary):
        pass
