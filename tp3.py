from cmu_graphics import *
#https://pypi.org/project/yfinance/
import yfinance as yf
from PIL import Image
#https://pandas.pydata.org/docs/
import pandas as pd
import os, pathlib
from datetime import datetime
#https://docs.python.org/3/library/webbrowser.html
import webbrowser


def onAppStart(app):
    #changing screen variables 
    app.mainScreen = True
    app.predictionButton = False
    app.analysisButton = False
    app.infoScreen = False
    app.stockInfo = False
    app.predictionInfo = False

    #switching between time frame variables
    app.oneMonth = True
    app.oneYear = False
    app.threeYears = False
    
    #input time frame variables
    app.text = ""
    app.input = '1mo'
    app.selectedTime = False
    app.selectedTimeColor = 'silver'

    #online images inside the application 
    #https://www.fool.com/investing/2022/12/14/bull-market-is-coming-smartest-investors-prepare/
    app.bgimage = openImage("images/bullbear1.webp")
    app.bgimageWidth,app.bgimageHeight = app.bgimage.width,app.bgimage.height
    app.bgimage = CMUImage(app.bgimage)
    #https://www.vectorstock.com/royalty-free-vector/candlestick-chart-data-report-or-stock-market-vector-22977998
    app.candleimage = openImage("images/candle.png")
    app.candleimageWidth = app.candleimage.width
    app.candleimageHeight = app.candleimage.height
    app.candleimage = CMUImage(app.candleimage)
    #https://www.gooddata.com/blog/how-ensure-success-when-it-comes-predictive-analytics/
    app.predimage = openImage("images/predict.png")
    app.predimageWidth = app.predimage.width
    app.predimageHeight = app.predimage.height
    app.predimage = CMUImage(app.predimage)
    #https://www.freepnglogos.com/pics/amazon-png-logo-vector
    app.amznimage = openImage("images/amznlogo1.png")
    app.amznimageWidth = app.amznimage.width
    app.amznimageHeight = app.amznimage.height
    app.amznimage = CMUImage(app.amznimage)
    #https://www.iconfinder.com/icons/7123025/logo_google_g_icon
    app.googimage = openImage("images/googlogo.webp")
    app.googimageWidth = app.googimage.width
    app.googimageHeight = app.googimage.height
    app.googimage = CMUImage(app.googimage)
    #https://en.wikipedia.org/wiki/File:Tesla_logo.png
    app.tslaimage = openImage("images/tslalogo.png")
    app.tslaimageWidth = app.tslaimage.width
    app.tslaimageHeight = app.tslaimage.height
    app.tslaimage = CMUImage(app.tslaimage)
    #https://commons.wikimedia.org/wiki/File:MSFT_logo_png_grey.png
    app.msftimage = openImage("images/msftlogo.png")
    app.msftimageWidth = app.msftimage.width
    app.msftimageHeight = app.msftimage.height
    app.msftimage = CMUImage(app.msftimage)
    #https://freebiesupply.com/logos/johnson-johnson-logo/
    app.jnjimage = openImage("images/jnjlogo.png")
    app.jnjimageWidth = app.jnjimage.width
    app.jnjimageHeight = app.jnjimage.height
    app.jnjimage = CMUImage(app.jnjimage)
    #https://www.tiicker.com/brand/BRK.A
    app.brkimage = openImage("images/brklogo.png")
    app.brkimageWidth = app.brkimage.width
    app.brkimageHeight = app.brkimage.height
    app.brkimage = CMUImage(app.brkimage)
    #https://www.stickpng.com/img/icons-logos-emojis/social-media-icons/meta-logo
    app.metaimage = openImage("images/metalogo.png")
    app.metaimageWidth = app.metaimage.width
    app.metaimageHeight = app.metaimage.height
    app.metaimage = CMUImage(app.metaimage)
    #https://www.pngegg.com/en/png-snqfy
    app.aaplimage = openImage("images/aapllogo.png")
    app.aaplimageWidth = app.aaplimage.width
    app.aaplimageHeight = app.aaplimage.height
    app.aaplimage = CMUImage(app.aaplimage)
    #https://sco.wikipedia.org/wiki/File:Nvidia_logo.svg
    app.nvdaimage = openImage("images/nvdalogo.png")
    app.nvdaimageWidth = app.nvdaimage.width
    app.nvdaimageHeight = app.nvdaimage.height
    app.nvdaimage = CMUImage(app.nvdaimage)
    #https://1000logos.net/visa-logo/
    app.vimage = openImage("images/vlogo.png")
    app.vimageWidth = app.vimage.width
    app.vimageHeight = app.vimage.height
    app.vimage = CMUImage(app.vimage)
    #https://www.pngwing.com/en/free-png-yinxn
    app.unhimage = openImage("images/unhlogo.png")
    app.unhimageWidth = app.unhimage.width
    app.unhimageHeight = app.unhimage.height
    app.unhimage = CMUImage(app.unhimage)

    #list of all the image logos
    app.imageList= [app.msftimage, app.aaplimage, app.amznimage, app.nvdaimage, app.googimage, 
                    app.tslaimage, app.metaimage,app.vimage, app.jnjimage, app.unhimage, app.brkimage]

    #Buttons for the different the different sections and screens
    app.butAnalColor = 'silver'
    app.butPredColor = 'silver'
    app.mainAnalWidth1 = 155
    app.mainAnalWidth2 = 305
    app.mainAnalHeight1 = 470
    app.mainAnalHeight2 = 545
    app.mainPredWidth1 = 490
    app.mainPredWidth2 = 640
    app.mainPredHeight1 = 470
    app.mainPredHeight2 = 545
    app.backButtWidth1 = 10
    app.backButtWidth2 = 60
    app.backButtHeight1 = 10
    app.backButtHeight2 = 35
    app.infoButtWidth1 = 760
    app.infoButtWidth2 = 790
    app.infoButtHeight1 = 10
    app.infoButtHeight2 = 40

    #the downloaded stock data for my stocks, 1y
    app.msft = yf.download('MSFT', period='1y', interval = '5d')
    app.aapl = yf.download('aapl', period='1y', interval = '5d')
    app.amzn = yf.download('amzn', period='1y', interval = '5d')
    app.nvda = yf.download('nvda', period='1y', interval = '5d')
    app.goog = yf.download('goog', period='1y', interval = '5d')
    app.tsla = yf.download('tsla', period = '1y', interval = '5d')
    app.meta = yf.download('tsla', period = '1y', interval = '5d')
    app.v = yf.download('v', period = '1y', interval = '5d')
    app.jnj = yf.download('jnj', period = '1y', interval = '5d')
    app.unh = yf.download('unh', period = '1y', interval = '5d')
    app.brk = yf.download('brk-a', period = '1y', interval = '5d')

    #downloaded 1 week stocks 
    app.msft3 = yf.download('MSFT', period='7d')
    app.aapl3 = yf.download('aapl', period='7d')
    app.amzn3 = yf.download('amzn', period='7d')
    app.nvda3 = yf.download('nvda', period='7d')
    app.goog3 = yf.download('goog', period='7d')
    app.tsla3 = yf.download('tsla', period = '7d')
    app.meta3 = yf.download('tsla', period = '7d')
    app.v3 = yf.download('v', period = '7d')
    app.jnj3 = yf.download('jnj', period = '7d')
    app.unh3 = yf.download('unh', period = '7d')
    app.brk3 = yf.download('brk-a', period = '7d')

    #downloaded 1 month stocks
    app.msftMon = yf.download('MSFT', period='1mo')
    app.aaplMon = yf.download('aapl', period='1mo')
    app.amznMon = yf.download('amzn', period='1mo')
    app.nvdaMon = yf.download('nvda', period='1mo')
    app.googMon = yf.download('goog', period='1mo')
    app.tslaMon = yf.download('tsla', period = '1mo')
    app.metaMon = yf.download('tsla', period = '1mo')
    app.vMon= yf.download('v', period = '1mo')
    app.jnjMon = yf.download('jnj', period = '1mo')
    app.unhMon = yf.download('unh', period = '1mo')
    app.brkMon = yf.download('brk-a', period = '1mo')

    #downloaded 1 year stocks without an interval for predictions 
    app.msft1 = yf.download('MSFT', period='1y')
    app.aapl1 = yf.download('aapl', period='1y')
    app.amzn1 = yf.download('amzn', period='1y')
    app.nvda1 = yf.download('nvda', period='1y')
    app.goog1 = yf.download('goog', period='1y')
    app.tsla1 = yf.download('tsla', period = '1y')
    app.meta1 = yf.download('tsla', period = '1y')
    app.v1 = yf.download('v', period = '1y')
    app.jnj1 = yf.download('jnj', period = '1y')
    app.unh1 = yf.download('unh', period = '1y')
    app.brk1 = yf.download('brk-a', period = '1y')

    #need to set max shape for my 1y graphs
    app.setMaxShapeCount(4000)

    #list of all the stock downloads
    app.dataList = [app.msft, app.aapl, app.amzn, app.nvda, app.goog, app.tsla
                    , app.meta, app.v, app.jnj, app.unh, app.brk]
    
    app.dataListMon = [app.msftMon, app.aaplMon, app.amznMon, app.nvdaMon, app.googMon, app.tslaMon
                    , app.metaMon, app.vMon, app.jnjMon, app.unhMon, app.brkMon]

    app.dataList3 = [app.msft3, app.aapl3, app.amzn3, app.nvda3, app.goog3, app.tsla3
                    , app.meta3, app.v3, app.jnj3, app.unh3, app.brk3]
    app.dataList1 = [app.msft1, app.aapl1, app.amzn1, app.nvda1, app.goog1, app.tsla1
                    , app.meta1, app.v1, app.jnj1, app.unh1, app.brk1]
    
    #list of all the stock names
    app.allStocks = ['MSFT','AAPL','AMZN', 'NVDA', 'GOOG',
                     'TSLA', 'META','V','JNJ','UNH',
                     'BRK-A']
    app.stockBoxColor = None
    app.msftTicker= yf.Ticker('MSFT')
    app.aaplTicker= yf.Ticker('AAPL')
    app.amznTicker= yf.Ticker('AMZN')
    app.nvdaTicker= yf.Ticker('NVDA')
    app.googTicker= yf.Ticker('GOOG')
    app.tslaTicker= yf.Ticker('TSLA')
    app.metaTicker= yf.Ticker('META')
    app.vTicker= yf.Ticker('V')
    app.jnjTicker= yf.Ticker('JNJ')
    app.unhTicker= yf.Ticker('UNH')
    app.brkTicker= yf.Ticker('BRK-A')

    #download the stock information section 
    app.msftInfo = app.msftTicker.info
    app.aaplInfo = app.aaplTicker.info
    app.amznInfo = app.amznTicker.info
    app.nvdaInfo = app.nvdaTicker.info
    app.googInfo = app.googTicker.info
    app.tslaInfo = app.tslaTicker.info
    app.metaInfo = app.metaTicker.info
    app.vInfo = app.vTicker.info
    app.jnjInfo = app.jnjTicker.info
    app.unhInfo = app.unhTicker.info
    app.brkInfo = app.brkTicker.info

    #list of the stock information 
    app.stockInfoList = [app.msftInfo, app.aaplInfo, app.amznInfo, app.nvdaInfo
                         , app.googInfo, app.tslaInfo, app.metaInfo, app.vInfo,
                         app.jnjInfo, app.unhInfo, app.brkInfo]
    
    app.nameList = ['Microsoft','Apple', 'Amazon', 'Nvida', 'Google', 'Tesla', 
                     'Meta', 'Visa', 'Johnson and Johnson', 'United Health Group', 'Berkshire Hathaway']

    #news section for the stock information
    app.msftNews = app.msftTicker.news
    app.aaplNews = app.aaplTicker.news
    app.amznNews = app.amznTicker.news
    app.nvdaNews = app.nvdaTicker.news
    app.googNews = app.googTicker.news
    app.tslaNews = app.tslaTicker.news
    app.metaNews = app.metaTicker.news
    app.vNews = app.vTicker.news
    app.jnjNews = app.jnjTicker.news
    app.unhNews = app.unhTicker.news
    app.brkNews = app.brkTicker.news

    #class stock calls
    app.msftBox = stockBox('MSFT',40, 120, 55, 95, None, app.msftInfo, app.msftNews)
    app.aaplBox = stockBox('AAPL',40, 120, 105, 145, None, app.aaplInfo, app.aaplNews)
    app.amznBox = stockBox('AMZN',40, 120, 155, 195, None, app.amznInfo, app.amznNews)
    app.nvdaBox = stockBox('NVDA',40, 120, 205, 245, None,app.nvdaInfo, app.nvdaNews)
    app.googBox = stockBox('GOOG',40, 120, 255, 295, None,app.googInfo, app.googNews)
    app.tslaBox = stockBox('TSLA',40, 120, 305, 345, None,app.tslaInfo, app.tslaNews)
    app.metaBox = stockBox('META',40, 120, 355, 395, None, app.metaInfo, app.metaNews)
    app.vBox = stockBox('V',40, 120, 405, 445, None, app.vInfo, app.vNews)
    app.jnjBox = stockBox('JNJ',40, 120, 455, 495, None, app.jnjInfo, app.jnjNews)
    app.unhBox = stockBox('UNH',40, 120, 505, 545, None,app.unhInfo, app.unhNews )
    app.brkBox = stockBox('BRK-A',40, 120, 555, 595, None, app.brkInfo, app.brkNews)
    app.stockList = [app.msftBox, app.aaplBox, app.amznBox, app.nvdaBox,
                     app.googBox, app.tslaBox, app.metaBox, app.vBox, app.jnjBox
                     , app.unhBox, app.brkBox]

    #list for phone numbers and websites (needed because not all stocks have
    #their phone and website in their stock information)
    app.phoneList = ['425 882 8080', '408 996 1010', '206 266 1000','408 486 2000',
                     '650 253 0000', '512 516 8177', '650 543 4800', '650 432 3200',
                     '732 524 0400','952 936 1300','402 346 1400']
    
    app.websiteList = ['https://www.microsoft.com', 'https://www.apple.com', 'https://www.amazon.com',
                       'https://www.nvidia.com', 'https://www.google.com', 'https://www.tesla.com', 
                       'https://investor.fb.com', 'https://usa.visa.com', 'https://www.jnj.com',
                       'https://www.unitedhealthgroup.com', 'https://www.berkshirehathaway.com']

    #graph apps
    app.graphWidth = 400
    app.graphHeight = 267
    app.margin = 50
    app.graphX = 300
    app.graphY = 145
    app.zoomLevel = 1.0
    app.graphData = None

    #zoom apps
    app.zoomLevel = 1.0
    app.mousePercentageX = 0
    app.mousePercentageY = 0

    #graphing mouse hover feature 
    app.hover = True
    app.hoveredVolume = None
    app.hoveredHigh = None
    app.hoveredLow = None
    app.hoveredOpen = None
    app.hoveredPrice = None
    app.hoveredDate = None

    #prediction apps
    app.sma = None
    app.buy = 'BUY'
    app.sell = 'SELL'
    app.rsi = None
    app.macd = None


