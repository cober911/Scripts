import requests
import xmltodict
from datetime import datetime


"""
curl -H 'Accept: application/xml' -H 'Content-Type: application/xml' -u 4db09df5a62a8a32a9522fcac02d3c6f:06540b851b466ccf84558573aff11b65 -k -d '<request>...</request>' https://api.planfix.ru/xml/
"""

URL = "https://apiru.planfix.ru/xml"
USR_Tocken = "50e095fc617573f80f1baab10290d48f"
PSR_Tocken = "7bc564d8f4835ca9ca52523f6103ec47"
headr = {"Accept": 'application/xml', "Content-Type": 'application/xml'}

data_task = '''
<request method="task.get">
    <account>finfort</account>
    <task>
      <id>18186298</id>
    </task>    
</request>
'''

data_user = '''
<request method="user.get">
    <account>finfort</account>
    <user>
      <id>5307252</id>
    </user>    
</request>
'''
data_tasks = '''
<request method="task.getMulti">
    <account>finfort</account>
    <tasks>
<id>17079232</id><id>17079234</id><id>17079236</id><id>17146948</id><id>17147412</id><id>17163370</id><id>17163372</id><id>17163398</id><id>17207728</id><id>17207766</id><id>17237556</id><id>17237558</id><id>17405346</id><id>17405450</id><id>17496524</id><id>17500200</id><id>17540540</id><id>17560242</id><id>17560248</id><id>17579228</id><id>17922504</id><id>17922506</id><id>17922508</id><id>17982000</id><id>17994602</id><id>18011860</id><id>18011894</id><id>18014724</id><id>18045768</id><id>18045786</id><id>18045788</id><id>18045790</id><id>18045852</id><id>18045854</id><id>18045988</id><id>18046006</id><id>18046010</id><id>18046300</id><id>18046314</id><id>18046384</id><id>18046398</id><id>18046404</id><id>18046410</id><id>18046412</id><id>18046414</id><id>18046416</id><id>18046500</id><id>18046568</id><id>18046572</id><id>18046574</id><id>18046578</id><id>18046588</id><id>18046686</id><id>18046688</id><id>18046712</id><id>18046726</id><id>18046728</id><id>18046734</id><id>18046736</id><id>18046738</id><id>18046742</id><id>18046744</id><id>18046746</id><id>18046748</id><id>18046750</id><id>18046814</id><id>18046826</id><id>18046828</id><id>18047024</id><id>18047026</id><id>18047030</id><id>18047034</id><id>18047038</id><id>18047042</id><id>18047084</id><id>18047188</id><id>18047190</id><id>18047244</id><id>18047246</id><id>18047248</id><id>18047250</id><id>18047252</id><id>18047254</id><id>18047256</id><id>18047258</id><id>18047286</id><id>18047368</id><id>18047412</id><id>18047414</id><id>18047550</id><id>18047552</id><id>18047596</id><id>18047598</id><id>18047600</id><id>18047672</id><id>18047714</id><id>18047716</id><id>18047728</id><id>18047730</id><id>18047810</id>
    </tasks>    
</request>
'''

data_users1 = '<request method="user.getList"><account>finfort' \
              + '</account><status>UNACTIVE</status><pageSize>100</pageSize><pageCurrent>1' \
              + '</pageCurrent></request>'

data_contact = '''
<request method="contact.get">
    <account>finfort</account>
    <contact>
      <general>2162</general>
    </contact>    
</request>
'''

data_contact1 = '<request method="contact.getList"><account>' + \
                '</account><pageCurrent>' + \
                '</pageCurrent><pageSize>100</pageSize><target>6532326</target></request>'

data_group = '''
<request method="userGroup.getList">
    <account>finfort</account>
    <pageSize>100</pageSize>  
</request>
'''

data_process = '''
<request method="taskStatus.getSetList">
    <account>finfort</account>
</request>
'''
data_status_in_process = '''
<request method="taskStatus.getListOfSet">
    <account>finfort</account>
    <taskStatusSet>
       <id>230580</id>
    </taskStatusSet>
</request>
'''
data_filter_list = '''
<request method="contact.getFilterList">
  <account>finfort</account>
</request>'''

data_users_update = '<request method="user.update"><account>finfort</account><user><id>5315338</id>' \
                    '<email>da3@yandex.ru</email></user></request>'

data_action = '<request method="action.get"><account>finfort</account><action><id>78287168</id></action></request>'

data_actions = '<request method="action.getListByPeriod"><account>finfort</account><fromDate>12-12-2018 00:00' \
               + '</fromDate><toDate>' + datetime.now().strftime('%d-%m-%Y %H:%M') + '</toDate><pageCurrent>1'\
               + '</pageCurrent><pageSize>100</pageSize><sort>asc</sort></request>'

def load_contacts_from_api():
    """Загрузка всех контактов Сотрудников (группа №6532326) из АПИ ПФ в файл contacts.xml"""
    users = []
    i = 1
    while True:
        answer = requests.post(
            URL,
            headers=headr,
            data='<request method="user.getList"><account>finfort</account><status>UNACTIVE</status><pageCurrent>' +
                 str(i) + '</pageCurrent><pageSize>100</pageSize></request>' ,
            auth=(USR_Tocken, PSR_Tocken))
        if answer.text.find('count="0"/></response>') > -1:
            break
        else:
            users += xmltodict.parse(answer.text)['response']['users']['user']
        i += 1
    return users


#simple_request = '''
#users = load_contacts_from_api()
#for user in users:
#    data_users4update = '<request method="user.update"><account>finfort</account><user><id>' + str(user['id']) \
#                        + '</id><email>' + str(user['email']).split('@')[0] + '_old@' \
#                        + str(user['email']).split('@')[1] + '</email></user></request>'
#    q=0
#    answer = requests.post(URL, headers=headr, data=data_users4update, auth=(USR_Tocken, PSR_Tocken))

#answer = requests.post(URL,
#                       headers=headr,
#                       data='<request method="handbook.getRecords"><account>finfort</account>'
#                            '<handbook><id>2</id></handbook><parentKey>39</parentKey></request>',
#                       auth=(USR_Tocken, PSR_Tocken))

answer = requests.post(URL,
                       headers=headr,
                       data='<request method="user.get"><account>finfort</account><user><general>534</general>'
                            '</user></request>',
                       auth=(USR_Tocken, PSR_Tocken))

mydict = xmltodict.parse(answer.text)
q=0
#'''

