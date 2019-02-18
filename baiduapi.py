import urllib, urllib3, sys
import ssl
import json
import config

AppID = config.AppID
Secret_Key = config.Secret_Key
API_Key = config.API_Key

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host1 = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_Key + '&client_secret=' + Secret_Key + ''
a = urllib.request.urlopen(host1)
b = json.loads(a.read().decode())
access_token = b.get("access_token")
host = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/depparser?access_token=' + access_token
host3 = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/ecnet?access_token=' + access_token
body = {
    "text": "规模扩大，业务量增加，相应资产和负债也增加。",
    'mode' : 0
}
body = json.dumps(body).encode('GBK')
req = urllib.request.Request(url=host, data=body)
req.add_header('Content-Type', 'application/json')
res = urllib.request.urlopen(req)
ccc = str(res.read(), encoding='gbk')
if (ccc):
    print(ccc)

import pandas
# pandas.merge()
from stanfordcorenlp import StanfordCoreNLP 
nlp = StanfordCoreNLP(r'./stanford-corenlp-full-2016-10-31/', lang='zh')

sentence = "规模扩大，业务量增加，相应资产和负债也增加。"
print(nlp.parse(sentence))
print(nlp.dependency_parse(sentence))