
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


user = "standard_user"
password = "secret_sauce"


def logInToSwagLabs(driver):

	user = "standard_user"
	password = "secret_sauce"


	driver.get("https://www.saucedemo.com/")

	user_field = driver.find_element_by_id("user-name")
	user_field.clear()
	user_field.send_keys(user)

	password_field = driver.find_element_by_id('password')
	password_field.clear()
	password_field.send_keys(password)

	driver.find_element_by_id("login-button").click()


def countTheItemsOnDisplay(driver):

	items_on_display_count = len(driver.find_elements_by_class_name('inventory_item_name'))
	return items_on_display_count


def countTheBurgerButtonsIcons(driver):

	burger_button_icon_count = len(driver.find_elements_by_id('react-burger-menu-btn'))
	return burger_button_icon_count


def countTheShoppingCardsIcons(driver):

	shopping_cart_icon_count = len(driver.find_elements_by_id('shopping_cart_container'))
	return shopping_cart_icon_count


def countTheSortContainerIcons(driver):

	sort_container_icons_count = len(driver.find_elements_by_class_name('product_sort_container'))
	return sort_container_icons_count


def countTheInventoryItems(driver):

	inventory_items_count = len(driver.find_elements_by_class_name('inventory_item_name'))
	return inventory_items_count


def goToCardSummarySite(driver):

	driver.get("https://www.saucedemo.com/cart.html")


def goToInventorySite(driver):

	driver.get("https://www.saucedemo.com/inventory.html")


def clickToAddBackpackToCardSummary(driver):

	driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()


def clickToRemoveBackpackFromCardSummary(driver):

	driver.find_element_by_id("remove-sauce-labs-backpack").click()


def clickOnFirstProductToGoToProductDescriptionSite(driver):

	driver.find_elements_by_class_name('inventory_item_name')[0].click()








