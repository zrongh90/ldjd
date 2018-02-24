import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        # for title in response.css('h2.entry-title'):
        #     yield {'title': title.css('a ::text').extract_first()}
        #
        # for author in response.css('span.author'):
        #     yield {'author': author.css('a ::text').extract_first()}

        for header in response.css('header.entry-header'):
            yield {
                'title': header.css('h2.entry-title > a ::text').extract_first(),
                'author': header.css('span.author > a ::text').extract_first(),
            }
        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)
