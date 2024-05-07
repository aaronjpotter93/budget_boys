# Budget Boys
Welcome to Budget Boys, the budgeting application that frees you from the constraints of one-size-fits-all financial tools. We believe in a dynamic approach to financial literacy, and Budget Boys is crafted to provide the utmost flexibility paired with a neural network that adapts to your unique organizational preferences.

# Transaction Management Ideas:
    - Selecting a category and choosing all the transactions that belong to that category
    - Having the neural network group transactions by what it thinks belong together and you can yay or nay them in batches

# Database Design Implementation Ideas:
    - Every purchase can have any number of attributes. And some of those attributes may belong to different named categories. ie. A purchase made on domanic can be for clothes. but since it was for domanic that purchase doesn't show up in the clothes summary, instead it shows up in domanics summary and contributes to the kid's total spendings and you can see how much money you've spent on him fanned out to all the attributes that those transactions have; clothes, food, travel ect ect. The neural network can learn how we want these attributes to be used in grouping transactions for summaries.

# Connecting Python to a database:
    - Create a new user in pgAdmin
    - Add an entry to the pg_hba.conf file:
    TYPE    DATABASE        USER            ADDRESS       METHOD
    host    budget_boys     your_username   IP Address    md5