#class for stocks in the stock analytics section, checkable boxes in the left side
class stockBox():
    def __init__(self,name, boxX, boxX2, boxY, boxY2, color, info, news):
        self.boxX = boxX
        self.boxY = boxY
        self.boxX2 = boxX2
        self.color = color
        self.boxY2 = boxY2
        self.click = False
        self.name = name
        self.info = info
        self.infoClick = False
        self.oneMonth = False
        self.oneYear = False
        self.threeYears = False
        self.input = False
        self.small = 'white'
        self.comp = False
        self.ever = None
        self.news = news

    #drawing the name of the stocks
    def drawName(self, canvas):
        drawLabel(f'{self.name}', 80, self.boxY2 - 20, size = 20, fill = 'black',
                          bold = True)
    #drawing the boxes to click on for the stocks 
    def drawBox(self, canvas, app):
        drawRect(self.boxX, self.boxY, 80, 40, fill = self.color
                         , border = 'black')
        if app.analysisButton == True:
            drawRect(self.boxX - 20, self.boxY + 20, 10, 10, fill = self.small, border = 'black')

        if self.color == 'green':
            drawLabel(f'{self.name}', 400, 50, size = 50, bold = True)

    #onMousePress to select between stocks to see graphs and information 
    def onMousePress1(self, mouseX, mouseY, app):
        self.X = mouseX
        self.Y = mouseY
        if (self.boxX < self.X and self.boxX2 > self.X and self.boxY < self.Y 
            and self.boxY2 > self.Y):
            self.click = True
            self.color= 'green'
            self.input = False
            self.comp = False
            self.small = 'white'
        #time frame selections including input
        elif (150 < mouseX and 230 > mouseX and 155 < mouseY and 235 > mouseY):
                self.oneMonth = True
                self.oneYear = False
                self.threeYears = False
                self.input = False
        elif (150 < mouseX and 230 > mouseX and 255 < mouseY and 335 > mouseY):
            self.oneYear = True
            self.oneMonth = False
            self.threeYears = False
            self.input = False
        elif (150 < mouseX and 230 > mouseX and 355 < mouseY and 435 > mouseY):
            self.threeYears = True
            self.oneYear = False
            self.oneMonth = False
            self.input = False
        elif (150 < mouseX and 230 > mouseX and 55 < mouseY and 135 > mouseY):
            self.input = True
            self.oneYear = False
            self.oneMonth = False
            self.threeYears = False
        #color of the comparasion boxes
        elif (self.boxX-20 < self.X and self.boxX2-90 > self.X and self.boxY+20 < self.Y 
            and self.boxY2-10 > self.Y):
            if self.small == 'green':
                self.small = 'white'
            else:
                self.small = 'green'
            self.comp = True
        #comparasion for the graphs
        elif (20 < mouseX and 30 > mouseX):
            self.ever = True
        elif app.predictionButton == True and 200 < mouseX and 300 > mouseX and 255 <mouseY and 355 > mouseY:
            self.ever = True
        elif app.predictionButton == True and 350 < mouseX and 450 > mouseX and 405 < mouseY and 505 > mouseY:
            self.ever = True
        elif app.predictionButton == True and 500 < mouseX and 600 > mouseX and 255 <mouseY and 355 > mouseY:
            self.ever = True
        else:
            self.click = False

