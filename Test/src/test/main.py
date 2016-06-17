#coding:utf-8
import urllib, urllib2, json, re
from pyExcelerator import *
# typ: 0:get  1:post
def httpconn(url, para, typ):
    data = urllib.urlencode(para)
    if typ == 0:
        url = url + '?' + data
        req = urllib2.Request(url)
    else:
        req = urllib2.Request(url,data)
    try:
        con = urllib2.urlopen(req,timeout=15)
    except urllib2.HTTPError as e:    
        print "The server couldn't fulfill the request"
        print "Error code:",e.reason
        return None
    except urllib2.URLError as e:
        print "Failed to reach the server"
        print "The reason:",e.reason
        return None
    except Exception as e:
        print e
        return None
    ret = json.load(con)
    return ret

title = [unicode('手机号',"utf-8"),unicode('注册时间',"utf-8"),unicode('首投时间',"utf-8"),
    unicode('首投金额',"utf-8"),unicode('总投资金额',"utf-8"),unicode('是否实名认证',"utf-8"),unicode('是否绑卡',"utf-8"),]
klist = ['id_mobile','time','first_invest_time','first_invest_amount','total_amount',
           'is_realname','is_tiecard']
def get_data():
    read = {}
    with open('conf.txt') as f:
        for line in f:
            pat = re.compile('\s')
            line = pat.sub('', line)
            if ':' not in line:
                continue
            s = line.split(':',1)
            read[s[0]] = s[1]
    url_at = read.get('url1')
    param = {'username':read.get('username'),
             'password':read.get('password'),
    }
    json_ret = httpconn(url_at, param, 1)
    token = json_ret.get('data').get('token')
    url_at2 = read.get('url2')
    param2 = {'token':token,
              'startTime':read.get('startTime'),
              'endTime':read.get('endTime'),
              'type':'yqs',
    }
    json_ret2 = httpconn(url_at2, param2, 1)
    list = json_ret2.get('cpsList')
    print json_ret2
    result = [title,]
    for dic in list:
        item = []
        for key in klist:
            t = dic.get(key)
            if t!='NULL' and 'amount' in key:
                t=float(t)/100
            item.append(t)
        result.append(item)
        
    return result

w = Workbook()     #创建一个工作簿
ws = w.add_sheet('hello')     #创建一个工作表
ret = get_data()
row = len(ret)
for i in range(row):
    lis = ret[i]
    col = len(lis)
    for j in range(col):
        ws.write(i,j,lis[j])
w.save('mini.xls')     #保存