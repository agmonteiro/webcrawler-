Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib2
>>> response = urllib2.urlopen
>>> response = urllib2.urlopen('https://www.worldpackers.com/')
>>> page = response.read()
>>> def pega_link(text):
	pre_link = text.find('a href=')
	if pre_link == -1:
		return None,0
	inicio_link = text.find('"',pre_link)
	fim_link = text.find('"',inicio_link + 1)
	url = text [inicio_link + 1 : fim_link]
	return url, fim_link

>>> url,poslink = pega_link(text)

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    url,poslink = pega_link(text)
NameError: name 'text' is not defined
>>> pega_link (page)
('/users/sign_in', 9938)
>>> url,poslink = pega_link(page)
>>> url,poslink
('/users/sign_in', 9938)
>>> def pega_todos_links(text):
	while True:
		url,poslink = pega_link(text)
		if url:
			print url
			text = text[poslink:]
		else:
			break

		
>>> print pega_todos_links(page)
/users/sign_in
/users/sign_up?ref=unlogged_menu
/images/experiences/hostel.jpg
/images/experiences/social_impact.jpg
/images/experiences/nature_lovers.jpg
/images/experiences/social_media.jpg
/images/experiences/photography.jpg
/images/experiences/chef_to_the_world.jpg
/images/experiences/hands_on.jpg
/images/experiences/short_trip.jpg
/images/experiences/long_journey.jpg
/about-us
/stories
/guide/terms
/guide/traveling
/guide/traveling/tour
/guide/traveling/exchange-your-skills
/guide/traveling/how-to-travel
/hosts
mailto:info@worldpackers.com
None
>>> 
