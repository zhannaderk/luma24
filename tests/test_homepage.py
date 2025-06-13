import pytest
from pages.home_page import HomePage

@pytest.fixture
def homepage(driver):
    homepage = HomePage(driver)
    return homepage

def test_homepage_loads(homepage):
    homepage.open()
    assert "Home Page" in homepage.title or "Magento" in homepage.title

def test_homepage_logo(homepage):
    homepage.open()
    logo = homepage.get_logo()
    assert logo.is_displayed(), "Logo is not displayed"

def test_catalog_items_are_loaded(homepage):
    homepage.open()
    homepage.wait_for_products()
    products = homepage.get_products()
    assert len(products) > 0, "Products are not loaded"

def test_banner_is_loaded(homepage):
    homepage.open()
    homepage.wait_for_banner()
    banner = homepage.get_banner()
    assert banner.is_displayed(), "Banner is not loaded"