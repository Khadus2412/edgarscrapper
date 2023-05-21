# EDGAR Database Parser Bot

EDGAR database scrapping bot that goes through 10-Q and 10-K forms to collect financial information. 

### Background
The EDGAR database collects about 3000 terabytes of data on annual basis. The data includes financial information about American companies and foriegn companies that operate in America. From around 2010 the SEC made it mandatory to format all uploaded data into a XML format for consistency in the structure of the data. 

### Description
The main purpose of this bot is to go through specifically 10-Q and 10-K forms (annual and quarterly financial statements) of companies and collect their data to compile into a dataframe. With the XML format of these forms the bot uses the element tree package to parse through the text versions of the files. 

Once collected the data is then turned into a table for SQLlite to structure into a dataframe for use. 

