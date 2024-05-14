from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage

class CheckoutPage(BasePage):
    def fill_form(self, first_name, last_name, postal_code):
        first_name_input = self.driver.find_element(By.ID, "first-name")
        last_name_input = self.driver.find_element(By.ID, "last-name")
        postal_code_input = self.driver.find_element(By.ID, "postal-code")
        continue_button = self.driver.find_element(By.ID, "continue")

        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        postal_code_input.send_keys(postal_code)
        continue_button.click()

    def get_total_amount(self):
        total_amount = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
        total_amount_text = total_amount.text

        # Удаление "Total: " из текста итоговой суммы
        total_amount_value = total_amount_text.replace("Total: ", "")
        return total_amount_value
