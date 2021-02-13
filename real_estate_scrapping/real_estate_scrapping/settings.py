# Scrapy settings for real_estate_scrapping project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'real_estate_scrapping'

SPIDER_MODULES = ['real_estate_scrapping.spiders']
NEWSPIDER_MODULE = 'real_estate_scrapping.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'real_estate_scrapping (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'real_estate_scrapping.middlewares.RealEstateScrappingSpiderMiddleware': 543,
#}

#ROTATING_PROXY_LIST_PATH = 'C:\\Users\\Zlatan\\OneDrive\\Desktop\\real_estate_ml\\real_estate_scrapping\\real_estate_scrapping\\http_proxies.txt'

ROTATING_PROXY_LIST = [
    '149.255.36.185:3128',
    '37.120.239.152:3128',
    '116.228.227.211:443',
    #'103.124.111.33:8080',
    #'195.82.113.188:8080',
    #'88.99.134.61:8080',
    #'110.39.177.43:8080',
    #'35.164.173.8:3128',
    #'103.56.235.186:443',
    #'135.181.100.55:3128',
    #'70.165.65.233:48678',
    #'143.110.149.250:3128',
    #'116.203.232.229:8118',
    #'143.110.149.250:3128',
    #'54.168.174.194:3128',
    #'195.225.48.113:58302',
    #'163.172.47.182:3128',
    #'51.159.24.172:3156',
    #'51.158.154.60:3128',
    #'178.77.76.250:8080',
    #'116.203.232.229:8118',
    #'167.172.99.183:8080',
    #'37.120.169.116:8080',
    #'5.16.0.174:8080',
    #'195.170.38.230:8080',
    #'81.17.150.22:8080',
    #'46.35.249.189:41419',
    #'217.77.110.69:8080'
    #'104.198.108.238:8080',
    #'51.158.68.68:8811',
    #'193.29.104.90:3128',
    #'190.145.200.126:53281',
    #'164.132.112.237:80',
    #'51.75.147.41:3128',
    #'51.158.68.133:8811',
    #'37.49.127.228:8080',
    #'85.216.127.185	:8080',
    #'46.237.255.11:8080',
    #'154.16.202.22:8080',
    #'161.35.70.249:8080',
    #'88.198.24.108:8080',
    #'185.236.202.205:3128',
    #'46.21.153.16:3128',
    #'149.172.255.7:8080',
    #'217.8.51.202:8080',
    #'185.189.112.133:3128',
    #'194.58.102.34:34',
    #'193.239.86.249:3128',
    #'185.236.202.170:3128',
    #'136.243.254.196:80',
    #'79.110.52.252:3128',
    #'185.236.203.208:3128',
    #'78.42.42.44:3128',
    #'109.105.205.232:59152'
]

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'real_estate_scrapping.middlewares.RealEstateScrappingDownloaderMiddleware': 543,
   'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
   'rotating_proxies.middlewares.BanDetectionMiddleware': 620
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'real_estate_scrapping.pipelines.RealEstateScrappingPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