################################################################################

#function to implement photos into my project
def openImage(fileName): #basicPILMethods from Piazza post @1408 Lecture image/opp demos
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

#function that draws the main start up page 
def drawMainScreen(app):
    if app.mainScreen == True:
        newWidth, newHeight = (800,700) 
        drawImage(app.bgimage,0,-100, width = newWidth, height = newHeight ) #background image
        drawLabel('Market', 230, 50, size = 100, font ='caveat', fill = 'green',
              bold = True) #title of the application 
        drawLabel('Master', 565, 50, size = 100, bold = True, fill = 'red',
              font ='cinzel') #main label
        drawRect(155, 470, 150, 75, fill = app.butAnalColor, border = 'black', 
             borderWidth = 2) #buttons of the main page
        drawRect(490, 470, 150, 75, fill = app.butPredColor, border = 'black', 
             borderWidth = 2)
        drawLabel('Stock Analysis', 230, 507.5, size = 17, fill = 'red', 
              font = 'Courier', bold = True) #stock analysis section text
        drawLabel('Stock Prediction', 565, 507, size = 17, fill = 'red', 
              font = 'orbitron', bold = True) #stock prediction section text 
        drawLabel('Click or Press i for Info', 397, 507, size = 13, fill = 'purple', bold = True) #info 
        drawCircle(775, 25, 15, fill = 'deepSkyBlue')
        #information page
        drawLabel('i', 775, 25, size = 25, fill ='white', bold = True)

#function that draws the analysis section of the tp 
def drawAnalysisScreen(app):
    infoBoxX = 140
    infoBoxY = 530
    if app.analysisButton == True:
        #overall screen
        drawRect(0,0, 800, 600, fill = 'oldLace')
        drawRect(10, 10, 50, 25, fill = 'silver')
        #back button 
        drawLabel('Return',35, 23, size = 10, fill= 'black', bold = True)
        drawLabel('Address :', infoBoxX + 100, 545, size = 15, bold = True)
        drawLabel('Phone Number :', infoBoxX + 315, 545, size = 15,bold = True)
        drawLabel('Website :', infoBoxX + 530, 545, size = 15, bold = True)
        drawLabel('Click this box to get to website', infoBoxX + 530, 575, size = 12)
        drawRect(250, 155, 500, 350, fill = 'white')
        drawCircle(280, 50, 30, fill = 'deepSkyBlue')
        #information buttons
        drawLabel('i', 280, 50, size = 40, fill ='white', bold = True)
        drawLabel('Click or Press i for Stock Info', 575, 130, size = 15, fill = 'blue', bold = True)

        #time frame buttons 
        drawRect(150, 55, 80, 80, fill = app.selectedTimeColor)
        drawRect(150, 155, 80, 80, fill = 'silver')
        drawRect(150, 255, 80, 80, fill = 'silver')
        drawRect(150, 355, 80, 80, fill = 'silver')
        drawLabel('1 Year', 190, 295, bold = True)
        drawLabel('1 Month', 190, 195, bold = True)
        drawLabel('1 Week', 190, 395, bold= True)
        drawLabel(app.text, 190, 95, bold = True)
        drawLabel('Input Own', 190, 115, bold = True)
        drawLabel('Time Frame', 190, 125, bold = True)

        #input label frame  
        if app.selectedTimeColor == 'green':
            drawLabel('Input Format #d or #mo or #y', 190, 35, size = 10)
            
        #creating the information section and boxes
        for j in range(3):
            drawRect(infoBoxX, infoBoxY, 200, 60, fill = None, border = 'black')
            infoBoxX += 215

        #full names for each stock
        count = -1
        for j in app.stockList:
            count += 1
            address = ''
            if j.click == True and j.color == 'green':
                for names in app.nameList:
                    #full name loop
                    drawLabel(f'{app.nameList[count]}', 400, 100, bold = True, fill = 'green', size = 30)

                    #information for each stock
                    address = j.info["address1"] + ','
                    drawLabel(f'{address}', 240, 560, size = 13)
                    city = j.info['city']
                    drawLabel(f'{city}', 240, 575, size = 13)
                    
                    phone = app.phoneList[count]
                    drawLabel(f'{phone}', 445, 560, size = 13)

                    website = app.websiteList[count]
                    drawLabel(f'{website}', 670, 560, size = 13)
        #text to switch graph hover features 
        for i in app.stockList:
            if i.small == 'green':
                drawLabel('S = Switch Graph Hover', 575, 80, size = 10, bold = True, fill = 'blue')

#draws the stock information screen for the stock analysis section 
def drawStockInfo(app):
    if app.stockInfo == True:
        #overall screen
        drawRect(0,0, 800, 600, fill = 'oldLace')
        drawRect(10, 10, 50, 25, fill = 'silver')
        #back button 
        drawLabel('Return',35, 23, size = 10, fill= 'black', bold = True)
        drawLabel('News', 575, 155, bold = True, size = 30, fill ='purple')
        drawLabel('Key Data', 240, 150, bold = True, size = 30, fill = 'purple')

        count = -1
        for j in app.stockList:
            count += 1
            newWidth, newHeight = (125,125) 
            if j.click == True and j.color == 'green':
                #draw the names along with the company logo
                for names in app.nameList:
                    drawLabel(f'{app.nameList[count]}', 400, 100, bold = True, fill = 'green', size = 30)
                    drawImage(app.imageList[count], 600, 20, width = newWidth, height = newHeight)

                    #draws the key data 
                    weekLow = j.info['fiftyTwoWeekLow']
                    weekHigh = j.info['fiftyTwoWeekHigh']
                    sharesO = j.info ['sharesOutstanding']
                    mrq = j.info['mostRecentQuarter']
                    floatShares = j.info['floatShares']
                    teps = j.info['trailingEps']
                    feps = j.info['forwardEps']
                    payout = j.info['payoutRatio']
                    prevClose = j.info['previousClose']
                    open = j.info['open']
                    low = j.info['dayLow']
                    high = j.info['dayHigh']
                    drawLabel('Previous Close : $' + str(prevClose), 240, 220, size = 15, fill ='red')
                    drawLabel("Today's Open : $" + str(open), 240, 250, size = 15, fill = 'green')
                    drawLabel("Today's Low : $" + str(low), 240, 280, size = 15, fill = 'red')
                    drawLabel("Today's High : $" + str(high), 240, 310, size = 15, fill ='green')
                    drawLabel('52 Week Low: $' + str(weekLow), 240, 340, size = 15, fill ='red')
                    drawLabel('52 Week High: $' + str(weekHigh), 240, 370, size = 15, fill ='green')
                    drawLabel('Outstanding Shares : ' + str(sharesO), 240, 400, size = 15, fill = 'blue')
                    drawLabel('Recent Quarter : $' + str(mrq), 240, 430, size = 15, fill = 'blue')
                    drawLabel('Float Shares : ' + str(floatShares), 240, 460, size = 15, fill = 'blue')
                    drawLabel('Trailing EPS : ' + str(teps), 240, 490, size = 15, fill ='red')
                    drawLabel('Forward EPS : ' + str(feps), 240, 520, size = 15, fill ='green')
                    drawLabel('Payout Ratio : ' + str(payout), 240, 550, size = 15, fill = 'blue')

                    #draws the news 
                    drawLabel('All Boxes are Clickable Links', 575, 185, bold = True, size = 15, fill = 'blue')
                    boxX = 400
                    boxY = 220
                    #draw the clickable boxes for the news
                    for i in range(3):
                        drawRect(boxX, boxY, 350, 90, border = 'black', fill = None)
                        boxY += 120

                    title1 = j.news[0]['title']
                    publisher1 = j.news[0]['publisher']

                    title2 = j.news[1]['title']
                    publisher2 = j.news[1]['publisher']

                    title3 = j.news[2]['title']
                    publisher3 = j.news[2]['publisher']

                    #first news
                    drawLabel('Title: ' + (str(title1)[:40]), 575, 235, size = 13, bold = True)
                    if len(title1) > 40:
                        title1 = j.news[0]['title'][40:]
                        drawLabel((str(title1)[:40]), 575, 250, size = 13, bold = True)
                    drawLabel('Publisher: ' + str(publisher1), 575, 295, size = 13, bold =True )

                    #second news
                    drawLabel('Title: ' + (str(title2)[:40]), 575, 355, size = 13, bold = True)
                    if len(title2) > 40:
                        title2 = j.news[1]['title'][40:]
                        drawLabel((str(title2)[:40]), 575, 370, size = 13, bold = True)
                    drawLabel('Publisher: ' + str(publisher2), 575, 415, size = 13, bold =True )

                    #third news
                    drawLabel('Title: ' + (str(title3)[:40]), 575, 475, size = 13, bold = True)
                    if len(title3) > 40:
                        title3 = j.news[2]['title'][40:]
                        drawLabel((str(title3)[:40]), 575, 490, size = 13, bold = True)
                    drawLabel('Publisher: ' + str(publisher3), 575, 535, size = 13, bold =True )

