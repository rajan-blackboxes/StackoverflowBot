# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StackoverflowbotItem(scrapy.Item):
    question_vote_count = scrapy.Field()
    question_answer_count = scrapy.Field()
    question_title = scrapy.Field()
    question_title_link = scrapy.Field()
    question_tags = scrapy.Field()
