# Data Processes for Is a Wale

In this repositry you can find a workflow where I try to understand: 'What is a whale' in terms of money and also in amount of crypto asset. In general we think about the whale as an amount of money. But I whant to know: how many BTCs, ETHs, and etc are whales. This amount is affected by the price fluctuations.

## Whale Alert - Overall process 

Whale alert is an scraper which can be used for known how many bitcoins, or other criyptocurrencies are considered a whale.

![](documentation/whale-alert.png) 

# TODOS

Whale Alert - https://whale-alert.io/whales.html - Whale alerts have in their documentation: https://docs.whale-alert.io/#introduction information about the endpoints. But we can’t have information about what a whale is. So, we can create a process (and an api) that gives the information to the users. This information is in that web: https://whale-alert.io/whales
* Scraping web alert:
    * Create a table
    * Change format to millions
    * Add the numbers of cryptocurrencies that represent the amount
    * Take into consideration the total volume operated

* Exploring Web alert API
* https://www.blockchainresearchlab.org/2022/07/29/the-role-of-whale-alerts-and-sentiment-in-bitcoins-reaction-to-minting-and-burning-of-tethers-usdt/

## Miscellany

- I'm working in this projects besides others in Django. So I've two Postgre running in my computer. One installed standalone (The one that is used in Django) and other that is ran by Docker when I want to work with this project. If you are in the same situation than me, you'll need to stop one instance to be able to run the other. I found this tip in the following link: https://www.commandprompt.com/education/how-to-start-stop-or-restart-the-postgresql-server/ - (I stop the postgree server, run one that is in docker and start working in the data project) - If there is a better way to work let me know (Thanks in advance!)