#drawing graph functions
def drawGraph(app):
    #for one year stocks
    for k in app.stockList:
        if k.oneYear == True:
            if app.analysisButton == True:
                count = -1
                for j in app.stockList:
                    count += 1
                    if (j.click == True and j.color == 'green' and j.oneYear == True) or j.small == 'green':
                        drawLabel('Time', 500, 480, size = 15)
                        drawLabel('Price', 265, 322,size = 15, rotateAngle = 90)
                        drawLabel("Up = Zoom Out",
                                  575, 50, size = 8, fill = 'blue')
                        drawLabel("Down = Zoom In",
                                  575, 65, size = 8,fill = 'blue')

                        graphData = app.dataList[count]
                    # Calculate graph dimensions based on zoom level
                        graphX = app.graphX
                        graphY = app.graphY

                        # Draw x and y axis
                        drawLine(graphX, app.height - graphY, graphX + app.graphWidth, app.height - graphY)  # x axis
                        drawLine(graphX, app.height - graphY, graphX, app.height - graphY - app.graphHeight)  # y axis
                        
                        numGridLines = 4
                        gridSpacing = app.graphHeight / (numGridLines + 1)
                        for i in range(numGridLines + 1):
                            y = app.height - graphY - i * gridSpacing
                            drawLine(graphX, y, graphX + app.graphWidth, y, opacity = 5, fill = 'grey') 

                        # Draw vertical grid lines
                        numPoints = int(len(graphData)/4)
                        xIncrement = app.graphWidth / (numPoints - 1)
                        for i in range(numPoints):
                            x = graphX + i * xIncrement
                            drawLine(x, app.height - graphY, x, app.height - graphY - app.graphHeight, opacity = 5, fill = 'grey') 

                        # Draw graph data
                        maxPrice = graphData['Close'].max()
                        minPrice = graphData['Close'].min()
                        priceRange = maxPrice - minPrice
                        numPoints = len(graphData)
                        xIncrement = app.graphWidth / (numPoints - 1) / app.zoomLevel

                        #mouse Hover functions
                        for i in range(numPoints - 1):
                            x1 = int(graphX + i * xIncrement)
                            x2 = int(graphX + (i + 1) * xIncrement)
                            y1 = int(app.height - graphY - ((graphData['Close'][i] - minPrice) / priceRange) * app.graphHeight)
                            y2 = int(app.height - graphY - ((graphData['Close'][i + 1] - minPrice) / priceRange) * app.graphHeight)
                            if j.small == 'green':
                                drawLine(x1,y1,x2,y2, fill ='green')
                            else:
                                drawLine(x1,y1,x2,y2)
                            
                        drawRect(700, 155, 50, 350, fill = 'white')
                        drawRect(750, 155, 50, 350, fill = 'oldLace')
                        for i in range(numPoints - 1):
                            x1 = int(graphX + i * xIncrement)
                            x2 = int(graphX + (i + 1) * xIncrement)
                            y1 = int(app.height - graphY - ((graphData['Close'][i] - minPrice) / priceRange) * app.graphHeight)
                            y2 = int(app.height - graphY - ((graphData['Close'][i + 1] - minPrice) / priceRange) * app.graphHeight)
                            if app.hoveredPrice is not None and app.hoveredPrice == graphData['Close'][i]:
                                drawCircle(x1, y1, 5)
                                drawRect(x1 + 50, y1 - 100, 125, 125, fill = 'pink', opacity = 50)
                                drawLabel('Price: $' + (str(app.hoveredPrice)[:6]), x1 + 110, y1 - 60, bold = True, fill = 'blue')
                                drawLabel('Date:' + str(app.hoveredDate), x1 + 110 , y1 - 40, bold = True, fill = 'blue')
       
       
        #for one month stocks
        elif k.oneMonth == True:
            if app.analysisButton == True:
                count = -1
                for j in app.stockList:
                    count += 1
                    if (j.click == True and j.color == 'green' and j.oneMonth == True) or j.small == 'green':
                        drawLabel('Time', 500, 480, size = 15)
                        drawLabel('Price', 265, 322,  size = 15, rotateAngle = 90)

                        drawLabel("Up = Zoom Out",
                                  575, 50, size = 8, fill = 'blue')
                        drawLabel("Down = Zoom In",
                                  575, 65, size = 8, fill = 'blue')
                        graphData = app.dataListMon[count]
                    # Calculate graph dimensions based on zoom level
                        graphX = app.graphX
                        graphY = app.graphY

                        # Draw x and y axis
                        drawLine(graphX, app.height - graphY, graphX + app.graphWidth, app.height - graphY)  # x axis
                        drawLine(graphX, app.height - graphY, graphX, app.height - graphY - app.graphHeight)  # y axis
                        numGridLines = 4
                        gridSpacing = app.graphHeight / (numGridLines + 1)
                        for i in range(numGridLines + 1):
                            y = app.height - graphY - i * gridSpacing
                            drawLine(graphX, y, graphX + app.graphWidth, y, opacity = 5, fill = 'grey') 

                        # Draw vertical grid lines
                        numPoints = int(len(graphData)/4)
                        xIncrement = app.graphWidth / (numPoints - 1) 
                        for i in range(numPoints):
                            x = graphX + i * xIncrement
                            drawLine(x, app.height - graphY, x, app.height - graphY - app.graphHeight, opacity = 5, fill = 'grey') 

                        # Draw graph data
                        maxPrice = graphData['Close'].max()
                        minPrice = graphData['Close'].min()
                        priceRange = maxPrice - minPrice
                        numPoints = len(graphData)
                        xIncrement = app.graphWidth / (numPoints - 1) / app.zoomLevel

                        

                        for i in range(numPoints - 1):
                            x1 = int(graphX + i * xIncrement)
                            x2 = int(graphX + (i + 1) * xIncrement)
                            y1 = int(app.height - graphY - ((graphData['Close'][i] - minPrice) / priceRange) * app.graphHeight)
                            y2 = int(app.height - graphY - ((graphData['Close'][i + 1] - minPrice) / priceRange) * app.graphHeight)
                            if j.small == 'green':
                                drawLine(x1,y1,x2,y2, fill ='green')
                            else:
                                drawLine(x1,y1,x2,y2)
                            
                        drawRect(700, 155, 50, 350, fill = 'white')
                        drawRect(750, 155, 50, 350, fill = 'oldLace')
                        for i in range(numPoints - 1):
                            x1 = int(graphX + i * xIncrement)
                            x2 = int(graphX + (i + 1) * xIncrement)
                            y1 = int(app.height - graphY - ((graphData['Close'][i] - minPrice) / priceRange) * app.graphHeight)
                            y2 = int(app.height - graphY - ((graphData['Close'][i + 1] - minPrice) / priceRange) * app.graphHeight)
                            if app.hoveredPrice is not None and app.hoveredPrice == graphData['Close'][i]:
                                drawCircle(x1, y1, 5)
                                drawRect(x1 + 50, y1 - 100, 125, 125, fill = 'pink', opacity = 50)
                                drawLabel('Price: $' + (str(app.hoveredPrice)[:6]), x1 + 110, y1 - 60, bold = True, fill = 'blue')
                                drawLabel('Date:' + str(app.hoveredDate), x1 + 110 , y1 - 40, bold = True, fill = 'blue')
        
        
        #for one week stocks
        elif k.threeYears == True:
            if app.analysisButton == True:
                count = -1
                for j in app.stockList:
                    count += 1
                    if (j.click == True and j.color == 'green' and j.threeYears == True) or j.small == 'green':
                        drawLabel('Time', 500, 480, size = 15)
                        drawLabel('Price', 265, 322,  size = 15, rotateAngle = 90)

                        drawLabel("Up = Zoom Out",
                                  575, 50, size = 8, fill = 'blue')
                        drawLabel("Down = Zoom In",
                                  575, 65, size = 8, fill = 'blue')
                        graphData = app.dataList3[count]
                    # Calculate graph dimensions based on zoom level
                        graphX = app.graphX
                        graphY = app.graphY

                        # Draw x and y axis
                        drawLine(graphX, app.height - graphY, graphX + app.graphWidth, app.height - graphY)  # x axis
                        drawLine(graphX, app.height - graphY, graphX, app.height - graphY - app.graphHeight)  # y axis
                        
                        numGridLines = 4
                        gridSpacing = app.graphHeight / (numGridLines + 1)
                        for i in range(numGridLines + 1):
                            y = app.height - graphY - i * gridSpacing
                            drawLine(graphX, y, graphX + app.graphWidth, y, opacity = 5, fill = 'grey') 

                        # Draw vertical grid lines
                        numPoints = int(len(graphData)/2)
                        xIncrement = app.graphWidth / (numPoints - 1)
                        for i in range(numPoints):
                            x = graphX + i * xIncrement
                            drawLine(x, app.height - graphY, x, app.height - graphY - app.graphHeight, opacity = 5, fill = 'grey') 

                        # Draw graph data
                        maxPrice = graphData['Close'].max()
                        minPrice = graphData['Close'].min()
                        priceRange = maxPrice - minPrice
                        numPoints = len(graphData)
                        xIncrement = app.graphWidth / (numPoints - 1) / app.zoomLevel

                        
                        
                        for i in range(numPoints - 1):
                            x1 = int(graphX + i * xIncrement)
                            x2 = int(graphX + (i + 1) * xIncrement)
                            y1 = int(app.height - graphY - ((graphData['Close'][i] - minPrice) / priceRange) * app.graphHeight)
                            y2 = int(app.height - graphY - ((graphData['Close'][i + 1] - minPrice) / priceRange) * app.graphHeight)
                            if j.small == 'green':
                                drawLine(x1,y1,x2,y2, fill ='green')
                            else:
                                drawLine(x1,y1,x2,y2)
                            
                        drawRect(700, 155, 50, 350, fill = 'white')
                        drawRect(750, 155, 50, 350, fill = 'oldLace')
                        for i in range(numPoints - 1):
                            x1 = int(graphX + i * xIncrement)
                            x2 = int(graphX + (i + 1) * xIncrement)
                            y1 = int(app.height - graphY - ((graphData['Close'][i] - minPrice) / priceRange) * app.graphHeight)
                            y2 = int(app.height - graphY - ((graphData['Close'][i + 1] - minPrice) / priceRange) * app.graphHeight)
                            if app.hoveredPrice is not None and app.hoveredPrice == graphData['Close'][i]:
                                drawCircle(x1, y1, 5)
                                drawRect(x1 + 50, y1 - 100, 125, 125, fill = 'pink', opacity = 50)
                                drawLabel('Price: $' + (str(app.hoveredPrice)[:6]), x1 + 110, y1 - 80, bold = True, fill = 'blue')
                                drawLabel('Date:' + str(app.hoveredDate), x1 + 110 , y1 - 65, bold = True, fill = 'blue')
                                drawLabel('Volume: ' + str(app.hoveredVolume), x1 + 110, y1 - 50, bold = True, fill = 'blue')
                                drawLabel('High: ' + (str(app.hoveredHigh)[:6]), x1 + 110, y1 - 35, bold = True, fill = 'blue')
                                drawLabel('Low: ' + (str(app.hoveredLow)[:6]), x1 + 110, y1 - 20, bold = True, fill = 'blue')
                                drawLabel('Open Price: $' + (str(app.hoveredOpen)[:6]), x1 + 110, y1 - 5, bold = True, fill = 'blue')
                    
    #for input time frame, must change data everytime new input 
    for m in app.stockList:
        if m.input == True and app.input == app.text:
            if (app.input[-1] == 'o' or 'd' or 'y') and type(app.input[0]) == str:
                if app.analysisButton == True:
                    count = -1
                    for j in app.stockList:
                        count += 1
                        if (j.click == True and j.color == 'green' and k.input == True) or j.small == 'green':
                            if j.name == 'MSFT':
                                msft = yf.Ticker("MSFT")
                                overData = msft.history(period= app.input)
                            elif j.name == 'AAPL':
                                aapl = yf.Ticker("AAPL")
                                overData = aapl.history(period= app.input)
                            elif j.name == 'AMZN':
                                msft1 = yf.Ticker("AMZN")
                                overData = msft1.history(period= app.input)
                            elif j.name == 'NVDA':
                                nvda = yf.Ticker("NVDA")
                                overData = nvda.history(period= app.input)
                            elif j.name == 'GOOG':
                                goog = yf.Ticker("GOOG")
                                overData = goog.history(period= app.input)
                            elif j.name == 'TSLA':
                                tsla = yf.Ticker("TSLA")
                                overData = tsla.history(period= app.input)
                            elif j.name == 'META':
                                meta = yf.Ticker("Meta")
                                overData = meta.history(period= app.input)
                            elif j.name == 'V':
                                v = yf.Ticker("V")
                                overData = v.history(period= app.input)
                            elif j.name == 'JNJ':
                                jnj = yf.Ticker("JNJ")
                                overData = jnj.history(period= app.input)
                            elif j.name == "UNH":
                                unh = yf.Ticker("UNH")
                                overData = unh.history(period= app.input)
                            elif j.name == 'BRK-A':
                                brk = yf.Ticker("BRK-A")
                                overData = brk.history(period= app.input)

                            drawLabel('Time', 500, 480, size = 15)
                            drawLabel('Price', 265, 322, size = 15, rotateAngle = 90)

                            drawLabel("Up = Zoom Out",
                                  575, 50, size = 8, fill = 'blue')
                            drawLabel("Down = Zoom In",
                                  575, 65, size = 8, fill = 'blue')
                            graphData = overData #[count]
                        # Calculate graph dimensions based on zoom level
                            graphX = app.graphX
                            graphY = app.graphY

                            # Draw x and y axis
                            drawLine(graphX, app.height - graphY, graphX + app.graphWidth, app.height - graphY)  # x axis
                            drawLine(graphX, app.height - graphY, graphX, app.height - graphY - app.graphHeight)  # y axis
                            
                            numGridLines = 4
                            gridSpacing = app.graphHeight / (numGridLines + 1) / app.zoomLevel 
                            for i in range(numGridLines + 1):
                                y = app.height - graphY - i * gridSpacing
                                drawLine(graphX, y, graphX + app.graphWidth, y, opacity = 5, fill = 'grey') 
                            # Draw vertical grid lines
                            
                            if len(graphData) <= 7:
                                numPoints = int(len(graphData)/2)
                            else:
                                numPoints = int(len(graphData)/4)
                            xIncrement = app.graphWidth / (numPoints - 1)
                            for i in range(numPoints):
                                x = graphX + i * xIncrement
                                drawLine(x, app.height - graphY, x, app.height - graphY - app.graphHeight, opacity = 5, fill = 'grey')

                            # Draw graph data
                            maxPrice = graphData['Close'].max()
                            minPrice = graphData['Close'].min()
                            priceRange = maxPrice - minPrice
                            numPoints = len(graphData)
                            xIncrement = app.graphWidth / (numPoints - 1)

                            

                            for i in range(numPoints - 1):
                                x1 = int(graphX + i * xIncrement)
                                x2 = int(graphX + (i + 1) * xIncrement)
                                y1 = int(app.height - graphY - ((graphData['Close'][i] - minPrice) / priceRange) * app.graphHeight)
                                y2 = int(app.height - graphY - ((graphData['Close'][i + 1] - minPrice) / priceRange) * app.graphHeight)
                                if j.small == 'green':
                                    drawLine(x1,y1,x2,y2, fill ='green')
                                else:
                                    drawLine(x1,y1,x2,y2)
                            
                            drawRect(700, 155, 50, 350, fill = 'white')
                            drawRect(750, 155, 50, 350, fill = 'oldLace')
                            for i in range(numPoints - 1):
                                x1 = int(graphX + i * xIncrement)
                                x2 = int(graphX + (i + 1) * xIncrement)
                                y1 = int(app.height - graphY - ((graphData['Close'][i] - minPrice) / priceRange) * app.graphHeight)
                                y2 = int(app.height - graphY - ((graphData['Close'][i + 1] - minPrice) / priceRange) * app.graphHeight)
                                if app.hoveredPrice is not None and app.hoveredPrice == graphData['Close'][i]:
                                    drawCircle(x1, y1, 5)
                                    drawRect(x1 + 50, y1 - 100, 125, 125, fill = 'pink', opacity = 50)
                                    drawLabel('Price: $' + (str(app.hoveredPrice)[:6]), x1 + 110, y1 - 60, bold = True, fill = 'blue')
                                    drawLabel('Date:' + str(app.hoveredDate), x1 + 110 , y1 - 40, bold = True, fill = 'blue')
                                    
            else:
                drawLabel('Invalid Time Frame Inputed', 500, 300, size = 20, fill = 'red')
                drawLabel('Please Try Again', 500, 340, size = 20, fill ='red')



