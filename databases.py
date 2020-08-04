# databases, SQLite database and standard module.
# database is just an organized collection of data that can be used to store
# information on a computer or access from a web server over the Internet.
# Note: Android uses many databases to store things like your contact info 
# text messages and your browser history, search history etc
# Anything that stores and retrieves information can really be called a database.
# However, the term is used to refer to more structured data.  

# SQL is structured Query Language for performing operations such as querying and
# updating data. A new one is NoSQL databases used for storing and processing big data
# SQLite is completely self-contained and doesnt need a seperate server to run on unlike 
# Oracle and SQL Server.
# Text messages on IPhone are stored in SQLite database.
# SQLite is fast and very stable stand-alone database.
# 
# DATABASE TERMINOLOGY:
# Databse - the container for all stored data
# In sqlite, the entire database is stored in a single file
# Databse dictionary - provides a comprehensive list of structures and tyes of data 
# used in recording the data in the database.
# In sqlite there is a table in each database called SQL_lite_master that has this 
# information in it you can query that table. However, there are commands that can do that.
# Table - A collection of related data held in the database.
# field is the basic unit of data in the table so similar way to what a variable is
# There are date fields, large text field and blobs(binary large object) - stored photographs or audio
# Fields are often referred to as columns in database; i.e single entry.
# Flat File database stores all data in a single table, which causes alot of duplicates. 
# Thus, aren't used often.
# 
# To avoid duplicates, you can split the data and combine them through a link. This is known as
# Normaization - is the process of removing redundant duplicatd and irrelevant data from the tables.
# 
# View - is a way of looking at the data in a format similar to a table. In other words, It is a 
# selection of rows and columns. It can contain one column from a single table.
# 
# the sqlite command line shell is already installed on a mac
# 
# Note: some sql statements can be terminated with a semi colon
# 
# .help
# .headers on
# create table contacts (name text, phone integer, email text);
# In sql lite if you do something wrong it will let you know but if everything works fine then 
# it is keeps quiet.
# 
# Use sql insert statement to put data.
# insert into contacts (name, phone, email) values ("Tim", 645321,"tims@gmail.com");
# Single or double quotes can be used.
# to know that these commands actually did something we can check that it has we can query the 
# table(select from).
# 
# There are sql reserved words such as tables and columns names etc
#  SELECT * FROM contacts;
# name|phone|email
# Tim|645321|tims@gmail.com
# SELECT name, phone,email FROM contacts;
# name|phone|email
# Tim|645321|tims@gmail.com

# The use of capital letters for the reserved words, is for emphasis only:
# SELECT email from contacts;
# email
# tims@gmail.com

# Where the semi colon isn't used, this is the result:
# SELECT email from contacts
#  ...> ;
# email
# tims@gmail.com
# 
# INSERT into contacts VALUES("Brian", 1234, "brian234@gmail.com");

# If we enter just 2 values we get an error:
# INSERT INTO contacts VALUES("Steve", 23456);
# Error: table contacts has 3 columns but 2 values were supplied

# So we can specify what data we want to assign the values to:
# INSERT INTO contacts(name, phone) VALUES("Steve", 23456);
# SELECT * from contacts;
# name|phone|email
# Tim|645321|tims@gmail.com
# Brian|1234|brian234@gmail.com
# Steve|23456| 

# We can put any type of data into any column in sqlite, as its better to use text than integers. 
# SELECT * from contacts;
# INSERT INTO contacts VALUES("Avril", "+61 (0)87825372", "avril@gmail.com");
# This didnt bring an error even when the initial column is int not text for phone.
# SELECT * from contacts;
# Tim|645321|tims@gmail.com
# Brian|1234|brian234@gmail.com
# Steve|23456| 
# Avril|+61 (0)87825372|avril@gmail.com

# If you dont specify where to update, the whole field updates:
# UPDATE contact SET email="steve@gmail.com";
# SELECT * from contacts;
# Tim|645321|steve@gmail.com
# Brian|1234|steve@gmail.com
# Steve|23456|steve@gmail.com
# Avril|+61 (0)87825372|steve@gmail.com
# This comand is very powerful and a single sql statement can update all rows in the db
 
