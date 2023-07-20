from webdriver_operations import WebdriverOperations
from scrape import Scrape
from config import management_portal, username, password, resident_map


class TicketHelper:
    def __init__(self):
        self.webdriver = WebdriverOperations()
        self.scrape = Scrape()
        self.start_program()

    def start_program(self):
        self.webdriver.driver.get(management_portal)
        self.webdriver.driver.maximize_window()
        self.webdriver.login(username, password)

    def open_ticket(self):
        self.webdriver.switch_to_primary_tab()
        property, unit, resident = self.scrape.scrape_ticket()
        print(property, unit, resident)
        self.webdriver.new_tab()
        self.webdriver.driver.get(resident_map)
        self.webdriver.login(username, password)
        self.webdriver.open_property(property)
        if unit is not None:
            self.webdriver.open_unit(unit)
            if resident is None or self.scrape.compare_resident(resident):
                self.webdriver.open_ledger()
            else:
                self.webdriver.search_former(resident)
                self.webdriver.open_ledger()
