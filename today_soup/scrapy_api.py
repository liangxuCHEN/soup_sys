from requests_html import HTMLSession
# import asyncio
import os, django
import sys
sys.path.append("/home/louis/Documents/soup_sys")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "soup_sys.settings")
django.setup()

from today_soup.models import SoupModel

session = HTMLSession()

def get_list(url):
    #url = 'http://www.2kcn.com/soup/list_page.php?page=%s' % page
    print('open %s' % url)
    # future = asyncio.get_event_loop().run_in_executor(functools.partial(session, url, ))

    res = session.get(url)

    content = res.html.xpath('/html/body/div[3]/div/div[1]/div/div[2]/ul', first=True)

    items = content.find('li')
    soup = {'page_url': url}
    for item in items:
        item_url  = item.find('a', first=True)
        item_id = item_url.attrs['href'].split('id=')[1]
        soup['soup_origin_id'] = item_id
        soup['head_url'] = item_url.find('img', first=True).attrs['src']
        soup.update(get_page1(item_id))
        soup.update(get_page2(item_id))
        soup_model = SoupModel(**soup)
        soup_model.save()
        print(soup_model.id, soup_model.title)


def get_page1(item_id):
    url = 'http://www.2kcn.com/soup/soup.php?id=%s' % item_id
    res = session.get(url)
    title = res.html.xpath("/html/body/div[3]/div/div[1]/div/div[1]/h2", first=True).text
    div = res.html.xpath('/html/body/div[3]/div/div[1]/div/div[2]', first=True)
    content = div.text
    content = content.split('DIY步骤')[0]
    return {'title':title, 'content':content}



def get_page2(item_id):
    url = 'http://www.2kcn.com/soup/soup_msg.php?id=%s' % item_id
    res2 = session.get(url)
    imgs = res2.html.find('img')
    img_urls = []
    for m in imgs:
        img_urls.append(m.attrs['src'])

    plins = res2.html.find('p')
    text = ''
    for p in plins:
        text += p.text + '\n'

    return {'pic_urls': ';'.join(img_urls), 'how_to_do':text}


def my_requests():
    urls = []
    url = 'http://www.2kcn.com/soup/list_page.php?page={id}'
    # 1-10已经好了
    for i in range(10, 50):
        urls.append(url.format(id=i))
    return urls




if __name__ == '__main__':
    req_list = my_requests()
    # loop = asyncio.get_event_loop()
    # tasks = [get_list(url) for url in req_list]
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()
    #get_lists()
    for url in req_list:
        get_list(url)