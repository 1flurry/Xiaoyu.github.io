import pymysql
import math
import json
import configs as C
import time,datetime
#R = C.DATA_MYSQL
R = {'host': "localhost", 'user': "root", 'password': "123456", 'database': "AIE_Detect_Result"}

db = pymysql.connect(host=R['host'], user=R['user'], passwd=R['password'], db=R['database'],\
	charset = 'utf8',cursorclass = pymysql.cursors.DictCursor)

#获取威胁信息
def get_detect_result(type,current_page,page_size,beginTime,endTime):
    threat_type_dic = {
    "00000":"common",              #输出全部
    "10000":"abnormal_file",       #异常文件检测
    "20000":"bruteforce",          #暴力破解
    "30000":"cc_flow",             #CC通信
    "40000":"webshell",            #webshell
    "50000":"eca",                 #异常加密通信
    "60000":"dns_tunnel",          #DNS tunnel
    "70000":"dga" }                #DGA域名检测
    threat_type_change = {
    "abnormal_file" : "10000",       #异常文件检测
    "bruteforce" : "20000",           #暴力破解
    "cc_flow" : "30000",             #CC通信
    "webshell" : "40000",            #webshell
    "eca" : "50000",                 #异常加密通信
    "dns_tunnel" : "60000",          #DNS tunnel
    "dga" : "70000" }                #DGA域名检测
    threat_type = threat_type_dic[type.decode('utf-8')]
    cursor = db.cursor()
    beginTime = time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(beginTime))
    endTime = time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(endTime))
    try:
        cursor.execute("SELECT COUNT(id) as num from AIE_Detect_Result where threat_type = '%s' and time_start <= '%s' and time_start >= '%s'" % (threat_type,endTime,beginTime))
        data_num = cursor.fetchone()['num']#数据总数
    except:
        return [], 0, '4'
    try:
        total = int(math.ceil(data_num/page_size)) #总页数
        if total == 0: 
            return [], 0, '6'
        offset = (current_page-1)*page_size
    except:
        return [], 0, '1'
    try:
        cursor.execute("SELECT * from AIE_Detect_Result where threat_type = '%s' limit %d offset %d" % (threat_type,page_size,offset))
        data = cursor.fetchall()
    except:
        return [], 0, '4'
    try:
        items = []
        for el in data:
            el['threat_type'] = threat_type_change[str(el['threat_type'])]
            if el['time_start'] == None:
                el.update({"AttackType":el['threat_type'],
                           "AlarmLevel":el['threat_level'],
                           #"AttackSubType":"10001",
                           "AlarmTime":el['time_start'],
                           "SrcIP":el['sip'],
                           "DestIP":el['dip'],
                           "SrcPort":el['sport'],
                           "DestPort":el['dport']})
                el.pop("threat_type")
                el.pop("threat_level")
                el.pop("time_start")
                el.pop("sip")
                el.pop("dip")
                el.pop("sport")
                el.pop("dport")          
                items.append(el)
            else:
                el.update({"AttackType":el['threat_type'],
                           "AlarmLevel":el['threat_level'],
                           #"AttackSubType":"10001",
                           "AlarmTime":el['time_start'].strftime("%Y-%m-%d %H:%M:%S"),
                           "SrcIP":el['sip'],
                           "DestIP":el['dip'],
                           "SrcPort":el['sport'],
                           "DestPort":el['dport']})
                el.pop("threat_type")
                el.pop("threat_level")
                el.pop("time_start")
                el.pop("sip")
                el.pop("dip")
                el.pop("sport")
                el.pop("dport")          
                items.append(el)
    except:
        return [], 0, '1'
    return items, total, '0'

