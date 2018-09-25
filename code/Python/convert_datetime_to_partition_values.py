from datetime import datetime

def modify_line(next_line):

    date_str = datetime.strptime(next_line["trans_date"], next_line["date_format"])
    yyyymm = "%s%02d" % (date_str.year, date_str.month)
 
 
    new_line = {
        "trans_id": next_line["trans_id"],
        "trans_amt": next_line["trans_amt"],
        "trans_date": next_line["trans_date"],
        "dt": yyyymm
    }

    return new_line


dic = {
    "trans_id": 1,
    "trans_amt": 30000,
    "trans_date": "2018-05-08",
    "date_format":"%Y-%m-%d"
}

print modify_line(dic)

dic = {
    "trans_id": 1,
    "trans_amt": 30000,
    "trans_date": "2018-06-06 07:00:00432",
    "date_format":"%Y-%m-%d %H:%M:%S%f",
}

print modify_line(dic)

