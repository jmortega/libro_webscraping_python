from dude import select

@select(css="a")
def get_link(element):
    return {"url": element.get_attribute("href")}
