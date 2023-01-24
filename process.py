import requests
from bs4 import BeautifulSoup

# url = "https://electrical-engineering-portal.com/power-substation-project-design-construction-erection-commissioning"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

def get_text_from_url(url: str) -> tuple[list[str], list[str]]:
    f = requests.get(url, headers=headers)

    articla_list = []

    soup = BeautifulSoup(f.content, 'lxml')

    article_body = soup.find("div", {
        "class": "entry"
    })

    if article_body is None:
        pass

    headings = ['']
    contents = [[]]

    for ele in article_body.children:
        text = ele.get_text()
        if not text:
            continue
        text = text.strip()
        if text and ele.name.startswith('h'):
            headings.append(text)
            contents.append([])
        else:
            if text and len(text)>0:
                if text.lower().startswith('figure') or text.lower().startswith('go back to the contents table'):
                    continue
                contents[-1].append(text)

    assert len(headings) == len(contents)

    if len(contents[0]) == 0:
        headings.pop(0)
        contents.pop(0)

    for i in range(len(contents)):
        contents[i] = '\n\n'.join(contents[i])
        contents[i] = contents[i].strip()

    return headings, contents


def create_summary(headings: list[str], contents: list[str]):
    # TODO: Integrate model in this function to process text
    index = 0
    if not len(contents) or not len(headings):
        return f"{len(contents)} Content. {len(headings)} Headings."
    if not headings[index].strip() and len(contents) > 1:
        index += 1
    return contents[index].replace('\n',' ').replace('  ',' ')