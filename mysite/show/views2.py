from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import jaydebeapi, jpype

classname = 'Altibase.jdbc.driver.AltibaseDriver'
classfile = '$ALTIBASE_HOME/lib/Altibase.jar'
dbuser = 'sys'
passwd = 'manager'

conn, cursor = None, None

try :
    conn = jaydebeapi.connect (classname,
                                'jdbc:Altibase://127.0.0.1:20300/mydb',
                                {'user': dbuser, 'password': passwd},
                                classfile)

    cursor = conn.cursor()
    # print ('%s' %conn)

    sql = "SELECT TEST_RESULT_1 FROM STANDARD_TEST_RESULT WHERE PER_TEST_ID = 85 AND THREAD = 16"
    cursor.execute(sql)

    data = cursor.fetchall()

    for x in data:
        for y in x:
            print(y)

    cursor.close()
    conn.close()

except Exception as msg:
      print ('Error Message : %s' %msg)


def index(request):
	template = loader.get_template('show/index.html')
#	context = {
#		'list_data': data,
#	}

	return HttpResponse(data)
#	return HttpResponse(template.render(context, request))
