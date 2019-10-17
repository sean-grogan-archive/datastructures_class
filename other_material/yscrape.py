#!/usr/bin/env python
from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import shlex
import calculate
 
global ticker, income, balance, cash, x, y, z
global data, data2, data3, incomedict, balancedict, cashdict
 
def split_list(list_name, split_size):
    return [list_name[i:i+split_size] for i in range(0,len(list_name), split_size)]
 
def contains(str, set):
    return 1 in [c in str for c in set]
 
def accept_input():
   
    global ticker
    ticker = str(raw_input('Enter a ticker symbol (\'done\' to exit): ').upper())
    if ticker == 'DONE':
        exit()
    else:
        build_vars()
        print('\n')
        print('#####################################')
        print('#     INCOME STATEMENT ANALYSIS     #')
        print('#####################################')
        calculate.rev_inc(incomedict)
        calculate.rev_rate(incomedict)
        calculate.cor_rate(incomedict)
        calculate.analyze_rev_rates(incomedict)
        calculate.inc_inc(incomedict)
        print('\n')
        print('#####################################')
        print('#      BALANCE SHEET ANALYSIS       #')
        print('#####################################')
        calculate.cash_on_hand(balancedict)
        calculate.pos_se(balancedict)
        calculate.pos_nta(balancedict)
        print('\n')
        print('#####################################')
        print('#      CASH FLOW ANALYSIS           #')
        print('#####################################')
        calculate.cce(cashdict)
        calculate.ocf_rev_ratio(cashdict, incomedict)
        calculate.fcf_analysis(cashdict, incomedict)
        new = (raw_input('\n\nWould you like to enter another ticker? (y/n): ')).upper()
        while new == "Y":
            accept_input()
        exit()  
 
def build_vars():
   
        global income, balance, cash
        print('\n\nBuilding variables\n')
        income = 'http://finance.yahoo.com/q/is?s=' + ticker + '+Income+Statement&annual'
        balance = 'http://finance.yahoo.com/q/bs?s=' + ticker + '+Balance+Sheet&annual'
        cash = 'http://finance.yahoo.com/q/cf?s=' + ticker + '+Cash+Flow&annual'
        print('             ...Done!')
        scrape_all()
 
def scrape_all():
   
    print('\nCollecting data')
##    print('\n\nScraping Income Statement (' + income + ')\n')
    scrape(income)
##    print('             ...Done!')
##    print('\n\nScraping Balance Sheet (' + balance + ')\n')
    scrape(balance)
##    print('             ...Done!')
##    print('\n\nScraping Cash Flows (' + cash + ')\n')
    scrape(cash)
    print('             ...Done!')
 
def create_income_vars():
   
    global data3, incomedict
 
    x = 0
    y = 0
    z = 0
    incomedict = {}
    incomevars = ['istryr', 'iscoryr', 'isgpyr', 'isrndyr', 'issgayr', 'isnryr',
                  'oyr', 'istoeyr', 'isoilyr', 'istoienyr', 'isebityr', 'isieyr',
                  'isibtyr', 'isiteyr', 'ismiyr', 'isnifcoyr', 'isdoyr', 'iseiyr',
                  'iseacyr', 'isoiyr', 'isniyr', 'ispsoayr', 'isniacsyr']
    while y < len(data3):
        if x <= 2:
            var = incomevars[y]
            if z < 3:
                z += 1
            else:
                z = 1
            incomedict[var + str(z)] = data3[y][x]
            x += 1
        else:
            x = 0
            y += 1
 
def create_balance_vars():
   
    global data3, balancedict
 
    x = 0
    y = 0
    z = 0
    balancedict = {}
    balancevars = ['bscceyr', 'bsstiyr', 'bsnryr', 'bsiyr', 'bsocayr', 'bstcayr',
              'bsltiyr', 'bsppeyr', 'bsgyr', 'bsiayr', 'bsaayr', 'bsoayr',
              'bsdltacyr', 'bstayr', 'bsapyr', 'bsscltdyr', 'bsoclyr', 'bstclyr',
              'bsltdyr', 'bsolyr', 'bsdltlcyr', 'bsmiyr', 'bsngyr', 'bstlyr', 'bsmsowyr',
              'bsrpsyr', 'bspsyr', 'bscsyr', 'bsreyr', 'bstsyr', 'bscs2yr', 'bsoseyr',
              'bstseyr', 'bsntayr']
 
              #Note that the variable for Capital Surplus above is 'bscs2yr' becuase 'bscsyr' is used for Common Stock
   
    while y < len(data3):
        if x <= 2:
            var = balancevars[y]
            if z < 3:
                z += 1
            else:
                z = 1
            balancedict[var + str(z)] = data3[y][x]
            x += 1
        else:
            x = 0
            y += 1
 
def create_cash_vars():
   
    global data3, cashdict
 
    x = 0
    y = 0
    z = 0
    cashdict = {}
    cashvars = ['cfniyr', 'cfdyr', 'cfaniyr', 'cfcaryr', 'cfclyr', 'cfciyr',
              'cfcooayr', 'cftcfoayr', 'cfceyr', 'cfiyr', 'cfocfiayr', 'cftcfiayr',
              'cfdpyr', 'cfspsyr', 'cfnbyr', 'cfocffayr', 'cftcffayr', 'cfeercyyr',
              'cfccceyr']
    while y < len(data3):
        if x <= 2:
            var = cashvars[y]
            if z < 3:
                z += 1
            else:
                z = 1
            cashdict[var + str(z)] = data3[y][x]
            x += 1
        else:
            x = 0
            y += 1
 
def scrape(url):
   
    global data, data2, data3
    mech = Browser()
    page = mech.open(url)
    html = page.read()
 
    soup = BeautifulSoup(html)
    table = soup.find('table', width='100%', cellspacing='0', cellpadding='2', border='0')
    data2 = []
    rowIndex = 0
    for row in table.findAll('tr')[1:]:
        data = str(row.getText(separator=' '))
        data.strip()
        data = data.replace('&nbsp;', '')
        data = data.replace('\n', '')
        data = data.replace('-', '0')
        data = data.replace(',', '')
        data = data.replace('\'', '')
        data = shlex.split(data)
        rowIndex += 1
        for i in data[:]:
            if i.isdigit():
                i = int(i)
                data2.append(i)
            elif contains(i, '()'):
                i = i.replace('(', '')
                i = i.replace(')', '')
                i = int(i)
                i = -i
                data2.append(i)
            else:
                data.remove(i)
    data3 = split_list(data2, 3)
    if url == str(income):
        create_income_vars()
    elif url == str(balance):
        create_balance_vars()
    else:
        create_cash_vars()
 
accept_input()
