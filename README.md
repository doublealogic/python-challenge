# Py Me Up, Charlie

## Background

This repository contains a multi-project task where I was asked to create **two** Python programs, PyBank and PyPoll. 

### Pre-Programming Prep

* First, I created this repository on GitHub and then cloned it to my computer.

* Inside my local git repository, I created a directory for both Python programs. 

* Inside both `PyBank` and `PyPoll` folders, I was tasked to add:

  * A new file called `main.py`. This would be the main script I would be running for each analysis.
  * A `Resources` folder that would hold the respective CSV files I would use in each program. 
  * An `analysis` folder that would hold a text file that has the results from my analysis.

* I then pushed the above changes to GitHub or GitLab.

## PyBank

* This portion of the project required me to create a Python script for analyzing the financial records of a company. I was given a set of their financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). Within the dataset there were two columns: `Date` and `Profit/Losses`. 

* My task was to create a Python script that analyzed the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* Over the 86 month period, it was interesting to note that their average changes in profit skewed negative, with their biggest loss in September of 2013.

* My final script both prints the analysis to the terminal and exports a text file to the `analysis` folder with the results.