#function that draws the prediction section of the tp 
def drawPredictionScreen(app):
    if app.predictionButton == True:
        #overall screen
        drawRect(0,0, 800, 600, fill = 'oldLace')
        drawRect(10, 10, 50, 25, fill = 'silver')
        #back button
        drawLabel('Return',35, 23, size = 10, fill= 'black', bold = True)
        #information section button
        drawCircle(280, 50, 30, fill = 'deepSkyBlue')
        drawLabel('i', 280, 50, size = 40, fill ='white', bold = True)
        drawLabel('Click or Press i for Stock Info', 280, 550, size = 15, fill = 'blue', bold = True)
        
        #change the color of the prediction selection boxes
        color = None
        colorRsi = None
        colormacd = None 
        if app.sma == True:
            color = 'purple'
        else:
            color = None

        if app.rsi == True:
            colorRsi = 'orange'
        else:
            colorRsi = None
        
        if app.macd == True:
            colormacd = 'blue'
        else:
            colormacd = None
        
        #labels and boxes for the technical indicators
        drawRect(200, 255, 100, 100, fill = color, border = 'black')
        drawLabel('Use SMA', 250, 305, size = 15, fill = 'black', bold = True)
        drawRect(350, 405, 100, 100, fill = colorRsi, border = 'black')
        drawLabel('Use RSI', 400, 455, size = 15, fill = 'black', bold = True)
        drawRect(500, 255, 100, 100, fill = colormacd, border = 'black')
        drawLabel('Use MACD', 550, 305, size = 15, fill = 'black', bold = True)

        count = -1
        for j in app.stockList:
            count += 1
            newWidth, newHeight = (125,125) 
            if j.click == True and j.color == 'green':
                #draw the names along with the company logo
                for names in app.nameList:
                    drawLabel(f'{app.nameList[count]}', 400, 100, bold = True, fill = 'green', size = 30)
                    drawImage(app.imageList[count], 600, 20, width = newWidth, height = newHeight)
                
                data = app.dataList1[count]

                if app.sma == True:
                    #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html
                    #I used the link to understand and learn the .rolling command 
                    # Calculate 20 and 50 day simple moving average
                    data['SMA20'] = data['Close'].rolling(window=20).mean()
                    data['SMA50'] = data['Close'].rolling(window=50).mean()
                    data['Prediction'] = None
                    #https://www.investopedia.com/articles/active-trading/052014/how-use-moving-average-buy-stocks.asp
                    #Used this link to solve how SMA's effect stock predictions
                    #Buy = SMA20 crosses above SMA50
                    #Sell = SMA20 crosses below SMA50
                    for i in range(len(data)):
                        if data['SMA20'][i] > data['SMA50'][i] and data['SMA20'][i - 1] <= data['SMA50'][i - 1]:
                            data['Prediction'][i] = 'Buy'
                        elif data['SMA20'][i] < data['SMA50'][i] and data['SMA20'][i - 1] >= data['SMA50'][i - 1]:
                            data['Prediction'][i] = 'Sell'
                    
                    data['Prediction'] = data['Prediction'].fillna(method='ffill')  # Forward-fill the initial NaN values
                    data['Prediction'] = data['Prediction'].fillna('None')

                    drawLabel('According to SMA Calculations: ', 400, 150, size = 20, bold = True )
                    if data.iloc[-1]['Prediction'] == 'Buy':
                        drawLabel(f'{app.buy}', 400, 200, size = 25, bold = True, fill = 'green')
                    elif data.iloc[-1]['Prediction'] == 'Sell':
                        drawLabel(f'{app.sell}', 400, 200, size= 25, bold = True, fill ='red')
                
                elif app.rsi == True:
                    #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.where.html
                    data['PriceChange'] = data['Close'].diff()
                    data['Gain'] = data['PriceChange'].where(data['PriceChange'] > 0, 0)
                    data['Loss'] = -data['PriceChange'].where(data['PriceChange'] < 0, 0)

                    #https://www.wallstreetmojo.com/relative-strength-index/
                    #how to calculate RSI
                    numRsi = 14  
                    avgGain= data['Gain'].rolling(window=numRsi).mean()
                    avgLoss = data['Loss'].rolling(window=numRsi).mean()

                    #raw math calculations
                    rs = avgGain / avgLoss
                    rsi = 100 - (100 / (1 + rs))
                    data['RSI'] = rsi

                    #rsi meanings and outcomes
                    data['Prediction'] = None
                    for i in range(14, len(data)):
                        if data['RSI'][i] > 30 and data['RSI'][i - 1] <= 30:
                            data['Prediction'][i] = 'Buy'
                        elif data['RSI'][i] < 70 and data['RSI'][i - 1] >= 70:
                            data['Prediction'][i] = 'Sell'
                    
                    data['Prediction'] = data['Prediction'].fillna(method='ffill')  # Forward-fill the initial NaN values
                    data['Prediction'] = data['Prediction'].fillna('None')

                    drawLabel('According to RSI Calculations: ', 400, 150, size = 20, bold = True )
                    if data.iloc[-1]['Prediction'] == 'Buy':
                        drawLabel(f'{app.buy}', 400, 200, size = 25, bold = True, fill = 'green')
                    elif data.iloc[-1]['Prediction'] == 'Sell':
                        drawLabel(f'{app.sell}', 400, 200, size= 25, bold = True, fill ='red')
                elif app.macd == True:
                    windowShort= 12  # Short-term EMA window
                    windowLong = 26  # Long-term EMA window
                    windowSignal = 9  # Signal line window
                    #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ewm.html
                    #how to use .ewm command
                    # Calculate Short Exponential Moving Average
                    data['ShortEMA'] = data['Close'].ewm(span=windowShort, adjust=False).mean()

                    # Calculate Long Exponential Moving Average
                    data['LongEMA'] = data['Close'].ewm(span=windowLong, adjust=False).mean()

                    # Calculate MACD Line
                    data['MACDLine'] = data['ShortEMA'] - data['LongEMA']

                    # Calculate Signal Line
                    data['SignalLine'] = data['MACDLine'].ewm(span=windowSignal, adjust=False).mean()
                    #https://www.investopedia.com/terms/m/macd.asp
                    #how to mathmatically calculate MACD
                    prediction = []
                    for i in range(len(data)):
                        if data.iloc[i-1]['MACDLine'] < data.iloc[i-1]['SignalLine'] and data.iloc[i]['MACDLine'] > data.iloc[i]['SignalLine']:
                            predictions = 'Buy'
                        elif data.iloc[i-1]['MACDLine']> data.iloc[i-1]['SignalLine'] and data.iloc[i]['MACDLine'] < data.iloc[i]['SignalLine']:
                            predictions = 'Sell'
                        else:
                            predictions = None
                        
                        prediction.append(predictions)
                    data['Prediction'] = predictions
                    drawLabel('According to SMA Calculations: ', 400, 150, size = 20, bold = True )
                    if data.iloc[-1]['Prediction'] == 'Buy':
                        drawLabel(f'{app.buy}', 400, 200, size = 25, bold = True, fill = 'green')
                    elif data.iloc[-1]['Prediction'] == 'Sell':
                        drawLabel(f'{app.sell}', 400, 200, size= 25, bold = True, fill ='red')
                    else:
                        drawLabel('Hold', 400, 200, size = 25, bold = True, fill = 'grey')


