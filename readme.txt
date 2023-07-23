A short description of the project's name and what it does.

My term project will be named MarketMaster. MarketMaster is a stock market graphing application 
that has a variety of features allowing users to get better information about the 
financial market. Features that are included are stock selection,
time frame selection, chart selection, comparison and technical indicators. 
Stock Selection will allow users to select the stock or stocks they want to view on the graph.
Time Frame selection will allow users to select the time frame they want to view on the graph,
such as daily, weekly, monthly, or yearly. Technical indicators such as moving averages,
MACD, and Relative Strength Index (RSI) will provide more insights into the stock's
performance which will serve as a predictor to buy and sell stocks. 
The graph comparison will allow users to compare different stocks or market indices 
on the same graph. Finally, there is a key data and news section that allows users to view
tons of data as well as the news surrounding each stock. 

How to run the project. 

My user will need to use the Tp3.py file that exists inside this folder and place it inside
their 15-112 folder (or have pip installed cmu_graphics). They will also need to move the images
folder inside this folder to a location with cmu_graphics. Once the code is opened on vscode 
then the user can run the file and the program will run. 


Which libraries you're using that need to be installed, if any.

from cmu_graphics import *
import yfinance as yf
from PIL import Image
import pandas as pd
import os, pathlib
from datetime import datetime
import webbrowser


A list of any shortcut commands that exist.

Once the user enters the main screen, they can use the "i" key to enter the 
information section. Users can also use this exact hot key for the analysis and prediction 
screens to access their private information sections. In the analysis section, users can 
use the "up" and "down" arrows to zoom in/out of the graph as well as use the "s"
key to switch between graph hover features (granted there are 2 graphs activated). 

