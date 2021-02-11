import scrapy
import Constants
from real_estate_model import RealEstate
from query_generator import QueryGenerator
from scrapy.cmdline import execute


class RealEstateSpider(scrapy.Spider):
    name = "real_estate_spider"
    allowed_domains = ["4zida.rs"]

    start_urls = [
        "https://www.4zida.rs/izdavanje-stanova?strana=1",
        # "https://www.4zida.rs/izdavanje-kuca",
        # "https://www.4zida.rs/prodaja-stanova",
        # "https://www.4zida.rs/prodaja-kuca"
    ]

    @staticmethod
    def get_last_page(res):
        pagination_list = res.xpath('//a[contains(@class, "page-link ng-star-inserted")]/text()')
        last_page = pagination_list[len(pagination_list) - 1].extract()
        return last_page

    @staticmethod
    def get_current_page(res):
        page = res.url.split("=")[1]
        return page

    @staticmethod
    def get_base_url(url):
        base_url = url.split("?")[0]
        return base_url

    @staticmethod
    def get_apartments(res):
        apartments = res.xpath('//a[starts-with(@class, "ng-tns-c")]/@href').extract()
        return apartments

    def parse(self, response):
        # Get basic information from the page
        #
        base_url = RealEstateSpider.get_base_url(response.url)
        last_page = RealEstateSpider.get_last_page(response)
        current_page = RealEstateSpider.get_current_page(response)
        home_url = "https://www.4zida.rs"

        # Handle apartments
        #
        apartments = RealEstateSpider.get_apartments(response)
        for apartment in apartments:
            apartment_url = home_url + apartment
            yield scrapy.Request(apartment_url, callback=self.parse_apartment)

        # Visit next page
        #
        if current_page < last_page:
            next_page = int(current_page) + 1
            next_page_url = base_url + "?strana=" + str(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_apartment(self, response):

        # Creating the real estate object
        #
        real_estate = RealEstate()

        # Offer type
        #
        if Constants.RENTING == response.url.split('/')[3]:
            real_estate.set_offer_type(Constants.RENTING)
        if Constants.SELLING == response.url.split('/')[3]:
            real_estate.set_offer_type(Constants.SELLING)

        # Object type
        #
        if Constants.FLATS == response.url.split('/')[4]:
            real_estate.set_object_type(Constants.FLAT)
        if Constants.HOUSES == response.url.split('/')[4]:
            real_estate.set_object_type(Constants.HOUSE)

        # Ostale informacije
        #information = response.xpath('//span/text()')

        infos = response.xpath('//div[@class="wrapper ng-star-inserted"]/div/text()').getall()
        for info in infos:
            print(str(info))

        uknjizenost = 'x'
        cena = -1
        godina = -1
        broj_soba = -1
        broj_kupatila = -1
        povrsina_zemljista = -1
        kvadratura = -1
        sprat = -1
        grad = "x"
        opstina = "x"

        for i in range(0, len(information) - 1):
            print(information[i])

    def parse_error(self, failure):
        print(str(failure))

