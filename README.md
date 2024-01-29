# Budget Boys
Welcome to Budget Boys, the budgeting application that frees you from the constraints of one-size-fits-all financial tools. We believe in a dynamic approach to financial literacy, and Budget Boys is crafted to provide the utmost flexibility paired with a neural network that adapts to your unique organizational preferences.

# Transaction Management Ideas:
    - Selecting a category and choosing all the transactions that belong to that category
    - Having the neural network group transactions by what it thinks belong together and you can yay or nay them in batches

# Connecting Python to a database:
    - Create a new user in pgAdmin
    - Add an entry to the pg_hba.conf file:
    TYPE    DATABASE        USER            ADDRESS       METHOD
    host    budget_boys     your_username   IP Address    md5

# Testing Project IDX workflow
    - So does this know that I'm pushing to the repo and if so I don't understand how thats working. 
    - Ok now I see how its working. I was able to pull the repo branch without authenticating because the repo is public. but commiting and pushing needed me to authenticate with my github account.