def drawPredictionInfo(app):
    if app.predictionInfo == True:
        #overall screen
        drawRect(0,0, 800, 600, fill = 'oldLace')
        drawRect(10, 10, 50, 25, fill = 'silver')
        #back button 
        drawLabel('Return',35, 23, size = 10, fill= 'black', bold = True)
        #SMA text 
        drawLabel('What is SMA?', 400, 50, size = 20, fill = 'purple', bold = True)
        drawLabel('SMA stands for Simple Moving Average, which is a commonly', 400, 75, size = 15, bold = True)
        drawLabel('used technical analysis tool in the stock market to identify trends.', 400, 90, size = 15, bold = True)
        drawLabel('It is calculated by adding up a set of data points', 400, 105, size = 15, bold = True)
        drawLabel('over a specific time period, and then dividing the sum by the number of data points in that period.', 400, 120, size = 15, bold = True)
        drawLabel('This gives an average value that represents the price over that time period, ', 400, 135, size = 15, bold = True)
        drawLabel('which can be used to identify potential trends and patterns in price movement.', 400, 150, size = 15, bold = True)

        #rsi text
        drawLabel('What is RSI?', 400, 400, size = 20, fill = 'orange', bold = True)
        drawLabel('RSI stands for Relative Strength Index, a momentum oscillator used in', 400, 425, size = 15, bold = True)
        drawLabel('technical analysis to measure the strength of price movements.', 400, 440, size = 15, bold = True)
        drawLabel('It is calculated based on the ratio of average gains to average losses', 400, 455, size = 15, bold = True)
        drawLabel('over a specified time period. RSI values range from 0 to 100, with readings above 70', 400, 470, size = 15, bold = True)
        drawLabel('indicating overbought conditions and readings below 30 indicating oversold conditions,', 400, 485, size = 15, bold = True)
        drawLabel('which can be used to identify potential trend reversals and overbought/oversold market conditions.', 400, 500, size = 15, bold = True)

        #macd text
        drawLabel('What is MACD?', 400, 200, size = 20, fill = 'blue', bold = True)
        drawLabel('MACD stands for Moving Average Convergence Divergence, a popular technical analysis', 400, 225, size = 15, bold = True)
        drawLabel('indicator used to identify potential trend reversals, momentum changes, and generate ', 400, 240, size = 15, bold = True)
        drawLabel('buy/sell signals in the stock market. MACD is calculated by subtracting the longer-term ', 400, 255, size = 15, bold = True)
        drawLabel('exponential moving average (EMA) from the shorter-term EMA, and then plotting a 9-day', 400, 270, size = 15, bold = True)
        drawLabel('between the MACD line and the signal line, known as the histogram, can provide insights ', 400, 285, size = 15, bold = True)
        drawLabel('into the strength of price momentum, and the MACD indicator is commonly plotted on a ', 400, 300, size = 15, bold = True)
        drawLabel('chart alongside the price of the security for analysis.', 400, 315, size = 15, bold = True)

