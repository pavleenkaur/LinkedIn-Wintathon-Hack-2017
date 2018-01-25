
# coding: utf-8

# In[189]:

import numpy as np
import pandas as pd
job_data = pd.read_csv('job_threshold.csv')
required_job = job_data[job_data['Job_titles']=='junior datascientist']
required_job = required_job[required_job['Experience_yrs']<=0]

applicant_data = pd.read_csv('applicants.csv')

required_applicant = applicant_data[applicant_data['Experience_yrs']<=0]
required_applicant = required_applicant.reset_index()
required_applicant


# In[190]:

required_applicant


# In[191]:

required_applicant.iloc[0][4]


# In[192]:

required_applicant.shape


# In[193]:

required_applicant.iloc[243][3]


# In[194]:

required_job.iloc[0][5]


# In[195]:

rejected_applicant_list = []
final_applicant = required_applicant
final_applicant


# In[196]:

count = 0;
for i in range(0,244):
    for j in range(3,27):
        if required_applicant.iloc[i][j] >= required_job.iloc[0][j]:
            continue;
        else:
            count = count +1;
            url = required_applicant.User_url
            rejected_applicant_list.append(url)
            final_applicant = final_applicant[required_applicant.User_url != url ]
            break;


# In[197]:

count


# In[ ]:



