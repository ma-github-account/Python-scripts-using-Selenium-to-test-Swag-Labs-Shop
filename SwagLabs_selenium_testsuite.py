
from SwagLabs_navigation_management import *

def testVerificationOfTheNumberOfItemsOnDisplay():

	driver = webdriver.Firefox()
	logInToSwagLabs(driver)
	time.sleep(3)
	assert countTheItemsOnDisplay(driver) == 6
	driver.close()


def testVerificationThatBurgerButtonIsPresent():

	driver = webdriver.Firefox()
	logInToSwagLabs(driver)
	time.sleep(3)
	assert countTheBurgerButtonsIcons(driver) == 1
	driver.close()


def testVerificationThatShoppingCardIconIsPresent():

	driver = webdriver.Firefox()
	logInToSwagLabs(driver)
	time.sleep(3)
	assert countTheShoppingCardsIcons(driver) == 1
	driver.close()


def testVerificationThatSortContainerIconIsPresent():

	driver = webdriver.Firefox()
	logInToSwagLabs(driver)
	time.sleep(3)
	assert countTheSortContainerIcons(driver) == 1
	driver.close()


def testVerificationOfAddingAnItemToCardFromInventorySite():

	driver = webdriver.Firefox()
	logInToSwagLabs(driver)
	time.sleep(3)
	clickToAddBackpackToCardSummary(driver)
	goToCardSummarySite(driver)
	assert countTheInventoryItems(driver) == 1
	driver.close()


def testVerificationOfAddingAnItemToCardFromProductDescriptionSite():

	driver = webdriver.Firefox()
	logInToSwagLabs(driver)
	time.sleep(3)
	clickOnFirstProductToGoToProductDescriptionSite(driver)
	clickToAddBackpackToCardSummary(driver)
	goToCardSummarySite(driver)
	assert countTheInventoryItems(driver) == 1
	driver.close()


def testVerificationOfRemovingAnItemFromCardFromSummarySite():

	driver = webdriver.Firefox()
	logInToSwagLabs(driver)
	time.sleep(3)
	clickToAddBackpackToCardSummary(driver)
	goToCardSummarySite(driver)
	clickToRemoveBackpackFromCardSummary(driver)
	assert countTheInventoryItems(driver) == 0
	driver.close()


def testVerificationOfRemovingAnItemFromCardFromProductDescriptionSite():

	driver = webdriver.Firefox()
	logInToSwagLabs(driver)
	time.sleep(3)
	clickOnFirstProductToGoToProductDescriptionSite(driver)
	clickToAddBackpackToCardSummary(driver)
	clickToRemoveBackpackFromCardSummary(driver)
	goToCardSummarySite(driver)
	assert countTheInventoryItems(driver) == 0
	driver.close()
















