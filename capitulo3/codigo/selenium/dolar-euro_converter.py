from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_currency_values():
        browser = webdriver.Chrome()
        browser.get('http://www.xe.com/en/currencyconverter/convert/?Amount=1&From=USD&To=EUR')
        time.sleep(5)
        value = browser.find_element(By.CLASS_NAME,"result__BigRate-sc-1bsijpp-1")
        print(value)
        one_dollar = value.text.split(" ")[0]
        print('The dollar at this time has a value of: €{} EUROS'.format(one_dollar))
        browser.get('http://www.xe.com/en/currencyconverter/convert/?Amount=1&From=EUR&To=USD')
        time.sleep(5)
        value = browser.find_element(By.CLASS_NAME,"result__BigRate-sc-1bsijpp-1")
        one_euro = value.text.split(" ")[0]
        print('The euro at this time has a value of: ${} dollars'.format(one_euro))
        one_dollar_float = float(one_dollar)
        one_euro_float = float(one_euro)
        operate(one_dollar_float, one_euro_float)


def operate(one_dollar_float, one_euro_float):

        while True:
                command = str(input('''Select currency conversion:
				[1]Dollars to euros
				[2]Euros to dollars
				[e]exit
				-->
				'''))

                if command == '1':
                        dollar_to_euro(one_dollar_float)
                elif command == '2':
                        euro_to_dollar(one_euro_float)
                else:
                        break

def dollar_to_euro(one_dollar_float):
        dollar_amount = float(input('Dollars amount: '))
        result = one_dollar_float * dollar_amount
        print('${} Dollars are ${} Euros'.format(dollar_amount, result))

def euro_to_dollar(one_euro_float):
        euros_amount = float(input('Euros amount: '))
        result = one_euro_float * euros_amount
        print('€{} Euros are ${} Dollars'.format(euros_amount, result))


if __name__ == '__main__':
        get_currency_values()
