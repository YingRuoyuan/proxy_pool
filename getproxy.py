# -*- coding=utf-8 -*-
import urllib2, time, datetime
from lxml import etree
import sqlite3, random, sys

class domestic():

    def __init__(self):
        '''爬取国内ip代理'''
        self.GFW = "yes"
        userAgent=[
            "Mozilla/5.0 (Windows NT 5.1; rv:37.0) Gecko/20100101 Firefox/37.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
            "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"]
        self.user_agent = random.choice(userAgent)
        self.header = {"User-Agent": self.user_agent}
        self.now = time.strftime("%Y-%m-%d")

    def getXici(self, num=1):
        for i in range(1, num+1):
            xc_url = "http://www.xicidaili.com/nn/" + str(i)
            self.source = "http://www.xicidaili.com"
            req = urllib2.Request(xc_url, headers=self.header)
            Max_Num=6
            for i in range(Max_Num):
                try:
                    resp = urllib2.urlopen(req, timeout=10)
                    break
                except:
                    if i < Max_Num-1:
                        continue
                    else:
                        print 'URLError: <urlopen error timed out> All times is failed.'
                        sys.exit(1)
            content = resp.read()
            et = etree.HTML(content)
            result_even = et.xpath('//tr[@class=""]')
            result_odd = et.xpath('//tr[@class="odd"]')
            for i in result_even:
                t1 = i.xpath("./td/text()")[:2]
                print "IP:%s\tPort:%s" % (t1[0], t1[1])
                if datebase.isAlive(self.GFW,t1[0], t1[1]):
                    datebase.insert_gndb(self.now, self.source, t1[0], t1[1])
            for i in result_odd:
                t2 = i.xpath("./td/text()")[:2]
                print "IP:%s\tPort:%s" % (t2[0], t2[1])
                if datebase.isAlive(self.GFW, t2[0], t2[1]):
                    datebase.insert_gndb(self.now, self.source, t2[0], t2[1])

    def getKuai(self, num=1):
        for i in range(1, num+1):
            k_url = "http://www.kuaidaili.com/free/inha/" + str(i)
            self.source = "http://www.kuaidaili.com"
            req = urllib2.Request(k_url, headers=self.header)
            Max_Num=6
            for i in range(Max_Num):
                try:
                    resp = urllib2.urlopen(req, timeout=10)
                    break
                except:
                    if i < Max_Num-1:
                        continue
                    else:
                        print 'URLError: <urlopen error timed out> All times is failed.'
                        sys.exit(1)
            content = resp.read()
            et = etree.HTML(content)
            result = et.xpath('/html/body/div[@id="container"]/div/div[@id="list"]/table[@class="table table-bordered table-striped"]/tbody/tr')
            for i in result:
                t1 = i.xpath('./td[@data-title="IP"]/text()')[0]
                t2 = i.xpath('./td[@data-title="PORT"]/text()')[0]
                print "IP:%s\tPort:%s" % (t1, t2)
                if datebase.isAlive(self.GFW, t1, t2):
                    datebase.insert_gndb(self.now, self.source, t1, t2)

class overseas():

    def __init__(self):
        '''爬取国外ip代理'''
        self.GFW = "no"
        userAgent=[
            "Mozilla/5.0 (Windows NT 5.1; rv:37.0) Gecko/20100101 Firefox/37.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
            "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"]
        self.user_agent = random.choice(userAgent)
        self.header = {"User-Agent": self.user_agent}
        self.now = time.strftime("%Y-%m-%d")

    def getXici(self, num):
        for i in range(1, num+1):
            xc_url = "http://www.xicidaili.com/wn/" + str(i)
            self.source = "http://www.xicidaili.com"
            req = urllib2.Request(xc_url, headers=self.header)
            Max_Num=6
            for i in range(Max_Num):
                try:
                    resp = urllib2.urlopen(req, timeout=10)
                    break
                except:
                    if i < Max_Num-1:
                        continue
                    else:
                        print 'URLError: <urlopen error timed out> All times is failed.'
                        sys.exit(1)
            content = resp.read()
            et = etree.HTML(content)
            result_even = et.xpath('//tr[@class=""]')
            result_odd = et.xpath('//tr[@class="odd"]')
            for i in result_even:
                t1 = i.xpath("./td/text()")[:2]
                print "IP:%s\tPort:%s" % (t1[0], t1[1])
                if datebase.isAlive(self.GFW,t1[0], t1[1]):
                    datebase.insert_gwdb(self.now, self.source, t1[0], t1[1])
            for i in result_odd:
                t2 = i.xpath("./td/text()")[:2]
                print "IP:%s\tPort:%s" % (t2[0], t2[1])
                if datebase.isAlive(self.GFW, t2[0], t2[1]):
                    datebase.insert_gwdb(self.now, self.source, t2[0], t2[1])

    def getKuai(self, num=1):
        for i in range(1, num+1):
            k_url = "http://www.kuaidaili.com/free/outha/" + str(i)
            self.source = "http://www.kuaidaili.com"
            req = urllib2.Request(k_url, headers=self.header)
            Max_Num=6
            for i in range(Max_Num):
                try:
                    resp = urllib2.urlopen(req, timeout=10)
                    break
                except:
                    if i < Max_Num-1:
                        continue
                    else:
                        print 'URLError: <urlopen error timed out> All times is failed.'
                        sys.exit(1)
            content = resp.read()
            et = etree.HTML(content)
            result = et.xpath('/html/body/div[@id="container"]/div/div[@id="list"]/table[@class="table table-bordered table-striped"]/tbody/tr')
            for i in result:
                t1 = i.xpath('./td[@data-title="IP"]/text()')[0]
                t2 = i.xpath('./td[@data-title="PORT"]/text()')[0]
                print "IP:%s\tPort:%s" % (t1, t2)
                if datebase.isAlive(self.GFW, t1, t2):
                    datebase.insert_gwdb(self.now, self.source, t1, t2)