#function that draws the information section of the tp 
def drawInfoScreen(app):
    if app.infoScreen == True:
        #overall screen
        drawRect(0,0, 800, 600, fill = 'oldLace')
        drawRect(10, 10, 50, 25, fill = 'silver')
        #back button 
        drawLabel('Return',35, 23, size = 10, fill= 'black', bold = True)
        drawLabel('Market', 230, 50, size = 100, font ='caveat', fill = 'green',
              bold = True) 
        drawLabel('Master', 565, 50, size = 100, bold = True, fill = 'red',
              font ='cinzel') #main label
        drawLabel('MarketMaster is a stock application designed to provide '
                  'users with essential information',
                  400, 125, size = 15, fill = 'black', bold = True)
        drawLabel('about the stock market.',
                  400, 155, size = 15, fill = 'black', bold = True)
        drawLabel('The application includes a range of features that '
                  'can help traders and investors make informed decisions',
                  400, 185, size = 15, fill = 'black', bold = True)
        drawLabel('about buying or selling stocks.',
                  400, 215, size = 15, fill = 'black', bold = True)
        drawLabel('View graphs: The heart of MarketMaster',
                  175, 285, size = 12, bold = True)
        drawLabel('is the stock graph section.',
                  175, 300, size = 12, bold = True)
        drawLabel('You can view graphs of stock data in a range',
                  175, 315, size = 12, bold = True)
        drawLabel('of formats.',
                  175, 330, size = 12, bold = True)
        drawLabel('You can also adjust the time frame of the data,',
                  175, 345, size = 12, bold = True)
        drawLabel('allowing you to view historical trends and patterns.',
                  175, 360, size = 12, bold = True)
        newWidth, newHeight = (250,250) 
        drawImage(app.candleimage,25, 370, 
                  width = newWidth, height = newHeight )
        drawLabel('Predictive analytics: One of the most powerful features',
                  600, 285, size = 12, bold = True)
        drawLabel('of MarketMaster is its predictive analytics section. ',
                  600, 300, size = 12, bold = True)
        drawLabel(' the app uses advanced algorithms to make predictions',
                600, 315, size = 12, bold = True)
        drawLabel('This can help you identify high-potential investment '
                  'opportunities',
                  600, 330, size = 12, bold = True)
        drawLabel('and make more profitable trades.', 
                  600, 345, size = 12, bold = True)
        
        newWidth1, newHeight1 = (400,250) 
        drawImage(app.predimage,380, 370, 
                  width = newWidth1, height = newHeight1 )
        
def redrawAll(app):
    drawMainScreen(app)
    drawAnalysisScreen(app)
    drawPredictionScreen(app)
    drawInfoScreen(app)
    drawStockInfo(app)
    drawPredictionInfo(app)
    
    #class drawing calls for prediction secton or the stock information section 
    if app.predictionButton == True or app.stockInfo == True:
        app.msftBox.drawBox(app, app)
        app.aaplBox.drawBox(app, app)
        app.amznBox.drawBox(app, app)
        app.nvdaBox.drawBox(app, app)
        app.googBox.drawBox(app, app)
        app.tslaBox.drawBox(app, app)
        app.metaBox.drawBox(app, app)
        app.vBox.drawBox(app, app)
        app.jnjBox.drawBox(app, app)
        app.unhBox.drawBox(app, app)
        app.brkBox.drawBox(app, app)
        app.msftBox.drawName(app)
        app.aaplBox.drawName(app)
        app.amznBox.drawName(app)
        app.nvdaBox.drawName(app)
        app.googBox.drawName(app)
        app.tslaBox.drawName(app)
        app.metaBox.drawName(app)
        app.vBox.drawName(app)
        app.jnjBox.drawName(app)
        app.unhBox.drawName(app)
        app.brkBox.drawName(app)
    
    #Class drawing calls for if on analysis screen
    if app.analysisButton == True:
        app.msftBox.drawBox(app, app)
        app.aaplBox.drawBox(app, app)
        app.amznBox.drawBox(app, app)
        app.nvdaBox.drawBox(app,app)
        app.googBox.drawBox(app, app)
        app.tslaBox.drawBox(app, app)
        app.metaBox.drawBox(app, app)
        app.vBox.drawBox(app, app)
        app.jnjBox.drawBox(app, app)
        app.unhBox.drawBox(app, app)
        app.brkBox.drawBox(app, app)
        app.msftBox.drawName(app)
        app.aaplBox.drawName(app)
        app.amznBox.drawName(app)
        app.nvdaBox.drawName(app)
        app.googBox.drawName(app)
        app.tslaBox.drawName(app)
        app.metaBox.drawName(app)
        app.vBox.drawName(app)
        app.jnjBox.drawName(app)
        app.unhBox.drawName(app)
        app.brkBox.drawName(app)
        drawGraph(app)

        #calls the graph hovering section in the corner
        if app.hoveredPrice is not None and app.analysisButton == True:
            drawRect(675, 0, 125, 125, fill = 'pink', opacity = 100)
            drawLabel('Close Price: $' + (str(app.hoveredPrice)[:6]), 740, 36, bold = True)
            drawLabel('Date: ' + str(app.hoveredDate), 740, 48, bold = True,)
            drawLabel('Volume: ' + str(app.hoveredVolume), 740, 60, bold = True)
            drawLabel('High: ' + (str(app.hoveredHigh)[:6]), 740, 72, bold = True)
            drawLabel('Low: ' + (str(app.hoveredLow)[:6]), 740, 84, bold = True)
            drawLabel('Open Price: $' + (str(app.hoveredOpen)[:6]), 740, 96, bold = True)

#on Mouse Move command, making boxes green, graphing hover feature
def onMouseMove(app, mouseX, mouseY):
    #changes the buttons to green in the home page
    if (app.mainAnalWidth1 < mouseX and app.mainAnalWidth2 > mouseX and 
        app.mainAnalHeight1 < mouseY and app.mainAnalHeight2 > mouseY):
        app.butAnalColor = 'green'
    else:
        app.butAnalColor = 'silver'
    if (app.mainPredWidth1 < mouseX and app.mainPredWidth2 > mouseX and 
        app.mainPredHeight1 < mouseY and app.mainPredHeight2 > mouseY):
        app.butPredColor = 'green'
    else:
        app.butPredColor = 'silver'

    #graphing hover feature for the normal black graph
    if app.analysisButton == True:
        count = -1
        if app.hover == True:
            for j in app.stockList:
                count += 1
                if (j.click == True and j.color == 'green'):
                    if app.threeYears == True:
                        graphData = app.dataList3[count]
                    elif app.oneMonth == True:
                        graphData = app.dataListMon[count]
                    elif app.oneYear == True:
                        graphData = app.dataList[count]
                    
                    elif app.selectedTime == True:
                        if j.name == 'MSFT':
                            msft = yf.Ticker("MSFT")
                            overData = msft.history(period= app.input)
                        elif j.name == 'AAPL':
                            aapl = yf.Ticker("AAPL")
                            overData = aapl.history(period= app.input)
                        elif j.name == 'AMZN':
                            msft1 = yf.Ticker("AMZN")
                            overData = msft1.history(period= app.input)
                        elif j.name == 'NVDA':
                            nvda = yf.Ticker("NVDA")
                            overData = nvda.history(period= app.input)
                        elif j.name == 'GOOG':
                            goog = yf.Ticker("GOOG")
                            overData = goog.history(period= app.input)
                        elif j.name == 'TSLA':
                            tsla = yf.Ticker("TSLA")
                            overData = tsla.history(period= app.input)
                        elif j.name == 'META':
                            meta = yf.Ticker("Meta")
                            overData = meta.history(period= app.input)
                        elif j.name == 'V':
                            v = yf.Ticker("V")
                            overData = v.history(period= app.input)
                        elif j.name == 'JNJ':
                            jnj = yf.Ticker("JNJ")
                            overData = jnj.history(period= app.input)
                        elif j.name == "UNH":
                            unh = yf.Ticker("UNH")
                            overData = unh.history(period= app.input)
                        elif j.name == 'BRK-A':
                            brk = yf.Ticker("BRK-A")
                            overData = brk.history(period= app.input)

                        graphData = overData
                    #gives the data for the pink box that moves and the one in the corner
                    if app.graphX <= mouseX <= app.graphX + app.graphWidth and app.height - app.graphY >= mouseY >= app.height - app.graphY - app.graphHeight:
                        xIncrement = app.graphWidth / (len(graphData) - 1)
                        index = int((mouseX - app.graphX) / xIncrement)
                        app.hoveredPrice = graphData['Close'][index]
                        app.hoveredDate = graphData.index[index].strftime('%Y-%m-%d')
                        app.hoveredVolume = graphData['Volume'][index]
                        app.hoveredHigh = graphData['High'][index]
                        app.hoveredLow = graphData['Low'][index]
                        app.hoveredOpen = graphData['Open'][index]
                        
                    else:
                        app.hoveredPrice = None
                        app.hoveredDate = None
                        app.hoveredVolume = None
                        app.hoveredHigh = None
                        app.hoveredLow = None
                        app.hoveredOpen = None

    #graphing hover feature for the green graph/comparasion graph
    if app.analysisButton == True:
        count = -1
        if app.hover == False:
            for k in app.stockList:
                count += 1
                if k.small == 'green':
                    if app.threeYears == True:
                        graphData = app.dataList3[count]
                    elif app.oneMonth == True:
                        graphData = app.dataListMon[count]
                    elif app.oneYear == True:
                        graphData = app.dataList[count]
                    
                    elif app.selectedTime == True:
                        if j.name == 'MSFT':
                            msft = yf.Ticker("MSFT")
                            overData = msft.history(period= app.input)
                        elif j.name == 'AAPL':
                            aapl = yf.Ticker("AAPL")
                            overData = aapl.history(period= app.input)
                        elif j.name == 'AMZN':
                            msft1 = yf.Ticker("AMZN")
                            overData = msft1.history(period= app.input)
                        elif j.name == 'NVDA':
                            nvda = yf.Ticker("NVDA")
                            overData = nvda.history(period= app.input)
                        elif j.name == 'GOOG':
                            goog = yf.Ticker("GOOG")
                            overData = goog.history(period= app.input)
                        elif j.name == 'TSLA':
                            tsla = yf.Ticker("TSLA")
                            overData = tsla.history(period= app.input)
                        elif j.name == 'META':
                            meta = yf.Ticker("Meta")
                            overData = meta.history(period= app.input)
                        elif j.name == 'V':
                            v = yf.Ticker("V")
                            overData = v.history(period= app.input)
                        elif j.name == 'JNJ':
                            jnj = yf.Ticker("JNJ")
                            overData = jnj.history(period= app.input)
                        elif j.name == "UNH":
                            unh = yf.Ticker("UNH")
                            overData = unh.history(period= app.input)
                        elif j.name == 'BRK-A':
                            brk = yf.Ticker("BRK-A")
                            overData = brk.history(period= app.input)

                        graphData = overData

                    #gives the data for the pink box that moves and the one in the corner
                    if app.graphX <= mouseX <= app.graphX + app.graphWidth and app.height - app.graphY >= mouseY >= app.height - app.graphY - app.graphHeight:
                        xIncrement = app.graphWidth / (len(graphData) - 1)
                        index = int((mouseX - app.graphX) / xIncrement)
                        app.hoveredPrice = graphData['Close'][index]
                        app.hoveredDate = graphData.index[index].strftime('%Y-%m-%d')
                        app.hoveredVolume = graphData['Volume'][index]
                        app.hoveredHigh = graphData['High'][index]
                        app.hoveredLow = graphData['Low'][index]
                        app.hoveredOpen = graphData['Open'][index]
                    else:
                        app.hoveredPrice = None
                        app.hoveredDate = None
                        app.hoveredVolume = None
                        app.hoveredHigh = None
                        app.hoveredLow = None
                        app.hoveredOpen = None


