#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     28/03/2016
# Copyright:   (c) Admin 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from bs4 import BeautifulSoup

import lxml
import requests

def main():
    url = 'http://google.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

if __name__ == '__main__':
    main()
