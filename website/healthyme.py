import os
from flask import Flask, render_template, request
import MySQLdb as MS
from pattern.web import Wikipedia, plaintext, Google, Bing
from pattern.search import search
import requests

db = MS.connect(user="root", host="localhost")
with db:
	cursor=db.cursor()
	sql='USE ten_all_diseases'
	cursor.execute(sql)

app = Flask(__name__)
app.debu = True

@app.route("/")
def healthyme():
    return render_template('index_old.html') 


@app.route('/results_feb1.html', methods=['POST'])
def search():
	inputs = request.form
	age = inputs['age']
	sex = inputs['sex']
	race = inputs['race']
	if age == '1-4':
		Age = "Age='2a'"
		if sex == 'Female' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_f_asian !=1 ORDER BY p_f_asian DESC;"

		if sex == 'Female' and race == 'Black/African American':
			sql_query = "SELECT name,p_f_black FROM probabilities WHERE "+Age+" and p_f_black !=1 ORDER BY p_f_black DESC;"

		if sex == 'Female' and race == 'Hispanic':
			sql_query = "SELECT name,p_f_latino FROM probabilities WHERE "+Age+" and p_f_latino !=1 ORDER BY p_f_latino DESC;"

		if sex == 'Female' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_f_native FROM probabilities WHERE "+Age+" and p_f_native !=1 ORDER BY p_f_native DESC;"

		if sex == 'Female' and race == 'White':
			sql_query = "SELECT name,p_f_white FROM probabilities WHERE "+Age+" and p_f_white !=1 ORDER BY p_f_white DESC;"

		if sex == 'Male' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_m_asian !=1 ORDER BY p_m_asian DESC;"

		if sex == 'Male' and race == 'Black/African American':
			sql_query = "SELECT name,p_m_black FROM probabilities WHERE "+Age+" and p_m_black !=1 ORDER BY p_m_black DESC;"

		if sex == 'Male' and race == 'Hispanic':
			sql_query = "SELECT name,p_m_latino FROM probabilities WHERE "+Age+" and p_m_latino !=1 ORDER BY p_m_latino DESC;"

		if sex == 'Male' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_m_native FROM probabilities WHERE "+Age+" and p_m_native !=1 ORDER BY p_m_native DESC;"

		if sex == 'Male' and race == 'White':
			sql_query = "SELECT name,p_m_white FROM probabilities WHERE "+Age+" and p_m_white !=1 ORDER BY p_m_white DESC;"

	if age == '5-14':
		Age = "Age='3a'"
		if sex == 'Female' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_f_asian !=1 ORDER BY p_f_asian DESC;"

		if sex == 'Female' and race == 'Black/African American':
			sql_query = "SELECT name,p_f_black FROM probabilities WHERE "+Age+" and p_f_black !=1 ORDER BY p_f_black DESC;"

		if sex == 'Female' and race == 'Hispanic':
			sql_query = "SELECT name,p_f_latino FROM probabilities WHERE "+Age+" and p_f_latino !=1 ORDER BY p_f_latino DESC;"

		if sex == 'Female' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_f_native FROM probabilities WHERE "+Age+" and p_f_native !=1 ORDER BY p_f_native DESC;"

		if sex == 'Female' and race == 'White':
			sql_query = "SELECT name,p_f_white FROM probabilities WHERE "+Age+" and p_f_white !=1 ORDER BY p_f_white DESC;"

		if sex == 'Male' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_m_asian !=1 ORDER BY p_m_asian DESC;"

		if sex == 'Male' and race == 'Black/African American':
			sql_query = "SELECT name,p_m_black FROM probabilities WHERE "+Age+" and p_m_black !=1 ORDER BY p_m_black DESC;"

		if sex == 'Male' and race == 'Hispanic':
			sql_query = "SELECT name,p_m_latino FROM probabilities WHERE "+Age+" and p_m_latino !=1 ORDER BY p_m_latino DESC;"

		if sex == 'Male' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_m_native FROM probabilities WHERE "+Age+" and p_m_native !=1 ORDER BY p_m_native DESC;"

		if sex == 'Male' and race == 'White':
			sql_query = "SELECT name,p_m_white FROM probabilities WHERE "+Age+" and p_m_white !=1 ORDER BY p_m_white DESC;"
	if age == '15-24':
		Age = "Age='4a'"
		if sex == 'Female' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_f_asian !=1 ORDER BY p_f_asian DESC;"

		if sex == 'Female' and race == 'Black/African American':
			sql_query = "SELECT name,p_f_black FROM probabilities WHERE "+Age+" and p_f_black !=1 ORDER BY p_f_black DESC;"

		if sex == 'Female' and race == 'Hispanic':
			sql_query = "SELECT name,p_f_latino FROM probabilities WHERE "+Age+" and p_f_latino !=1 ORDER BY p_f_latino DESC;"

		if sex == 'Female' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_f_native FROM probabilities WHERE "+Age+" and p_f_native !=1 ORDER BY p_f_native DESC;"

		if sex == 'Female' and race == 'White':
			sql_query = "SELECT name,p_f_white FROM probabilities WHERE "+Age+" and p_f_white !=1 ORDER BY p_f_white DESC;"

		if sex == 'Male' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_m_asian !=1 ORDER BY p_m_asian DESC;"

		if sex == 'Male' and race == 'Black/African American':
			sql_query = "SELECT name,p_m_black FROM probabilities WHERE "+Age+" and p_m_black !=1 ORDER BY p_m_black DESC;"

		if sex == 'Male' and race == 'Hispanic':
			sql_query = "SELECT name,p_m_latino FROM probabilities WHERE "+Age+" and p_m_latino !=1 ORDER BY p_m_latino DESC;"

		if sex == 'Male' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_m_native FROM probabilities WHERE "+Age+" and p_m_native !=1 ORDER BY p_m_native DESC;"

		if sex == 'Male' and race == 'White':
			sql_query = "SELECT name,p_m_white FROM probabilities WHERE "+Age+" and p_m_white !=1 ORDER BY p_m_white DESC;"
	if age == '25-34':
		Age = "Age='5a'"
		if sex == 'Female' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_f_asian !=1 ORDER BY p_f_asian DESC;"

		if sex == 'Female' and race == 'Black/African American':
			sql_query = "SELECT name,p_f_black FROM probabilities WHERE "+Age+" and p_f_black !=1 ORDER BY p_f_black DESC;"

		if sex == 'Female' and race == 'Hispanic':
			sql_query = "SELECT name,p_f_latino FROM probabilities WHERE "+Age+" and p_f_latino !=1 ORDER BY p_f_latino DESC;"

		if sex == 'Female' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_f_native FROM probabilities WHERE "+Age+" and p_f_native !=1 ORDER BY p_f_native DESC;"

		if sex == 'Female' and race == 'White':
			sql_query = "SELECT name,p_f_white FROM probabilities WHERE "+Age+" and p_f_white !=1 ORDER BY p_f_white DESC;"

		if sex == 'Male' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_m_asian !=1 ORDER BY p_m_asian DESC;"

		if sex == 'Male' and race == 'Black/African American':
			sql_query = "SELECT name,p_m_black FROM probabilities WHERE "+Age+" and p_m_black !=1 ORDER BY p_m_black DESC;"

		if sex == 'Male' and race == 'Hispanic':
			sql_query = "SELECT name,p_m_latino FROM probabilities WHERE "+Age+" and p_m_latino !=1 ORDER BY p_m_latino DESC;"

		if sex == 'Male' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_m_native FROM probabilities WHERE "+Age+" and p_m_native !=1 ORDER BY p_m_native DESC;"

		if sex == 'Male' and race == 'White':
			sql_query = "SELECT name,p_m_white FROM probabilities WHERE "+Age+" and p_m_white !=1 ORDER BY p_m_white DESC;"
	if age == '35-44':
		Age = "Age='6a'"
		if sex == 'Female' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_f_asian !=1 ORDER BY p_f_asian DESC;"

		if sex == 'Female' and race == 'Black/African American':
			sql_query = "SELECT name,p_f_black FROM probabilities WHERE "+Age+" and p_f_black !=1 ORDER BY p_f_black DESC;"

		if sex == 'Female' and race == 'Hispanic':
			sql_query = "SELECT name,p_f_latino FROM probabilities WHERE "+Age+" and p_f_latino !=1 ORDER BY p_f_latino DESC;"

		if sex == 'Female' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_f_native FROM probabilities WHERE "+Age+" and p_f_native !=1 ORDER BY p_f_native DESC;"

		if sex == 'Female' and race == 'White':
			sql_query = "SELECT name,p_f_white FROM probabilities WHERE "+Age+" and p_f_white !=1 ORDER BY p_f_white DESC;"

		if sex == 'Male' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_m_asian !=1 ORDER BY p_m_asian DESC;"

		if sex == 'Male' and race == 'Black/African American':
			sql_query = "SELECT name,p_m_black FROM probabilities WHERE "+Age+" and p_m_black !=1 ORDER BY p_m_black DESC;"

		if sex == 'Male' and race == 'Hispanic':
			sql_query = "SELECT name,p_m_latino FROM probabilities WHERE "+Age+" and p_m_latino !=1 ORDER BY p_m_latino DESC;"

		if sex == 'Male' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_m_native FROM probabilities WHERE "+Age+" and p_m_native !=1 ORDER BY p_m_native DESC;"

		if sex == 'Male' and race == 'White':
			sql_query = "SELECT name,p_m_white FROM probabilities WHERE "+Age+" and p_m_white !=1 ORDER BY p_m_white DESC;"
	if age == '45-54':
		Age = "Age='7a'"
		if sex == 'Female' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_f_asian !=1 ORDER BY p_f_asian DESC;"

		if sex == 'Female' and race == 'Black/African American':
			sql_query = "SELECT name,p_f_black FROM probabilities WHERE "+Age+" and p_f_black !=1 ORDER BY p_f_black DESC;"

		if sex == 'Female' and race == 'Hispanic':
			sql_query = "SELECT name,p_f_latino FROM probabilities WHERE "+Age+" and p_f_latino !=1 ORDER BY p_f_latino DESC;"

		if sex == 'Female' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_f_native FROM probabilities WHERE "+Age+" and p_f_native !=1 ORDER BY p_f_native DESC;"

		if sex == 'Female' and race == 'White':
			sql_query = "SELECT name,p_f_white FROM probabilities WHERE "+Age+" and p_f_white !=1 ORDER BY p_f_white DESC;"

		if sex == 'Male' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_m_asian !=1 ORDER BY p_m_asian DESC;"

		if sex == 'Male' and race == 'Black/African American':
			sql_query = "SELECT name,p_m_black FROM probabilities WHERE "+Age+" and p_m_black !=1 ORDER BY p_m_black DESC;"

		if sex == 'Male' and race == 'Hispanic':
			sql_query = "SELECT name,p_m_latino FROM probabilities WHERE "+Age+" and p_m_latino !=1 ORDER BY p_m_latino DESC;"

		if sex == 'Male' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_m_native FROM probabilities WHERE "+Age+" and p_m_native !=1 ORDER BY p_m_native DESC;"

		if sex == 'Male' and race == 'White':
			sql_query = "SELECT name,p_m_white FROM probabilities WHERE "+Age+" and p_m_white !=1 ORDER BY p_m_white DESC;"
	if age == '55-64':
		Age = "Age='8a'"
		if sex == 'Female' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_f_asian !=1 ORDER BY p_f_asian DESC;"

		if sex == 'Female' and race == 'Black/African American':
			sql_query = "SELECT name,p_f_black FROM probabilities WHERE "+Age+" and p_f_black !=1 ORDER BY p_f_black DESC;"

		if sex == 'Female' and race == 'Hispanic':
			sql_query = "SELECT name,p_f_latino FROM probabilities WHERE "+Age+" and p_f_latino !=1 ORDER BY p_f_latino DESC;"

		if sex == 'Female' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_f_native FROM probabilities WHERE "+Age+" and p_f_native !=1 ORDER BY p_f_native DESC;"

		if sex == 'Female' and race == 'White':
			sql_query = "SELECT name,p_f_white FROM probabilities WHERE "+Age+" and p_f_white !=1 ORDER BY p_f_white DESC;"

		if sex == 'Male' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_m_asian !=1 ORDER BY p_m_asian DESC;"

		if sex == 'Male' and race == 'Black/African American':
			sql_query = "SELECT name,p_m_black FROM probabilities WHERE "+Age+" and p_m_black !=1 ORDER BY p_m_black DESC;"

		if sex == 'Male' and race == 'Hispanic':
			sql_query = "SELECT name,p_m_latino FROM probabilities WHERE "+Age+" and p_m_latino !=1 ORDER BY p_m_latino DESC;"

		if sex == 'Male' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_m_native FROM probabilities WHERE "+Age+" and p_m_native !=1 ORDER BY p_m_native DESC;"

		if sex == 'Male' and race == 'White':
			sql_query = "SELECT name,p_m_white FROM probabilities WHERE "+Age+" and p_m_white !=1 ORDER BY p_m_white DESC;"

	if age == '65-74':
		Age = "Age='9a'"
		if sex == 'Female' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_f_asian !=1 ORDER BY p_f_asian DESC;"

		if sex == 'Female' and race == 'Black/African American':
			sql_query = "SELECT name,p_f_black FROM probabilities WHERE "+Age+" and p_f_black !=1 ORDER BY p_f_black DESC;"

		if sex == 'Female' and race == 'Hispanic':
			sql_query = "SELECT name,p_f_latino FROM probabilities WHERE "+Age+" and p_f_latino !=1 ORDER BY p_f_latino DESC;"

		if sex == 'Female' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_f_native FROM probabilities WHERE "+Age+" and p_f_native !=1 ORDER BY p_f_native DESC;"

		if sex == 'Female' and race == 'White':
			sql_query = "SELECT name,p_f_white FROM probabilities WHERE "+Age+" and p_f_white !=1 ORDER BY p_f_white DESC;"

		if sex == 'Male' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_m_asian !=1 ORDER BY p_m_asian DESC;"

		if sex == 'Male' and race == 'Black/African American':
			sql_query = "SELECT name,p_m_black FROM probabilities WHERE "+Age+" and p_m_black !=1 ORDER BY p_m_black DESC;"

		if sex == 'Male' and race == 'Hispanic':
			sql_query = "SELECT name,p_m_latino FROM probabilities WHERE "+Age+" and p_m_latino !=1 ORDER BY p_m_latino DESC;"

		if sex == 'Male' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_m_native FROM probabilities WHERE "+Age+" and p_m_native !=1 ORDER BY p_m_native DESC;"

		if sex == 'Male' and race == 'White':
			sql_query = "SELECT name,p_m_white FROM probabilities WHERE "+Age+" and p_m_white !=1 ORDER BY p_m_white DESC;"
	if age == '75-84':
		Age = "Age='10a'"
		if sex == 'Female' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_f_asian !=1 ORDER BY p_f_asian DESC;"

		if sex == 'Female' and race == 'Black/African American':
			sql_query = "SELECT name,p_f_black FROM probabilities WHERE "+Age+" and p_f_black !=1 ORDER BY p_f_black DESC;"

		if sex == 'Female' and race == 'Hispanic':
			sql_query = "SELECT name,p_f_latino FROM probabilities WHERE "+Age+" and p_f_latino !=1 ORDER BY p_f_latino DESC;"

		if sex == 'Female' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_f_native FROM probabilities WHERE "+Age+" and p_f_native !=1 ORDER BY p_f_native DESC;"

		if sex == 'Female' and race == 'White':
			sql_query = "SELECT name,p_f_white FROM probabilities WHERE "+Age+" and p_f_white !=1 ORDER BY p_f_white DESC;"

		if sex == 'Male' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_m_asian !=1 ORDER BY p_m_asian DESC;"

		if sex == 'Male' and race == 'Black/African American':
			sql_query = "SELECT name,p_m_black FROM probabilities WHERE "+Age+" and p_m_black !=1 ORDER BY p_m_black DESC;"

		if sex == 'Male' and race == 'Hispanic':
			sql_query = "SELECT name,p_m_latino FROM probabilities WHERE "+Age+" and p_m_latino !=1 ORDER BY p_m_latino DESC;"

		if sex == 'Male' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_m_native FROM probabilities WHERE "+Age+" and p_m_native !=1 ORDER BY p_m_native DESC;"

		if sex == 'Male' and race == 'White':
			sql_query = "SELECT name,p_m_white FROM probabilities WHERE "+Age+" and p_m_white !=1 ORDER BY p_m_white DESC;"

	if age == '85+':
		Age = "Age='11a'"
		if sex == 'Female' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_f_asian !=1 ORDER BY p_f_asian DESC;"

		if sex == 'Female' and race == 'Black/African American':
			sql_query = "SELECT name,p_f_black FROM probabilities WHERE "+Age+" and p_f_black !=1 ORDER BY p_f_black DESC;"

		if sex == 'Female' and race == 'Hispanic':
			sql_query = "SELECT name,p_f_latino FROM probabilities WHERE "+Age+" and p_f_latino !=1 ORDER BY p_f_latino DESC;"

		if sex == 'Female' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_f_native FROM probabilities WHERE "+Age+" and p_f_native !=1 ORDER BY p_f_native DESC;"

		if sex == 'Female' and race == 'White':
			sql_query = "SELECT name,p_f_white FROM probabilities WHERE "+Age+" and p_f_white !=1 ORDER BY p_f_white DESC;"

		if sex == 'Male' and race == 'Asian/Pacific Islander':
			sql_query = "SELECT name,p_f_asian FROM probabilities WHERE "+Age+" and p_m_asian !=1 ORDER BY p_m_asian DESC;"

		if sex == 'Male' and race == 'Black/African American':
			sql_query = "SELECT name,p_m_black FROM probabilities WHERE "+Age+" and p_m_black !=1 ORDER BY p_m_black DESC;"

		if sex == 'Male' and race == 'Hispanic':
			sql_query = "SELECT name,p_m_latino FROM probabilities WHERE "+Age+" and p_m_latino !=1 ORDER BY p_m_latino DESC;"

		if sex == 'Male' and race == 'Native American/Alaskan':
			sql_query = "SELECT name,p_m_native FROM probabilities WHERE "+Age+" and p_m_native !=1 ORDER BY p_m_native DESC;"

		if sex == 'Male' and race == 'White':
			sql_query = "SELECT name,p_m_white FROM probabilities WHERE "+Age+" and p_m_white !=1 ORDER BY p_m_white DESC;"

	cursor.execute(sql_query)
	rows = cursor.fetchall()
	new_list=[''.join(list(rows[0][0])),''.join(list(rows[1][0])),''.join(list(rows[2][0])),''.join(list(rows[3][0])),''.join(list(rows[4][0]))]
	pvals=[rows[0][1],rows[1][1],rows[2][1],rows[3][1],rows[4][1]]
	padded_list=[]

	#need to pad the strings so that they are equal length
	max_len=len(max(new_list,key=len))
	for i in range(len(new_list)):
		cur_len=len(new_list[i])
		empty_string=" "*cur_len
		padded_string=new_list[i]+empty_string
		padded_list.append(padded_string)

	#using pattern look up google for top diseases

	engine=Google(license=key,throttle=0)

	empty_link_disease=[]
	empty_text_disease=[]

	empty_link_treatment=[]
	empty_text_treatment=[]


	for index in new_list:
		#search wikipedia first for snippet about the disease, if it doesn't exist change to google
		about=Wikipedia().search(index)
		if not about:
			about=engine.search(index)
			empty_link_disease.append(about[0].url)
			empty_text_disease.append(plaintext(about[0].text))
		elif about:
			about_url=engine.search(index+' Wikipedia')
			empty_link_disease.append(about_url[0].url)
			empty_text_disease.append(plaintext(about.sections[0].content[0:1000])+'...')

		treatment=engine.search(index+' treatment site:www.healthtap.com')
		empty_link_treatment.append(treatment[0].url)
		empty_text_treatment.append(plaintext(treatment[0].text))
		
	disease_links=[''.join(list(empty_link_disease[0])),''.join(list(empty_link_disease[1])),''.join(list(empty_link_disease[2])),''.join(list(empty_link_disease[3])),''.join(list(empty_link_disease[4]))]
	treatment_links=[''.join(list(empty_link_treatment[0])),''.join(list(empty_link_treatment[1])),''.join(list(empty_link_treatment[2])),''.join(list(empty_link_treatment[3])),''.join(list(empty_link_treatment[4]))]
	#string_links=[str(list(empty_link[0])),str(list(empty_link[1])),str(list(empty_link[2])),str(list(empty_link[3])),str(list(empty_link[4]))]
	#print string_links
	return render_template('results_feb1.html',disease_name=padded_list,pvalues=pvals, d_links=disease_links, disease_snippets=empty_text_disease, t_links=treatment_links, treatment_snippets=empty_text_treatment)

@app.route("/slides")
def slides():
    return render_template('Slides.html') 

if __name__ == '__main__':
    print "Starting debugging server."
    app.debug=True
    app.run(host='0.0.0.0',port=80)
