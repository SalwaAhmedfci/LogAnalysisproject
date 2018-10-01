### LOGS ANALYSIS
#### H2

I have work with PgAdmin which is the most popular and feature rich Open Source administration and development platform for PostgreSQL, the most advanced Open Source database in the world.

pgAdmin may be used on Linux, Unix, Mac OS X and Windows to manage PostgreSQL 9.2.
you can download it from here :
https://www.pgadmin.org/

How to Run?

PreRequisites:

1-Python3
2-Vagrant
3-VirtualBox




  



Follow the steps below to access the code of this project:

1-If you don't already have the latest version of python download it from the link in requirements.
2-Download and install Vagrant and VirtualBox.
Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  $ vagrant up
Then Log into this using command:
  $ vagrant ssh
3-Download this Udacity folder with preconfigured vagrant settings. from here:https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip
4-Clone this repository.
Change directory to /vagrant and look around with ls.
5-Download this database.from here :https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
6-Navigate to the Udacity folder in your bash interface and inside that cd into the vagrant folder.
7-launch the virtual machine with vagrant up from GitBash.
8-Once Vagrant installs necessary files use vagrant ssh to login.
9-To load the database type psql -d news -f newsdata.sql
10-To run the database type psql -d news
11-run log.py run the python program that fetches query results.
open log.py file using python IDE and run it using the command :
   python log.py


The database includes three tables:

The authors table includes information about the authors of articles.
The articles table includes the articles themselves.
The log table includes one entry for each time a user has accessed the site.
Use psql -d news to connect to database.


Created Views:
-CREATE VIEW total_req AS
SELECT count(*) AS num,
       date(TIME) AS day
FROM log
GROUP BY day
ORDER BY num DESC;

-CREATE VIEW error_req AS
SELECT count(*) AS num,
       date(TIME) AS day
FROM log
WHERE status like '4%' or status like '5%'
GROUP BY day
ORDER BY num DESC;

-CREATE VIEW error_percentage AS
SELECT total_req.day,
       round((100.0*error_req.num)/total_req.num,2) AS error_percentage
FROM error_req,
     total_req
WHERE error_req.day=total_req.day
and round((100.0*error_req.num)/total_req.num,2)>1;


1- this query to access that most popular  three articles:

[select a.title , count(l.*) as num from "log" l , articles a where l.path like CONCAT('%',a.slug,'%') group by a.title order by num desc limit 3]

-which selects the title and num from the two tables log and articles under the condition of the equality or partial equality of the slug and title and order that all in descending order 
and shows only the first 3 outputs 

-the output samples of that query is stored in (mostpoparticle.csv) without limit 3
-the output samples of that query is stored in (mostpoparticlelimit.csv) with limit 3



question two:

2- these queries to get most puplic authors of all the time:

[create view ArticleCount as
select l.path, au.name, count(l.*) as num , ar.title  from articles ar, authors au, "log" l where ar.author = au.id and l.path like CONCAT('%',ar.slug) group by l.path, au.name, ar.title order by num desc]

[select sum(num) as views, name from ArticleCount group by name order by views desc]

-it create a view which carries the name of each article  and the author of it redundantly  in desc then  we sums the views to get the most popular

-the output samples of that query is stored in (popauthor.csv)  


3-it was a really hard question and took long time :
I have created 3 views the first is :

CREATE VIEW total_req AS
SELECT count(*) AS num,
       date(TIME) AS day
FROM log
GROUP BY day
ORDER BY num DESC;

- to collect the total number  requests

CREATE VIEW error_req AS
SELECT count(*) AS num,
       date(TIME) AS day
FROM log
WHERE status like '4%' or status like '5%'
GROUP BY day
ORDER BY num DESC;


-to collect number of error requests in certain day

//this part represent the view creation

CREATE VIEW error_percentage AS
SELECT total_req.day,
       round((100.0*error_req.num)/total_req.num,2) AS error_percentage
FROM error_req,
     total_req
WHERE error_req.day=total_req.day
and round((100.0*error_req.num)/total_req.num,2)>1;

- to calculate percentage of error

select to_char(day,'Mon DD,YYYY') as day,error_percentage from error_percentage where error_percentage>1.0


- to calculate the exact value that is > 1%





