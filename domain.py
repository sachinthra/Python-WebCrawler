from urllib.parse import urlparse

#get domail name example.com
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        #return result[-3] + '.' + results[-2] + '.' + results[-1] 
        return results[-2] + '.' + results[-1] 
    except:
        return ''

# get subdomain and domain name.wxamplee.com

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

#print(get_domain_name('https://vit.ac.in/indesx/index.php'))
