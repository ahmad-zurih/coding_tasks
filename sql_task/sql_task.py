import pandas as pd
import sqlite3

# upload the excel files as pandas dataframes
first_names = pd.read_excel(
    'first_names.xlsx',
    sheet_name='first_names',
    header=0)

foundation_people = pd.read_excel(
    'foundation_people.xlsx',
    sheet_name='foundation_people',
    header=0)

foundations = pd.read_excel(
    'foundations.xlsx',
    sheet_name='foundations',
    header=0)

people = pd.read_excel(
    'people.xlsx',
    sheet_name='people',
    header=0)

# create the database
connection = sqlite3.connect("coding_task.db")
cursor = connection.cursor()

# create the tables with the values
cursor.execute("""
    CREATE TABLE IF NOT EXISTS first_names(
        id INT PRIMARY KEY,
        first_name TEXT,
        name_sanitized TEXT,
        gender TEXT
        );"""
               )


cursor.execute("""
    CREATE TABLE IF NOT EXISTS foundation_people(
        id INT PRIMARY KEY,
        foundation_id INT,
        person_id INT,
        function_class TEXT,
        function_full TEXT,
        FOREIGN KEY(foundation_id) REFERENCES foundation(id),
        FOREIGN KEY(person_id) REFERENCES people(id)
        );"""
               )


cursor.execute("""
    CREATE TABLE IF NOT EXISTS foundations(
        id INT PRIMARY KEY,
        foundation_name TEXT,
        canton TEXT
        );"""
               )


cursor.execute("""
    CREATE TABLE IF NOT EXISTS people(
        id INT PRIMARY KEY,
        first_name_id INT,
        last_name TEXT,
        citizen TEXT,
        residence TEXT,
        nationality TEXT,
        FOREIGN KEY(first_name_id) REFERENCES first_name(id)
        );"""
               )

# add the values into the database
first_names.to_sql('first_names', connection, if_exists='append', index=False)
foundation_people.to_sql('foundation_people', connection, if_exists='append', index=False)
foundations.to_sql('customers', connection, if_exists='append', index=False)
people.to_sql('people', connection, if_exists='append', index=False)

# save changes
connection.commit()


# count of the people who are board members of the foundations in Basel.
cursor.execute("""
    SELECT COUNT(function_class)
    FROM foundation_people
    INNER JOIN foundations
        ON foundation_people.foundation_id = foundations.id
    WHERE foundation_people.function_class = "MEMBER"
    OR foundation_people.function_class = "PRESIDENT"
    AND foundations.canton = "BS"
    """)
print(cursor.fetchall())

# how many of those board members are swiss nationals
cursor.execute("""
    SELECT COUNT(function_class)
    FROM foundation_people 
    INNER JOIN foundations
        ON foundation_people.foundation_id = foundations.id
    INNER JOIN people
        ON foundation_people.person_id = people.id
    WHERE foundation_people.function_class = "MEMBER"
    OR foundation_people.function_class = "PRESIDENT"
    AND foundations.canton = "BS" 
    AND people.nationality = "CH_res"
    """)

print(cursor.fetchall())
# how many of those board members are NOT swiss nationals
cursor.execute("""
    SELECT COUNT(function_class)
    FROM foundation_people
    INNER JOIN foundations
        ON foundation_people.foundation_id = foundations.id
    INNER JOIN people
        ON foundation_people.person_id = people.id
    WHERE foundation_people.function_class = "MEMBER"
    OR foundation_people.function_class = "PRESIDENT"
    AND foundations.canton = "BS"
    AND people.nationality != "CH_res"
    """)

print(cursor.fetchall())

# people in the board who are swiss citizens and residents in Basel.
cursor.execute("""
    SELECT COUNT(function_class)
    FROM foundation_people
    INNER JOIN foundations
        ON foundation_people.foundation_id = foundations.id
    INNER JOIN people
        ON foundation_people.person_id = people.id
    WHERE foundation_people.function_class = "MEMBER"
    OR foundation_people.function_class = "PRESIDENT"
    AND foundations.canton = "BS"
    AND people.nationality = "CH_res"
    AND people.residence = "Basel"
    """)

print(cursor.fetchall())

# people in the board who are residents in Basel regardless of nationality.
cursor.execute("""
    SELECT COUNT(function_class)
    FROM foundation_people
    INNER JOIN foundations
        ON foundation_people.foundation_id = foundations.id
    INNER JOIN people
        ON foundation_people.person_id = people.id
    WHERE foundation_people.function_class = "MEMBER"
    OR foundation_people.function_class = "PRESIDENT"
    AND foundations.canton = "BS"
    AND people.residence = "Basel"
    """)

print(cursor.fetchall())