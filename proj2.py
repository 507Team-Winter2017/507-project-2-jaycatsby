##############
## proj2.py ##
##############
import requests
from bs4 import BeautifulSoup


################################
#### Function for Problem 1 ####
################################
def nyt_headlines(souped_ny):
	h_lst = []
	# headlines = souped_ny.find_all(class_='story-heading')
	headlines = souped_ny.find_all('h2', {'class':'story-heading'})
	for headline in headlines:
		if headline.a:
			h_lst.append(headline.a.get_text())
	return h_lst

################################
#### Function for Problem 2 ####
################################
def get_mi_most_read(souped_mi):
	m_lst = []
	m_li = []
	most_read = souped_mi.find_all(class_='item-list')
	for m_read in most_read:
		m_li = m_read.find_all('li')

	for m in m_li:
		m_lst.append(m.a.get_text())

	return m_lst

################################
#### Function for Problem 3 ####
################################
def get_cat_alt(souped_cat):
	cat_img = souped_cat.find_all('img')
	for cat in cat_img:
		print(cat.get('alt','No alternative text provided!!'))

#################################
#### Functions for Problem 4 ####
#################################
def get_email(b_url, ext_url):
	si_contact_url = b_url + ext_url
	si_contact_req = requests.get(si_contact_url, headers={'User-Agent': 'SI_CLASS'})
	si_contact_soup = BeautifulSoup(si_contact_req.text, 'html.parser')
	contact_email = si_contact_soup.find(class_='field-type-email')
	return contact_email.a.get_text()
	

def get_UMSI_emails(souped_umsi, emails):
	si_base_url = 'https://www.si.umich.edu'
	si_emails = souped_umsi.find_all(class_='field-name-contact-details')
	for em in si_emails:
		if em.a:
			emails.append(get_email(si_base_url, em.a['href']))
	return emails


###################
#### Problem 1 ####
###################
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
nyt_url = 'http://www.nytimes.com'
ny_req = requests.get(nyt_url)
ny_soup = BeautifulSoup(ny_req.text,'html.parser')

headliners = nyt_headlines(ny_soup)

for head in headliners[:10]:
	print(head)


###################
#### Problem 2 ####
###################
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
mi_url = 'https://www.michigandaily.com'
mi_req = requests.get(mi_url)
mi_soup = BeautifulSoup(mi_req.text, 'html.parser')

mi_most_read = get_mi_most_read(mi_soup)

for mi in mi_most_read:
	print(mi)


###################
#### Problem 3 ####
###################
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
cat_url = 'http://newmantaylor.com/gallery.html'
cat_req = requests.get(cat_url)
cat_soup = BeautifulSoup(cat_req.text, 'html.parser')

get_cat_alt(cat_soup)

###################
#### Problem 4 ####
###################
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
umsi_counter = 1
umsi_emails = []
for i in range(7):
	if i == 0:
		umsi_url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
		umsi_req = requests.get(umsi_url, headers={'User-Agent': 'SI_CLASS'})
		umsi_soup = BeautifulSoup(umsi_req.text, 'html.parser')
		get_UMSI_emails(umsi_soup, umsi_emails)

	else:
		umsi_url_next = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4&page={}'.format(i)
		umsi_req_next = requests.get(umsi_url_next, headers={'User-Agent': 'SI_CLASS'})
		umsi_soup_next = BeautifulSoup(umsi_req_next.text, 'html.parser')
		get_UMSI_emails(umsi_soup_next, umsi_emails)

for ems in umsi_emails:
	print(umsi_counter, ems)
	umsi_counter += 1






