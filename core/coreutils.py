# -*- coding: utf-8 -*-

from db_interface import MysqlInstance
import re


NAME_REGEX = re.compile(u'^[\u4E00-\u9FA5]{2,6}(?:(·|•)[\u4E00-\u9FA5]{2,6})*$')
PHONE_REGEX = re.compile('^[1-9]\d{10}$')
IDNO_REGEX = re.compile('^(^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$)|(^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])((\d{4})|\d{3}[Xx])$)$')
MAIL_REGEX = re.compile(u'^\w+[-+.\w]*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')
BIRTH_DAY  = re.compile(r'\d{4}-\d{1,2}-\d{1,2}')
SEX  = re.compile('[FMfm]')  

DATE_REGEX = re.compile(
    r'(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})'
    r'(?: (?P<hour>\d{1,2}):(?P<minute>\d{1,2}):(?P<second>\d{1,2})'
    r'(?:\.(?P<microsecond>\d{1,6}))?)?')
      
#########################################################################
"""
函数返回的是元组类型，可以一次将请求参数获取并赋值，如下所示：
self.name,self.age = get_args_tuple(self,'name','age')
request为tornado的RequestHandler类
"""        
def get_args_tuple(request,*args):
    _=[]
    for i in range(len(args)):
        _.append(request.get_argument(args[i], '').strip()) 
    return tuple(_)


def check_refer(request):
    referer = request.headers.get('Referer', '')
    if not referer:
        return False
    if referer.find(request.uri) != -1: 
        return False
    return True


##########################################################################
def get_db_conn(idno,phone):
    if idno is None:
            raise ValueError('The "idno" parameter must not be empty')
    if phone is None:
            raise ValueError('The "phone" parameter must not be empty')
    return MysqlInstance.instance().get_db(idno, phone)


############################################################################
def check_name(name):
    try:
        name = name.decode('utf8')
    except:
        return False
    if NAME_REGEX.match(name) == None:
        return False
    return True


def check_phone(phone):
    if PHONE_REGEX.match(phone) == None:
        return False
    return True

def check_idno(idno):
    if IDNO_REGEX.match(idno) == None:
        return False
    return True

def check_birthday(birthday):
    if BIRTH_DAY.match(birthday) == None:
        return False
    return True


def check_sex(sex):
    if SEX.match(sex) == None:
        return False
    return True
        
############################################################################


def insert_by_dict(torndbConn, tablename, rowdict, replace=False):
    cursor = torndbConn._cursor()
    cursor.execute("describe %s" % tablename)
    allowed_keys = set(row[0] for row in cursor.fetchall())
    keys = allowed_keys.intersection(rowdict)

    if len(rowdict) > len(keys):
        unknown_keys = set(rowdict) - allowed_keys

    columns = ", ".join(keys)
    values_template = ", ".join(["%s"] * len(keys))

    if replace:
        sql = "REPLACE INTO %s (%s) VALUES (%s)" % (
            tablename, columns, values_template)
    else:
        sql = "INSERT INTO %s (%s) VALUES (%s)" % (
            tablename, columns, values_template)

    values = tuple(rowdict[key] for key in keys)
    try:
        cursor.execute(sql, values)
        
        return cursor.lastrowid
    finally:
        cursor.close()
        

def get_seo(keywords,title,description):
    seo = {'keywords': keywords,'title': title,'description': description}
    return seo