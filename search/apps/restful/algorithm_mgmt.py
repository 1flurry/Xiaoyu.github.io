from flask import *
from service import data_show as ads
import json
from apps.restful import api

@api.route('/aievisualize/rest/threatevent/threat_event_list_data')
def get_all_output_data():
    try: 
        current_page = int(request.args.get('current_page')) if request.args.get('current_page') else 1
        page_size = int(request.args.get('pageSize')) if request.args.get('pageSize') else 20
    except:
        items = []
        total = 0
        resultCode = '5'
    else:
        items, total, resultCode = ads.get_all_result(current_page,page_size)
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
    return json_data

@api.route('/aievisualize/rest/threatevent/threat_event_detect_list_data')
def get_detect_output_data():
    try:
        threat_type = str(request.args.get('ThreatType')).encode('utf-8') if request. args.get('ThreatType') else '40000'.encode("utf-8")
        current_page = int(request.args.get('current_page')) if request.args.get('current_page') else 1
        page_size = int(request.args.get('pageSize')) if request.args.get('pageSize') else 20
        beginTime = int(request.args.get('beginTime')) if request.args.get('beginTime') else 0
        endTime = int(request.args.get('endTime')) if request.args.get('endTime') else 1538212486
    except:
        items = []
        total = 0
        resultCode = '5'
    else:
        items, total, resultCode = ads.get_detect_result(threat_type,current_page,page_size,beginTime,endTime)
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
    return json_data

@api.route("/aievisualize/rest/threatevent/threat_event_agg_data")
def get_algorithms_num():
    errDesc = "OK"
    resultCode = "0"
    aggField = str(request.args.get("aggField"))
    try:
        if aggField == "ThreatType":
            agg_terms = ads.get_algorithms_type_num()
        elif aggField == "ThreatLevel":
            agg_terms = ads.get_algorithms_level_num()
        else:
            resultCode = "1"
            errDesc = "Fail"
            agg_terms = []
    except Exception:
        resultCode = "4"
        errDesc = "Fail"
        agg_terms = []
    data = [
        {
            "key" : "",
            "doc_count" : len(agg_terms),
            "agg_terms" : agg_terms,
        }
    ]
    rstJson = {
        "resultCode" : resultCode,
        "errDesc" : errDesc,
        "totalCount" : len(data),
        "data" : data
    }
    json_data = json.dumps(rstJson)
    return json_data
