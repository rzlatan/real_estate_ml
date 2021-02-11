import scrapy
import Constants
from real_estate_model import RealEstate
from query_generator import QueryGenerator
from database_connection import db_cursor, db_connection
from scrapy.cmdline import execute
import re


class RealEstateSpider(scrapy.Spider):
    name = "real_estate_spider"
    allowed_domains = ["4zida.rs"]

    start_urls = [
        "https://www.4zida.rs/izdavanje-stanova?strana=1",
        "https://www.4zida.rs/izdavanje-kuca?strana=1",
        "https://www.4zida.rs/prodaja-stanova?strana=1",
        "https://www.4zida.rs/prodaja-kuca?strana=1"
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

    @staticmethod
    def parse_offer_type(real_estate: RealEstate, response: scrapy.http.Response):
        if Constants.RENTING == response.url.split('/')[3]:
            real_estate.set_offer_type(Constants.RENTING)
        if Constants.SELLING == response.url.split('/')[3]:
            real_estate.set_offer_type(Constants.SELLING)

    @staticmethod
    def parse_object_type(real_estate: RealEstate, response: scrapy.http.Response):
        if Constants.FLATS == response.url.split('/')[4]:
            real_estate.set_object_type(Constants.FLAT)
        if Constants.HOUSES == response.url.split('/')[4]:
            real_estate.set_object_type(Constants.HOUSE)

    @staticmethod
    def parse_price(real_estate: RealEstate, response: scrapy.http.Response):
        if real_estate.get_offer_type() == Constants.RENTING:
            price_value = response.xpath('//div[@class="info-item ng-star-inserted"]/div[@class="value"]/span/text()').extract_first()
            if price_value is not None:
                price_value = price_value.replace(u'\xa0', u' ')
                price_value = price_value.replace('.', '')
                price_value = price_value.split(' ')[0]
                real_estate.set_price(int(price_value))
        if real_estate.get_offer_type() == Constants.SELLING:
            price_value = response.xpath('//div[@class="info-item"]/div[@class="value"]/span/text()').extract_first()
            if price_value is not None:
                price_value = price_value.replace(u'\xa0', u' ')
                price_value = price_value.replace('.', '')
                price_value = price_value.split(' ')[0]
                real_estate.set_price(int(price_value))

    @staticmethod
    def parse_location(real_estate: RealEstate, response: scrapy.http.Response):
        location_info = response.xpath('//h1[@class="location"]/text()').extract_first().split(',')
        location = None
        city = location_info[-1].strip()

        if len(location_info) > 1 and location_info is not None:
            if location_info[1] == Constants.GENERAL_MUNICIPALITY:
                location = location_info[0].strip()
            else:
                location = location_info[1].strip()
        else:
            location = location_info[0].strip()

        real_estate.set_city(city)
        real_estate.set_municipality(location)

    @staticmethod
    def parse_details(real_estate: RealEstate, response: scrapy.http.Response):
        details = response.xpath('//div[@class="wrapper ng-star-inserted"]/div/text()').getall()

        for i in range(len(details)):
            label = details[i]

            if label is not None:

                if label == Constants.ROOM_NUMBER:
                    room_count = details[i + 1].strip()
                    real_estate.set_room_count(room_count)

                if label == Constants.SQUARE_FOOTAGE:
                    try:
                        square_footage = re.search(r'\d+', details[i + 1].strip()).group()
                        real_estate.set_square_footage(square_footage)
                    except:
                        print("Square footage was not provided as a number")

                if label == Constants.HEATING_SYSTEM:
                    heating_system = details[i + 1].strip()
                    real_estate.set_heating_system(heating_system)

                if label == Constants.EQUIPMENT_STATE:
                    equipment_state = details[i + 1].strip()
                    real_estate.set_equipment_state(equipment_state)

                if label == Constants.PARKING:
                    if details[i + 1] is not None:
                        real_estate.set_has_parking(True)
                    else:
                        real_estate.set_has_parking(False)

                if label == Constants.GARAGE:
                    if details[i + 1] is not None:
                        real_estate.set_has_garage(True)
                    else:
                        real_estate.set_has_garage(False)

                if label == Constants.ELEVATOR:
                    if details[i + 1] is not None:
                        if Constants.YES in details[i + 1].lower():
                            real_estate.set_has_elevator(True)
                        if Constants.NO in details[i + 1].lower():
                            real_estate.set_has_elevator(False)

                if label == Constants.BATHROOM_NUMBER:
                    if details[i + 1] is not None:
                        if Constants.BATHROOM_SUBST in details[i + 1]:
                            try:
                                bathroom_count = re.search(r'\d+', details[i + 1].strip()).group()
                                real_estate.set_bathroom_count(bathroom_count)
                            except:
                                print("bathroom count was not provided, assuming 1 bathroom")
                                real_estate.set_bathroom_count(1)
                        else:
                            real_estate.set_bathroom_count(1)

                if label == Constants.FLOOR:
                    if details[i + 1] is not None:
                        try:
                            floor = re.search(r'\d+', details[i + 1].strip()).group()
                            real_estate.set_floor(floor)
                        except:
                            print("Floor information was not provided")

                if label == Constants.YEAR_BUILD:
                    if details[i + 1] is not None:
                        try:
                            year_built = re.search(r'\d+', details[i + 1].strip()).group()
                            real_estate.set_year_built(year_built)
                        except:
                            print("built year was not provided")

                if label == Constants.REGISTERED:
                    if details[i + 1] is not None:
                        registration_state = details[i + 1].strip()
                        real_estate.set_registration_state(registration_state)

                if label == Constants.CONSTRUCTION_STATE:
                    if details[i + 1] is not None:
                        construction_state = details[i + 1].strip()
                        real_estate.set_construction_state(construction_state)

    @staticmethod
    def parse_description(real_estate: RealEstate, response: scrapy.http.Response):
        description = response.xpath('//div[@class="description"]/text()').extract_first()
        if description is not None:
            real_estate.set_description(description)

    def parse_error(self, failure):
        print(str(failure))

    def parse(self, response):
        # Get basic information from the page
        #
        base_url = RealEstateSpider.get_base_url(response.url)
        last_page = int(RealEstateSpider.get_last_page(response))
        current_page = int(RealEstateSpider.get_current_page(response))
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

        # Parse offer type
        #
        RealEstateSpider.parse_offer_type(real_estate, response)

        # Parse object type
        #
        RealEstateSpider.parse_object_type(real_estate, response)

        # Parse price
        #
        RealEstateSpider.parse_price(real_estate, response)

        # Parse location
        #
        RealEstateSpider.parse_location(real_estate, response)

        # Parse description
        #
        RealEstateSpider.parse_description(real_estate, response)

        # Parse details
        #
        RealEstateSpider.parse_details(real_estate, response)

        statement = QueryGenerator.insert_real_estate_query(real_estate)
        db_cursor.execute(statement)
        db_connection.commit()