#mouse press command, clicking buttons and tme frames
def onMousePress(app, mouseX, mouseY):
    #Stock Analysis Button
    if (app.mainAnalWidth1 < mouseX and app.mainAnalWidth2 > mouseX and 
        app.mainAnalHeight1 < mouseY and app.mainAnalHeight2 > mouseY):
        app.analysisButton = True
        app.mainScreen = False
    #Stock Prediction Button 
    if (app.mainPredWidth1 < mouseX and app.mainPredWidth2 > mouseX and 
        app.mainPredHeight1 < mouseY and app.mainPredHeight2 > mouseY):
        app.predictionButton = True
        app.mainScreen = False
       
    #back button
    if (app.backButtWidth1 < mouseX and app.backButtWidth2 > mouseX 
        and app.backButtHeight1 < mouseY and app.backButtHeight2 > mouseY):
        app.mainScreen = True
        app.predictionButton = False
        app.analysisButton = False
        app.infoScreen = False
    #information button
    if (app.infoButtWidth1 < mouseX and app.infoButtWidth2 > mouseX 
        and app.infoButtHeight1 < mouseY and app.infoButtHeight2 > mouseY):
        app.mainScreen = False
        app.infoScreen = True

    #switching between graphs and information inside the analysis page
    if app.analysisButton == True:
        if 250 < mouseX and 310 > mouseX and 20 < mouseY and 80 > mouseY:
            app.analysisButton = False
            app.stockInfo = True
    elif app.predictionButton == True:
        if 250 < mouseX and 310 > mouseX and 20 < mouseY and 80 > mouseY:
            app.predictionButton = False
            app.predictionInfo = True


    #back button for the stock information page
    if app.stockInfo == True:
        if (app.backButtWidth1 < mouseX and app.backButtWidth2 > mouseX 
        and app.backButtHeight1 < mouseY and app.backButtHeight2 > mouseY):
            app.analysisButton = True
            app.stockInfo = False

    #back button for the prediction information page
    if app.predictionInfo == True:
        if (app.backButtWidth1 < mouseX and app.backButtWidth2 > mouseX 
        and app.backButtHeight1 < mouseY and app.backButtHeight2 > mouseY):
            app.predictionButton = True
            app.predictionInfo = False

    #clicking time frame buttons 
    if (150 < mouseX and 230 > mouseX and 155 < mouseY and 235 > mouseY):
                app.oneMonth = True
                app.oneYear = False
                app.threeYears = False
                app.selectedTimeColor = 'silver'
                app.text = ''
                app.selectedTime = False
    elif (150 < mouseX and 230 > mouseX and 255 < mouseY and 335 > mouseY):
            app.oneYear = True
            app.oneMonth = False
            app.threeYears = False
            app.selectedTimeColor = 'silver'
            app.text = ''
            app.selectedTime = False
    elif (150 < mouseX and 230 > mouseX and 355 < mouseY and 435 > mouseY):
            app.threeYears = True
            app.oneYear = False
            app.oneMonth = False
            app.selectedTimeColor = 'silver'
            app.text = ''
            app.selectedTime = False
    elif (150 < mouseX and 230 > mouseX and 55 < mouseY and 135 > mouseY):
            app.threeYears = False
            app.oneYear = False
            app.oneMonth = False
            app.selectedTime = True
            app.selectedTimeColor = 'green'

    #opening the websites for each stock, Piazza @1751 
    count = -1
    for j in app.stockList:
        count += 1
        if app.analysisButton == True:
            if j.click == True and j.color == 'green':
                if 570 < mouseX and 770 > mouseX and 530 < mouseY and 590 > mouseY:
                    website = app.websiteList[count]
                    webbrowser.open(website)

    #opening the websites for the news feature, Piazza @1751 
    num = -1
    for j in app.stockList:
        num += 1
        if app.stockInfo == True:
            if j.click == True and j.color == 'green':
                if 400 < mouseX and 750 > mouseX and 220 < mouseY and 310 > mouseY:
                    page = str(j.news[0]['link'])
                    webbrowser.open(page)
                if 400 < mouseX and 750 > mouseX and 340 < mouseY and 430 > mouseY:
                    page2 = str(j.news[1]['link'])
                    webbrowser.open(page2)
                if 400 < mouseX and 750 > mouseX and 460 < mouseY and 550 > mouseY:
                    page3 = str(j.news[2]['link'])
                    webbrowser.open(page3)

    #calls for the class to change graphs, info and etc... 
    app.msftBox.onMousePress1(mouseX, mouseY, app)
    app.aaplBox.onMousePress1(mouseX, mouseY, app)
    app.amznBox.onMousePress1(mouseX, mouseY, app)
    app.nvdaBox.onMousePress1(mouseX, mouseY, app)
    app.googBox.onMousePress1(mouseX, mouseY, app)
    app.tslaBox.onMousePress1(mouseX, mouseY, app)
    app.metaBox.onMousePress1(mouseX, mouseY, app)
    app.vBox.onMousePress1(mouseX, mouseY, app)
    app.jnjBox.onMousePress1(mouseX, mouseY, app)
    app.unhBox.onMousePress1(mouseX, mouseY, app)
    app.brkBox.onMousePress1(mouseX, mouseY, app)

    #loop to check change graphs and "stockBox class"
    for i in app.stockList:
        if i.color == 'green' and i.click == False:
            i.color = None
    
    #clicking prediction choices
    if app.predictionButton == True:
        if 200 < mouseX and 300 > mouseX and 255 < mouseY and 355 > mouseY:
            app.sma = True
        else:
            app.sma = None

        if 350 < mouseX and 450 > mouseX and 405 < mouseY and 505 > mouseY:
            app.rsi = True
        else:
            app.rsi = None
        
        if 500 < mouseX and 600 > mouseX and 255 < mouseY and 355 > mouseY:
            app.macd = True
        else:
            app.macd = None


def onKeyPress(app, key):
    #zooming feature
    if app.analysisButton == True:
        if key == 'up':
            app.zoomLevel += 0.1  # Increase zoom level
            if app.zoomLevel > 1.7:
                app.zoomLevel = 1.7
        elif key == 'down':
            app.zoomLevel -= 0.1  # Decrease zoom level
            if app.zoomLevel < 0.3:  # Set minimum zoom level
                app.zoomLevel = 0.3

    #input time frame feature
    if app.selectedTime == True:
        if key == 'enter':
            app.input = app.text
        elif key == 'backspace':
            app.text = app.text[:-1]
        else:
            app.text += key

    #switching inbetween graph hover sections
    #From the green comparasion graph to the regular one 
    for i in app.stockList:
        if i.small =='green':
            if key == 's':
                if app.hover == False:
                    app.hover = True
                else:
                    app.hover = False

    #clickable information screens for multiple pages
    if app.mainScreen == True:
        if key == 'i':
            app.mainScreen = False
            app.infoScreen = True


    if app.analysisButton == True:
        if key == 'i':
            app.analysisButton = False
            app.stockInfo = True


    if app.predictionButton == True:
        if key == 'i':
            app.predictionButton = False
            app.predictionInfo = True

        


runApp(width=800, height=600)


