from module.parser import Scraper
from module.excel import saveToExcel

DICT = {}

if __name__ == "__main__":

    T = Scraper()
    
    for i in range(1, 9999):

        # Testing Webpage
        T.goTo(f"https://webscraper.io/test-sites/e-commerce/allinone/product/{i}")
        T.waitXPATH('/html//div[2]')

        # End
        if (T.compareStringByXPATH('/html//div[2]', 'NOT FOUND')):
            break;
    
        # Name
        T.waitXPATH('//div[1]/div[3]/div/div[2]//div[2]/div[1]/h4[2]')
        NAME = T.getElementByXPATH('//div[1]/div[3]/div/div[2]//div[2]/div[1]/h4[2]').text.strip()

        # Price
        T.waitXPATH('//div[1]/div[3]/div/div[2]//div[2]/div[1]/h4[1]')
        PRICE = T.getElementByXPATH('//div[1]/div[3]/div/div[2]//div[2]/div[1]/h4[1]').text.strip()

        # Colors
        COLORLIST = []
        if (T.doesElementExistByXPATH('//div[1]/div[3]/div/div[2]//div[2]/div[2]/select')):
            OPTIONS = T.getDropdownItemsByXPATH('//div[1]/div[3]/div/div[2]//div[2]/div[2]/select')
            for option in OPTIONS:
                text = option.text.strip()
                if text != 'Select color':
                    COLORLIST.append(text)
    
        # Append
        DICT[NAME] = [PRICE, COLORLIST]
     
    # Save
    saveToExcel(DICT, 'output.xlsx')
