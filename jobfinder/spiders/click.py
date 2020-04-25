import scrapy

from jobfinder.items import ClickItem

class Click(scrapy.Spider):
    name = "click"
    allowed_domains = ["click.in",]
    start_urls = ['https://www.click.in/jobs-ctgid59-p%s' %page for page in range(1,1800)]

    def parse(self, response):
        links = response.xpath('//*[@class="clickin-classified-posts"]/div[1]/div/h2/a/@href').extract()
        i = 1
        for link in links:
            if(i <= len(links)):
                i=i+1
                yield scrapy.Request(link, callback = self.parse_indetail)

    def parse_indetail(self, response):
        item = ClickItem()
        item['title'] = response.xpath('//*[@id="clickin-container"]/div[6]/div[2]/div[2]/h1/text()').extract()
        item['location'] = response.xpath('//*[@id="city_cat_frm"]/div[1]/span/text()').extract()
        

        categorical_data = response.xpath('//*[@id="clickin-container"]/div[6]/div[2]/div[2]/div[1]/table/tbody/tr/td/div/text()').extract()
        for i in range(0,len(categorical_data),2):
            if(categorical_data[i]=='Role'):
                item['role'] = categorical_data[i+1]
            elif(categorical_data[i]=='Experience'):
                item['experience']=categorical_data[i+1]
            elif(categorical_data[i]=="Job Type"):
                item['job_type']=categorical_data[i+1]
            elif(categorical_data[i]=='Key skills'):
                item['skills']=categorical_data[i+1]
            else:
                continue

        contacts = response.xpath('//*[@id="clickin-container"]/div[6]/div[2]/div[2]/div[2]/div/div/text()').extract()
        if(contacts==[]):
            contacts = response.xpath('//*[@id="clickin-container"]/div[6]/div[2]/div[2]/div[3]/div/div/text()').extract()
        for i in range(0,len(contacts),2):
            if(contacts[i]=='Landline'):
                item['landline'] = contacts[i+1]
            elif(contacts[i]=='Mobile'):
                item['mobile'] = contacts[i+1]

        description = response.xpath('//*[@id="clickin-container"]/div[6]/div[2]/div[2]/div[3]/div/p/text()').extract()
        if (description==[]):
            description = response.xpath('//*[@id="clickin-container"]/div[6]/div[2]/div[2]/div[4]/div/p/text()').extract()
        description[0]=' '.join(description[0].split())
        description[-1]=' '.join(description[-1].split())
        item['description']=description


        return item


