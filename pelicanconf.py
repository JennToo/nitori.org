AUTHOR = "Jennifer Wilcox"
SITENAME = "nitori.org"
SITEURL = "https://nitori.org"

PATH = "content"

TIMEZONE = "America/Chicago"

DEFAULT_LANG = "en"

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = None
SOCIAL = None

DEFAULT_PAGINATION = False

ARTICLE_URL = 'posts/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
SLUGIFY_SOURCE = 'title'

FEED_DOMAIN = SITEURL
FEED_RSS = 'rss.xml'
