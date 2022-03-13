print("hello world!")


import pytest
import allure


class TestCase1:

    @allure.story("demo1")
    def test_1_demo1(self):
        print("demo1")

    @allure.story("demo2")
    def test_1_demo2(self):
        print("demo2")