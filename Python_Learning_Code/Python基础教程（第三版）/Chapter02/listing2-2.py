# Split up a URL of the form http://www.something.com

url = input('Please enter the URL:')
domain = url[4:-4]

print("Domain name: " + domain)
# Please enter the URL:www.nichijou-lab.com
# Domain name: nichijou-lab
