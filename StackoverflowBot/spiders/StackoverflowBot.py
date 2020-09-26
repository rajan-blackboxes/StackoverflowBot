from ..items import StackoverflowbotItem
import scrapy


class StackoverflowBot(scrapy.Spider):
    name = 'stackoverflow'

    def __init__(self, language, max_page, *args, **kwargs):
        """
        :param language: which language to scrape
        :param max_page: Max pagination of giving language or How much pages to scrape?,
        """
        super(StackoverflowBot, self).__init__(*args, **kwargs)
        self.max_page = max_page
        self.language = language
        self.urls = ['https://stackoverflow.com/questions/tagged/{}?tab=active&page=1&pagesize=50'.format(language)]
        self.page_no = 2

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        items = StackoverflowbotItem()
        question_summary = response.css('.question-summary')
        for question_detail in question_summary:
            stats_container = question_detail.css('div.statscontainer div.stats')
            question_vote_count = stats_container.css('div.vote div.votes span.vote-count-post strong::text').extract()
            question_answer_count = stats_container.css('div.status strong::text').extract()

            answer_container = question_detail.css('div.summary')
            question_title = answer_container.css('h3 a::text').extract()
            question_title_link = 'https://stackoverflow.com' + answer_container.css('h3 a').attrib['href']
            question_tags = answer_container.css(' div.tags a::text').getall()

            items['question_vote_count'] = question_vote_count
            items['question_answer_count'] = question_answer_count
            items['question_title'] = question_title
            items['question_title_link'] = question_title_link
            items['question_tags'] = question_tags
            yield items

        next_page = f'https://stackoverflow.com/questions/tagged/{self.language}?tab=active&page={self.page_no}' \
                    f'&pagesize=50'
        if self.page_no < int(self.max_page)+1:
            print('--'*10 + "Came: {} of {}".format(self.max_page, self.page_no).center(20)+'--'*10,
                  end='\r', flush=True)
            self.page_no += 1
            yield response.follow(next_page, callback=self.parse)
