from query_generator import QueryGenerator
from real_estate_model import RealEstate
from database_connection import db_connection, db_cursor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from real_estate_crawler import RealEstateSpider

process = CrawlerProcess(get_project_settings())
process.crawl(RealEstateSpider)
process.start()
