

import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
url='https://www.glassdoor.co.in/Explore/browse-companies.html?'
webpage=requests.get(url,headers=headers).text

soup=BeautifulSoup(webpage, 'lxml')

print(soup.prettify())

title=soup.title
print(title)

"""## TO FIND OUT NAMES OF THE COMPANIES"""

soup.find_all('h2')

for i in soup.find_all('h2')[1:]:
    print(i.text.strip())

"""## TO FIND OUT COMPANY DETAILS"""

for i in soup.find_all('div',class_='row d-flex flex-wrap'):
    print(i.text.strip())

len(soup.find_all('b'))

len(soup.find_all('div' , class_='d-flex flex-column align-items-center'))

"""## CONSIDERING THE WHOLE CONTAINER"""

company=soup.find_all('div',class_='row d-flex flex-wrap')

len(company)

"""## COMPANY DESCRIPTION"""

comp_detail=soup.find('p',class_='css-1sj9xzx css-56kyx5').text.strip()[:215]
print(comp_detail)

c_name=[]
rating=[]
reviews=[]
industry=[]
hq=[]
jobs=[]
employee=[]




for i in company:
   c_name.append(i.find('h2').text.strip())
   rating.append(i.find('b').text.strip())
   reviews.append(i.find('div' , class_='d-flex flex-column align-items-center').text.strip())
   industry.append(i.find('span', attrs = {'data-test' : 'employer-industry'}).text.strip())
   hq.append(i.find('span',class_='d-block mt-0 css-56kyx5').text.strip())
   jobs.append(i.find('h3', attrs = {'data-test' : 'cell-Jobs-count'}).text.strip())
   employee.append(i.find('span', attrs = {'data-test' : 'employer-size'}).text.strip())
 
  
df=pd.DataFrame({'Company_name':c_name,'Rating':rating,'Reviews':reviews,'Industry_type':industry,'Total_headquater':hq,'Total_jobs':jobs,'Total_employee':employee,
                })

"""## COMPANY NAMES"""

c_name

"""## COMPANY RATINGS"""

rating

"""## COMPANY REVIEWS"""

reviews

"""## INDUSTRY TYPES"""

industry

"""## TOTAL NUMBER OF COMPANIES LOCATION"""

hq

"""## TOTAL JOBS"""

jobs

"""## TOTAL EMPLOYEE


"""

employee

"""## DATAFRAME 

"""

df

df.shape

"""## CREATING DATAFRAME FOR ALL PAGES"""

final=df

for j in range (1,11):

     url='https://www.glassdoor.co.in/Explore/browse-companies.htm?page={}'.format(j)
     headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
     webpage=requests.get(url,headers=headers).text
     soup=BeautifulSoup(webpage, 'lxml')
     company=soup.find_all('div',class_='row d-flex flex-wrap')

     c_name=[]
     rating=[]
     reviews=[]
     industry=[]
     hq=[]
     jobs=[]
     employee=[]

     for i in company:
        try:
          c_name.append(i.find('h2').text.strip())
        except:
          c_name.append(np.nan)   

        try:
           rating.append(i.find('b').text.strip())
        except:
            rating.append(np.nan)   

        try:
          reviews.append(i.find('div' , class_='d-flex flex-column align-items-center').text.strip())
        except:
           reviews.append(np.nan)  
 
        try:
          industry.append(i.find('span', attrs = {'data-test' : 'employer-industry'}).text.strip())
        except:
          industry.append(np.nan)   
      
        try:
           hq.append(i.find('span',class_='d-block mt-0 css-56kyx5').text.strip())
        except:
           hq.append(np.nan)  

        try:
          jobs.append(i.find('h3', attrs = {'data-test' : 'cell-Jobs-count'}).text.strip())
        except:
          jobs.append(np.nan)

        try:
           employee.append(i.find('span', attrs = {'data-test' : 'employer-size'}).text.strip())
        except:
           employee.append(np.nan)

  
     df=pd.DataFrame({  'Company_name':c_name,
                        'Rating':rating,
                        'Reviews':reviews,
                        'Industry_type':industry,
                        'Total_headquater':hq,
                        'Total_jobs':jobs,
                        'Total_employee':employee,
                      }) 
     final=final.append(df)

final

final.shape

df.sample(5)

"""## EXPOTING THE DATAFRAME INTO AN EXTENAL CSV

"""

x = np.arange(len(final))
final.insert(0, 'index', x)
final.to_csv('final.csv',index=False)