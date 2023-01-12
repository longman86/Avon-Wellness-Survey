import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(layout='wide')
image = Image.open("AvonLogo.png")
st.image(image, use_column_width=False)
st.title('AVON HMO Wellness Survey')


path = r'C:\Users\ademola.atolagbe\OneDrive - Avon Healthcare Ltd\Member Wellness.csv'
#path = 'https://avonhealthcareltd-my.sharepoint.com/personal/droguguah_ejinkeonye_avonhealthcare_com/Documents/Documents/Wellness%20member%20list.xlsx?web=1'
wellness_df = pd.read_csv(path)


enrollee_id = st.text_input('Kindly input your member number and press the enter key to confirm your eligibility')
enrollee_id = enrollee_id.upper()


#def IsMemberEligible(enrollee_id):
#member_list = wellness_df.AvonoldEnrolleId.tolist()
if enrollee_id:
    if enrollee_id in wellness_df['AvonoldEnrolleId'].values:
        enrollee_name = wellness_df.loc[wellness_df['AvonoldEnrolleId'] == enrollee_id, 'membername'].values[0]
        st.balloons()
        st.info(f'Welcome {enrollee_name}. \n Please click the link below to continue',icon="✅")
        st.write("[AVON Wellness Survey](https://forms.office.com/Pages/ResponsePage.aspx?id=y7xkPyIn5UK1ynGyBgRdh8-wGEk3Z51JtzuJQUW5THtUN0s5RVJQOFQ5R0swSktXSlQyWlBBUjFWUi4u&origin=Invitation&channel=1)")
       
    elif enrollee_id not in wellness_df['AvonoldEnrolleId'].values:
        st.info('You are not eligible to participate, please contact your HR or Client Manager')
else:
    st.write('You must input your Member number to continue')

#st.write(IsMemberEligible(memberno))
