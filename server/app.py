'''
this needs to accept a search string, 
    - add the necessary boolean operators
    - run the query 
    - return the results

it might need to handle offsets, or it could just be limited to return a maximum
number of results that would always fit on the page
'''
import psycopg2                                                                                                                                                                                                    
from flask import Flask
from flask import jsonify

app = Flask(__name__, static_url_path='/static')
                                                                                                                                                                                                                   
connect_str = "dbname='vinyl' user='patrick' host='localhost' password='asdfasdf'"                                                                                                                                 
conn = psycopg2.connect(connect_str)                                                                                                                                                                               
cur = conn.cursor()                                                                                                                                                                                                

@app.route('/')
def index ():
    return app.send_static_file('html/index.html')


sql = '''
select 
    front, back, id, ts_rank_cd(for_search, to_tsquery(%s)) as score 
from records 
where 
    for_search @@ to_tsquery(%s) 
order by score desc;
'''

@app.route('/search/<search_query>')
def search (search_query):
    fmt_query = search_query.replace(' ', ' | ')
    cur.execute(sql, (fmt_query, fmt_query))
    rows = cur.fetchall()
    response_d = {
        'rows': []
    }
    for row in rows:
        response_d['rows'].append(row)
    return jsonify(response_d)

