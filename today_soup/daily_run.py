import os, django
import sys
sys.path.append("/home/clx/soup_sys")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "soup_sys.settings")
django.setup()
from today_soup.scrapy_api import send_one_soup_by_day 


if __name__ == '__main__':
    send_one_soup_by_day()

