# -*- coding: utf-8 -*-
import scrapy
import Images

class TopgoodspiderSpider(scrapy.Spider):
    name = "tm_goods"
    allowed_domains = ["http://www.tmall.com"]
    start_urls = (
        'https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.4TGf7l&cat=50025135&q=%C6%B7%C5%C6%C5%AE%D7%B0&sort=s&style=g&search_condition=7&from=sn_1_rightnav&active=2#J_crumbs',
    )
    count=0
    def parse(self, response):
        TopgoodspiderSpider.count+=1
        divs=response.xpath('/html/body/div[1]/div/div[3]/div/div[7]/div[1]/div/div[1]/a/text()')[0].extract()
        if not divs:
            self.log("List page error %s"%response.url)
        print "商品总数:",len(divs)
        for div in divs:
            item=TopgoodsItem()
            item["GOODS_PRICE"]=response.xpath('/html/body/div[1]/div/div[3]/div/div[7]/div[1]/div/p[1]/em/text()')[0].extract()
            item["GOODS_NAME"]=response.xpath('/html/body/div[1]/div/div[3]/div/div[7]/div[1]/div/p[2]/a/text()')[0].extract()
            item["GOODS_NAME"]=response.xpath('/html/body/div[1]/div/div[3]/div/div[7]/div[1]/div/p[2]/a/text()')[0].extract()
            pre_good_url=response.xpath('/html/body/div[1]/div/div[3]/div/div[7]/div[1]/div/p[2]/a/@href')[0].extract()
            item["GOODS_URL"]=pre_good_url if "http:" in pre_good_url else ("http:"+pre_good_url)
            #try:
#                file_urls=response.xpath('/html/body/div[1]/div/div[3]/div/div[7]/div[1]/div/div[1]/a/img/@src'|'/html/body/div[1]/div/div[3]/div/div[7]/div[1]/div/div[1]/a/img/@data-ks-lazyload-custom')[0].extract()
            file_urls=response.xpath('/html/body/div[1]/div/div[3]/div/div[7]/div[1]/div/div[1]/a/img/@src')[0].extract()
            item["file_urls"]="http:"+file_urls
            #except Exception,e:
            print "Error occured",e
            import pdb;pdb.set_trace()
            yield scrapy.Request(url=item["GOODS_URL"],meta={'item':item},callback=self.parse_detail,dont_filter=true)

    def parse_detail(self,response):
        div=response.xpath('//div[@class="extend"]/ul')
        if not divs:
            self.log("List page error %s" % response.url)
        item=response.meta['item']
        div=div[0]
        item["SHOP_NAME"]=div.xpath('li[1]/div/a/text()')[0].extract()
        item["SHOP_URL"]=div.xpath('li[1]/div/a/@href')[0].extract()
        item["COMPANY_NAME"]=div.xpath('li[3]/div/text()')[0].extract().strip()
        item["COMPANY_ADDRESS"]=div.xpath('li[4]/div/text()')[0].extract().strip()
        yield item

