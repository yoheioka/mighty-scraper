from apartment_scraper import ApartmentScraper


def handler(event, context):
    ApartmentScraper().run()
    return 'OK'
