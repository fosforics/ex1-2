#!/usr/bin/env python3

# Do not touch this file, it will only bring heartache. In the future we will talk about how to write
# your own test files, but for now, this gets used for grading.

import unittest

import code


class HelloWorldTest(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(code.hello("Alice"), "Hello, Alice!")
        self.assertEqual(code.hello("Bill"), "Hello, Bill!")


if __name__ == '__main__':
    unittest.main()
