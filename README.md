# CEPS Coding Challenge - WEBSCRAPING and SQL
This is a small challenge set for all applicants that would like to apply to [this open position at CEPS](https://jobs.unibas.ch/offene-stellen/junior-developer/f4835ec8-936c-4ed2-a953-d720740f92cc). 
We have two small tasks for you:
1. **Webscraping** - It is a simple webscraping task that we already implemented. So it is a real use case, and it is not only for us to see how you approach problems, but also for you to get an idea what kind of problems you can expect. 
2. **SQL** - We would provide you with the structure of a few tables in our database and ask you to write an sql query for a defined problem statement. The idea again is to introduce you to the kind of problems you can expect.

## 1 - WEBSCRAPING TASK

### Scrape Email Adresses
The goal of this challenge is to write a simple script that scrapes email-addresses of a given entity (this could be a company, foundation, NGO or any other kind of organization). All information given is the name of the entity.

### Task Description
1. Write a function that takes the entity name as an input, then runs a webscraper algorithm that looks out for email-addresses of that entity and returns the findings as an array (or empty array/null if nothing was found). If you find multiple addresses, gather all of them.
2. The webscraping algorithm could be something like this (PSEUDO CODE): 
```python
def scrape_emails(entity_name)
  # SCRAPE ALGORITHM PSEUDO CODE
  # 1. open webbrowser
  # 2. google the entity_name
  # 3. when google returns results, open the first result
  # 4. extract all email addresses from this website
  # OPTIONAL: if no email address is found in previous step, search for a contacts page, click on it, and redo step 4.
  # return emails as array
end
```
3. If you have a function that works for a single entity name, write a script where you iterate over a list of entity names, scrape them and store the results in a file of your choice (JSON, csv, XML, ...). Use the files described in the next section as inputs.

### Data
This repo contains the folder [webscraping_task](/webscraping_task) which further contains 3 files:
- **`entity_names_example.txt`**: In this file you find 3 entities to test your algorithm. They are manually selected and should be easy to scrape.
- **`entity_names_example_SOLUTION.json`**: here you will find the emails your scraper should find for all 3 examples. You can use this to check if your scraper works.
- **`entity_names_real.txt`**: This is real data used for this scraping task. You can run your script with this real data and send the results. 



## 2 - SQL TASK

### SQL query 
The goal of this task is to write an SQL query that gives the count of number the people in the foundation board of all the foundations in Basel canton- overall count, international candidates, swiss nationals. Furthermore, it would also be interesting to know that in each of these three categories how many people are citizens of/residing in Basel canton.
The table structure of the all the tables needed for this task is in the folder [sql_task](/sql_task).

### Task Description
Please read the following points carefully to understand the task.
1. You have a list of foundations from whole of switzerland, a few of which are in canton Basel = (BS).
2. Each foundation has a board of members.
3. If a person is classified as a 'President' or 'Member', he is a board member.
4. The task is to first find the overall count of the people who are board members of the foundations in Basel.
5. Then find out how many of those board members are swiss nationals and how many are internationals. (swiss nationals are marked as "CH_res").
6. Then find out how many of those people in the board are also citizens of or residents in Basel canton. 

### Data
The data concerns the non-profit organizations in switzerland and is available in mainly 3 languages - Deutsch, Italian and French. This repo contains the folder [sql_task](/sql_task) which further contains 4 files to give you an idea of the table structure of the following tables:
- **`foundations.xlsx`**: Contains the columns **`id`**, **`foundation_name`**, **`canton`**
- **`people.xlsx`**: Contains the columns **`id`**, **`first_name_id`**, **`last_name`**, **`citizen`**, **`residence`**, **`nationality`** 
- **`foundation_people.xlsx`**: Contains the columns **`id`**, **`foundation_id`**, **`person_id`**, **`function_class`**, **`function_full`**
- **`first_names.xlsx`**: Contains the columns **`id`**, **`first_name`**, **`gender`**



## Rules
1. **any language and any scraping framework is allowed for the webscraping task**: but it's a plus if you use **`ruby`**/**`python`** as your programming language and **`selenium`** web-driver for scraping, since this is the stack we are working with. 
2. the script does not have to be perfect. Webscraping is never accurate, there will be always noise and wrongly classified data, especially when you run the real data example.
3. The tasks are simple and easy to understand.
4. If you have any questions, please don't hesitate to contact me via mail (manvi.bhatia@unibas.ch).
5. There is no time limit to this coding-challenge, but ideally you can implement it in 6-8h. 

**HAPPY CODING** 🚀