class datebaseOp():

    def __init__(self):
        userAgent=[
            "Mozilla/5.0 (Windows NT 5.1; rv:37.0) Gecko/20100101 Firefox/37.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
            "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"]
        self.user_agent = random.choice(userAgent)
        self.header = {"User-Agent": self.user_agent}
        self.dbname="proxy.db"
        self.now = time.strftime("%Y-%m-%d")

    def insert_gndb(self, date, source, ip, port):
        dbname=self.dbname
        try:
            conn=sqlite3.connect(dbname)
        except:
            print "Error to open database%" %self.dbname
        create_tb='''
        CREATE TABLE IF NOT EXISTS PROXY_GN
        (DATE TEXT,
        IP TEXT UNIQUE,
        PORT TEXT,
        SOURCE TEXT
        );
        '''
        conn.execute(create_tb)
        insert_db_cmd='''
        INSERT INTO PROXY_GN (DATE,IP,PORT,SOURCE) VALUES ('%s','%s','%s','%s');
        ''' %(date, ip, port, source)
        try:
            conn.execute(insert_db_cmd)
        except:
            print "Error happended when insert to datebgase."
        conn.commit()
        conn.close()

    def insert_gwdb(self, date, source, ip, port):
        dbname=self.dbname
        try:
            conn=sqlite3.connect(dbname)
        except:
            print "Error to open database%" %self.dbname
        create_tb='''
        CREATE TABLE IF NOT EXISTS PROXY_GW
        (DATE TEXT,
        IP TEXT UNIQUE,
        PORT TEXT,
        SOURCE TEXT
        );
        '''
        conn.execute(create_tb)
        insert_db_cmd='''
        INSERT INTO PROXY_GW (DATE,IP,PORT,SOURCE) VALUES ('%s','%s','%s','%s');
        ''' %(date, ip, port, source)
        try:
            conn.execute(insert_db_cmd)
        except:
            print "Error Duplicate happended when insert to datebgase."
        conn.commit()
        conn.close()

    def isAlive(self, GFW, ip, port):
        proxy={'http':ip+':'+port}
        print proxy
        #使用这个方式是全局方法。
        proxy_support=urllib2.ProxyHandler(proxy)
        opener=urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)
        if GFW == 'yes':
            test_url = "http://www.qq.com"
        else:
            test_url = "http://www.baidu.com"
        req=urllib2.Request(test_url, headers=self.header)
        try:
            resp=urllib2.urlopen(req, timeout=5)

            if resp.code==200:
                print "work"
                return True
            else:
                print "not work"
                return False
        except :
            print "Not work"
            return False

    def check_gndb_pool(self):
        conn = sqlite3.connect(self.dbname)
        query_cmd = '''
        select IP,PORT from PROXY_GN;
        '''
        cursor = conn.execute(query_cmd)
        for row in cursor:
            if not self.isAlive('yes', row[0],row[1]):
                delete_cmd = '''
                delete from PROXY_GN where IP='%s'
                ''' %row[0]
                print "delete IP %s in db" %row[0]
                conn.execute(delete_cmd)
                conn.commit()
        conn.close()

    def check_gwdb_pool(self):
        conn = sqlite3.connect(self.dbname)
        query_cmd = '''
        select IP,PORT from PROXY_GW;
        '''
        cursor = conn.execute(query_cmd)
        for row in cursor:
            if not self.isAlive('no', row[0], row[1]):
                delete_cmd = '''
                delete from PROXY_GW where IP='%s'
                ''' %row[0]
                print "delete IP %s in db" %row[0]
                conn.execute(delete_cmd)
                conn.commit()
        conn.close()

datebase = datebaseOp()

if __name__ == "__main__":
    now = datetime.datetime.now()
    print "Start at %s" % now
    if len(sys.argv) == 2:
        argv = sys.argv[1]
    else:
        argv = 'update'
    domestic = domestic()
    overseas = overseas()
    if argv == 'getgn':
        domestic.getKuai(5)
        domestic.getXici(1)
    elif argv == 'getgw':
        overseas.getKuai(5)
        overseas.getXici(1)
    elif argv == 'update':
        datebase.check_gndb_pool()
        datebase.check_gwdb_pool()
    elif argv == 'updategn':
        datebase.check_gndb_pool()
    elif argv == 'updategw':
        datebase.check_gwdb_pool()
    elif argv == 'getgnxici':
        domestic.getXici(1)
    elif argv == 'getgnkuai':
        domestic.getKuai(5)
    elif argv == 'getgwxici':
        overseas.getXici(1)
    elif argv == 'getgwkuai':
        overseas.getKuai(5)
    else:
        print "Oops, command not found."


