from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from skechers.spiders import allkidshoes, allkidclothes, allmenshoes, allmenclothes, allwomenshoes, allwomenclothes

process = CrawlerProcess(get_project_settings())

process.crawl(allkidshoes.AllkidshoesSpider)
process.crawl(allkidclothes.AllkidclothesSpider)
process.crawl(allmenshoes.AllmenshoesSpider)
process.crawl(allmenclothes.AllmenclothesSpider)
process.crawl(allwomenshoes.AllwomenshoesSpider)
process.crawl(allwomenclothes.AllwomenclothesSpider)

process.start()