def get_all_result(current_page,page_size):
    threat_type_change = {
    "abnormal_file" : "10000",       #异常文件检测
    "bruteforce" : "20000",           #暴力破解
    "cc_flow" : "30000",             #CC通信
    "webshell" : "40000",            #webshell
    "eca" : "50000",                 #异常加密通信
    "dns_tunnel" : "60000",          #DNS tunnel
    "dga" : "70000" }                #DGA域名检测
    cursor = db.cursor()
    try:
        cursor.execute("SELECT COUNT(id) as num from AIE_Detect_Result")
        data_num = cursor.fetchone()['num']#数据总数
    except:
        return [], 0, '4'
    try:
        total = int(math.ceil(data_num/page_size)) #总页数
        print(total)
        if total == 0: 
            return [], 0, '6'
        offset = (current_page - 1)*page_size
    except:
        return [], 0, '1'
    try:
        cursor.execute("SELECT * from AIE_Detect_Result limit %d offset %d" % (page_size,offset))
        data = cursor.fetchall()
    except:
        return [], 0, '4'
    try:
        items = []
        for el in data:
            el['threat_type'] = threat_type_change[str(el['threat_type'])]
            #转换数据库字段
            if el['time_start'] == None:
                el.update({"AttackType":el['threat_type'],
                           "AlarmLevel":el['threat_level'],
                           #"AttackSubType":"10001",
                           "AlarmTime":el['time_start'],
                           "SrcIP":el['sip'],
                           "DestIP":el['dip'],
                           "SrcPort":el['sport'],
                           "DestPort":el['dport']})
                el.pop("threat_type")
                el.pop("threat_level")
                el.pop("time_start")
                el.pop("sip")
                el.pop("dip")
                el.pop("sport")
                el.pop("dport")          
                items.append(el)
            else:
                el.update({"AttackType":el['threat_type'],
                           "AlarmLevel":el['threat_level'],
                           #"AttackSubType":"10001",
                           "AlarmTime":el['time_start'].strftime("%Y-%m-%d %H:%M:%S"),
                           "SrcIP":el['sip'],
                           "DestIP":el['dip'],
                           "SrcPort":el['sport'],
                           "DestPort":el['dport']})
                el.pop("threat_type")
                el.pop("threat_level")
                el.pop("time_start")
                el.pop("sip")
                el.pop("dip")
                el.pop("sport")
                el.pop("dport")          
                items.append(el)
    except:
        return [], 0, '1'
    return items, total, '0'

def get_algorithms_type_num():
    cursor = db.cursor()
    threat_type_dic = {
    "abnormal_file" : "10000",       #异常文件检测
    "brutefoce" : "20000",           #暴力破解
    "cc_flow" : "30000",             #CC通信
    "webshell" : "40000",            #webshell
    "eca" : "50000",                 #异常加密通信
    "dns_tunnel" : "60000",          #DNS tunnel
    "dga" : "70000" }                #DGA域名检测
    threat_type_num = []
    for threat_type in threat_type_dic:
        sql = "SELECT COUNT(id) FROM AIE_Detect_Result WHERE threat_type = '%s'" %(threat_type)
        cursor.execute(sql)
        num = cursor.fetchone()
        num_dic = {"key" : threat_type_dic[threat_type], "doc_count" : num["COUNT(id)"]}
        threat_type_num.append(num_dic)
    return threat_type_num

def get_algorithms_level_num():
    cursor = db.cursor()
    threat_level_dic = {
    1 : "1",            #很低
    2 : "2",            #低
    3 : "3",            #中
    4 : "4",            #高
    5 : "5"}            #很高
    threat_level_num = []
    for threat_level in threat_level_dic:
        sql = "SELECT COUNT(id) FROM AIE_Detect_Result WHERE threat_level = '%d'" %(threat_level)
        cursor.execute(sql)
        num = cursor.fetchone()
        num_dic = {"key" : threat_level_dic[threat_level], "doc_count" : num["COUNT(id)"]}
        threat_level_num.append(num_dic)
    return threat_level_num

if __name__ == '__main__':
    try:
        threat_type = str("10000").encode("utf-8")
        current_page = int("1")
        page_size = int("20")
    except:
        items = []
        total = 0
        resultCode = '5'
    else:
        #items, total, resultCode = get_all_result(current_page,page_size)
        items, total, resultCode= get_detect_result(threat_type,current_page,page_size)
    
    rstJson = {
    "resultCode":resultCode,
    "errDesc":"",
    "totalCount":total,
	"data":items
	}
    try:
        json_data = json.dumps(rstJson)
    except:
        items = []
        total = 0
        resultCode = '5'
        rstJson = {
        "resultCode":resultCode,
        "errDesc":"",
        "totalCount":total,
        "data":items
        }
        json_data = json.dumps(rstJson)
    #return json_data
    print(json_data)