# to get it back since we backed up, we can do
# .restore sqltestbackup
# SELECT * FROM contacts;
# Tim|645321|tims@gmail.com
# Brian|1234|brian234@gmail.com
# Steve|23456|
# Avril|+61 (0)87825372|avril@gmail.com

# To use the Update command for a single field, use the "where" clause:
#  UPDATE contacts SET email="steve@gmail.com" WHERE name = "Steve";
# SELECT * FROM contacts
#    ...> ;
# Tim|645321|tims@gmail.com
# Brian|1234|brian234@gmail.com
# Steve|23456|steve@gmail.com
# Avril|+61 (0)87825372|avril@gmail.com
# Avril|+61 (0)87825372|avril@gmail.com

# You can use the where clause even in select statement:
# DELETE FROM contacts WHERE name ="Avril";
# sqlite> SELECT * FROM contacts;
# Tim|645321|tims@gmail.com
# Brian|1234|brian234@gmail.com
# Steve|23456|steve@gmail.com

# After set up, you can use commands such as:
# .tables
# contacts
# sqlite> .schema
# CREATE TABLE contacts (name text, phone integer, email text);
# sqlite> .dump
# PRAGMA foreign_keys=OFF;
# BEGIN TRANSACTION;
# CREATE TABLE contacts (name text, phone integer, email text);
# INSERT INTO contacts VALUES('Tim',645321,'tims@gmail.com');
# INSERT INTO contacts VALUES('Brian',1234,'brian234@gmail.com');
# INSERT INTO contacts VALUES('Steve',23456,'steve@gmail.com');
# COMMIT;
# .exit 
# to leave.

# We're looking at views and join.
# Note: In relational databases is that the ordering of the rows is undefined, That's why
# you need an ID column. 
# Note: Not null
# Note autoincrement in sqlite for primary key.

# NOW order by and Joins.
# SELECT * FROM artists ORDER BY name;
# prints in alphabetical order.

# SELECT * FROM albums ORDER BY name COLLATE NOCASE;
# SELECT * FROM albums ORDER BY name COLLATE NOCASE DESC;

# SELECT * FROM albums ORDER BY artist, name COLLATE NOCASE;
# This sorts by artist Id and then by album.

# List all songs so that the songs from the same album appear together in track order:
# SELECT * FROM songs ORDER BY album, track COLLATE NOCASE;

# SQL Join is used to join tables:
# SELECT songs.track, songs.title, albums.name FROM songs JOIN albums ON songs.album = albums._id; OR
# SELECT track, title, name FROM songs JOIN albums ON song.album = albums._id;
# Note: Join is the short for INNER JOIN.
# SELECT songs.track, songs.title, album.name FROM songs INNER JOIN albums ON songs.album = albums._id
#  ORDER BY albums.name, songs.track;

# This puts the contents in order:
# SELECT albums.name, songs.track, songs.title FROM songs INNER JOIN albums ON songs.album = 
# albums._id ORDER BY albums.name, songs.track;

# To produce a list of all the artists with their albums in alphabetical order of artists name:
# SELECT artists.name, albums.name FROM albums INNER JOIN artists ON albums.artist = artists._id ORDER BY artists.name;

# SELECT artists.name, albums.name, songs.track, songs.title FROM songs
# INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artists ON albums.artist = artists._id
# ORDER BY artists.name, albums.name, songs.track;

# Note the ordering of the clauses is important.
# In using a WHERE clause it comes before the ORDER BY clause.

# select artists.name, albums.name, songs.track, songs.title from songs
# INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artists on albums.artist = artists._id
#    ...> WHERE albums._id = 19
#    ...> ORDER BY artists.name, albums.name, songs.track;

# select artists.name, albums.name, songs.track, songs.title from songs
#    ...> INNER JOIN albums ON songs.album = albums._id
#    ...> INNER JOIN artists on albums.artist = artists._id
#    ...> WHERE albums.name = "Doolittle"
#    ...> ORDER BY artists.name, albums.name, songs.track;

# INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artists on albums.artist = artists._id
# WHERE albums.name = "Doolittle"
# ORDER BY artists.name, albums.name, songs.track;

# WILDCARDS AND VIEWS:
