def avito(req):
    return "https://www.avito.ru/rostov-na-donu/bytovaya_elektronika?q="+req+"&s=104"

def dns(req, tt = ""):
    return  "https://www.dns-shop.ru/search/?q="+req+"&stock=hard" + tt

def citi(req):
    return "https://www.citilink.ru/search/?text="+req