# Expenses Manager

##### CLI python program to keep track of expenses.
<p>
Since TransferWise does not have any features to analyze your expenses, 
I developed this python project to manage my account expenses. 
It uses the exported csv file from TransferWise with the account 
movements to provide summaries and graphs of the information.
</p> 

#### Features
<p> Following commands are accepted:  </p>

* _*expyear y*_ (returns expenses of year y per month)
* _*expmonth m y*_ (returns expenses of month m and year y)
* _*expweeks l*_  (returns expenses of last l weeks)
* _*expcat (optional: category)*_ (prints expenses by category)
* _*expgraph y*_ (prints expenses of year y)
* _*catgraph y*_ (prints expenses of year y by category)