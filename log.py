#!/usr/bin/env python3
import psycopg2

username = "superadmin"
password = "admin"
DB_NAME = "news"
# What are the most popular three articles of all time?
query_1_title = "What are the most popular three articles of all time?"

query1 = ("select a.title , count(l.*) as num "
          "from log l , articles a "
          "where l.path=CONCAT('/article/',a.slug) "
          "group by a.title order by num desc limit 3;")

# Who are the most popular article authors of all time?
query_2_title = "Who are the most popular article authors of all time?"

query2 = ("select sum(num) as views, name "
          "from ArticleCount"
          " group by name "
          "order by views desc")

# On which days did more than 1% of requests lead to errors
query_3_title = ("days > 1% of requests lead to errors?")
query3 = (
    "select to_char(day,'Mon DD,YYYY')"
    " as day,error_percentage"
    " from error_percentage"
    " where error_percentage>1.0")

# store results in dict to be easy in access

query1_result = dict([("title", "most popular articles of all time:\n")])

query2_result = dict([("title", " most popular authors of all time: \n")])

query3_result = dict([("title", " Days > 1% of request error:\n")])


# returns query result
def get_query_result(query):
    db = psycopg2.connect(database=DB_NAME, user=username, password=password)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_query_results(query_result):
    print(query_result['title'])
    for result in query_result['results']:
        print( str(result[1]) + '   ' + str(result[0]) + ' views' + '\n')


def print_error_percentage(query_result):
    print(query_result['title'])
    for result in query_result['results']:
        print( str(result[0]) + '   ' + str(result[1]) + ' %' + '\n')


# stores the results
query1_result['results'] = get_query_result(query1)
query2_result['results'] = get_query_result(query2)
query3_result['results'] = get_query_result(query3)

# print required output
print_query_results(query1_result)
print_query_results(query2_result)
print_error_percentage(query3_result)
