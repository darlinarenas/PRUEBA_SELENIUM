import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones import Funciones_Globales
from Page_Login import Funciones_Login
from selenium.webdriver import ActionChains
t=.8


@pytest.mark.validarif
def test_validar_if():
    a=20
    b=20
    if (a==b):
        print("LoS datos son iguales")
        assert True
    else:
        print("los datos no son iguales")
        assert False


