# -*- coding: utf-8 -*-
'''
爬取职位名、公司名、工作地点、薪资、发布时间
'''
import scrapy
from scrapy import Request
from scrapy.spiders import Spider
from Recruitment.items import RecruitmentItem
import re


class GethtmlSpider(scrapy.Spider):
    name = 'getHTML'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Accept': 'text/css,*/*;q=0.1',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Referer': 'https://www.51job.com/',
        'Host': 'search.51job.com',
        'Cookies': 'guid=14f122db9ed2c605a181b537d6229b9b; _ujz=MTM0NzUzNjY3MA%3D%3D; ps=needv%3D0; adv=adsnew%3D0%26%7C%26adsnum%3D2004282%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttps%253A%252F%252Fwww.baidu.com%252Fother.php%253Fsc.af00000AaJc-CgNBXsT4PRxRsuypV0b3c604BM7SVzM10Qw2WiyDjsW6Bm0kDntW8_7mecIRNkPr0uPFDoAZ-e-6mPAtjpkygOmbbqeBfHW5qH0LysKaCc1BVKGj1Yd0L4Sb6mP6YjcI-HJ2WUUHDtzAgurRq5lCRDHspM0aYdtCGZUotk8e6r6XYLyfWkaLnfXQOdJn8sfnFpaDZJ5jZcsyUYKF.7b_NR2Ar5Od66CHnsGtVdXNdlc2D1n2xx81IZ76Y_uQQr1F_zIyT8P9MqOOgujSOODlxdlPqKMWSxKSgqjlSzOFqtZOmzUlZlS5S8QqxZtVAOtIO0hWEzxkZeMgxJNkOhzxzP7Si1xOvP5dkOz5LOSQ6HJmmlqoZHYqrVMuIo9oEvpSMG34QQQYLgFLIW2IlXk2-muCyr1FkzTf.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqPH7JUvc0IgP-T-qYXgK-5H00mywxIZ-suHY10ZIEThfqPH7JUvc0ThPv5HmdPHnL0ZNzU7qGujYkPHDvrjDzPH640Addgv-b5HDkPjczrj0k0AdxpyfqnH0drjnLnjn0UgwsU7qGujYknHR1P0KsI-qGujYs0APzm1Y1PjDLPs%2526ck%253D4579.3.101.320.151.132.160.289%2526dt%253D1583844151%2526wd%253D%2526tpl%253Dtpl_11534_21264_17382%2526l%253D1516812589%2526us%253DlinkName%25253D%252525E6%252525A0%25252587%252525E5%25252587%25252586%252525E5%252525A4%252525B4%252525E9%25252583%252525A8-%252525E4%252525B8%252525BB%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D%252525E3%25252580%25252590%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A751Job%252525E3%25252580%25252591-%25252520%252525E5%252525A5%252525BD%252525E5%252525B7%252525A5%252525E4%252525BD%2525259C%252525E5%252525B0%252525BD%252525E5%2525259C%252525A8%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A7%2521%252526linkType%25253D; slife=lowbrowser%3Dnot%26%7C%26lastlogindate%3D20200317%26%7C%26securetime%3DUW1VY1U7AGdfNVZsCzRcNFdkAjU%253D; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; 51job=cenglish%3D0%26%7C%26; search=jobarea%7E%60020000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60020000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA32%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CA%FD%BE%DD%B7%D6%CE%F6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60020000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21',
        'Encoding': 'utf-8'
    }

    def start_requests(self):
        url1 = 'https://search.51job.com/list/020000,000000,0000,32,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,'
        url2 = '.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
        url = url1 + '1' + url2
        yield Request(url, headers=self.headers)

    # 处理提取的网页
    def parse(self, response):
        # 数据存储的地方
        # print(response.body)
        item = RecruitmentItem()
        jobs = response.xpath('//div[@class="dw_table"]/div[@class="el"]')

        for job in jobs:
            co = job.xpath('.//span[@class="t2"]/a[@target="_blank"]/text()').extract()
            if len(co) == 0:
                item['companyname'] = 'None'
            else:
                item['companyname'] = job.xpath('.//span[@class="t2"]/a[@target="_blank"]/text()').extract()[0]
            item['workingplace'] = job.xpath('.//span[@class="t3"]/text()').extract()[0]
            item['salary'] = job.xpath('.//span[@class="t4"]/text()').extract()
            item['posttime'] = job.xpath('.//span[@class="t5"]/text()').extract()[0]
            a = job.xpath('.//p[@class="t1 "]/span/a[@target="_blank"]/text()').extract()
            item['jobname'] = [x.strip() for x in a if x.strip() != '']
            yield item

        for i in range(2, 24):
            url1 = 'https://search.51job.com/list/020000,000000,0000,32,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,'
            url2 = '.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
            next_url = url1 + str(i) + url2
            print(next_url)
            yield Request(next_url, headers=self.headers, callback=self.parse)
