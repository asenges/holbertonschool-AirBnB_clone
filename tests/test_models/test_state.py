#!/usr/bin/python3
"""
Applying Unit Test for State Class
"""
import unittest
import models
from models.state import State


class Test_State_init(unittest.TestCase):
    """ Testing instantiation """

    def test_init(self):
        self.assertIs(State, type(State()))


class Test_State_Save(unittest.TestCase):
    """ Unittest for testing save"""

    def test_save(self):
        state = State()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_update(self):
        state = State()
        state.save()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_json(self):
        state = State()
        state.save()
        self.assertIs(type(state.to_dict()), dict)


if __name__ == "__main__":
    unittest.main()
