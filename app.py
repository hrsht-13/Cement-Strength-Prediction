import streamlit as st
import time
import pickle 
import numpy as np
import sklearn

st.title("CEMENET STRENGTH PREDICTOR")
st.info("Cement strength is a critical factor in construction projects as it determines the durability and load-bearing capacity of structures. Traditional methods of strength prediction rely heavily on empirical testing, which can be time-consuming and costly. Machine learning techniques offer an alternative approach to predicting cement strength more efficiently and accurately.")
cement=st.number_input("Cement (kg in a m^3 mixture)")
st.warning("The amount of cement, measured in kilograms, present in one cubic meter of the concrete mixture. Cement is a binding material responsible for providing strength and durability to concrete.",icon="ℹ️")
slag=st.number_input("Blast Furnace Slag (kg in a m^3 mixture)")
st.warning("The quantity of blast furnace slag, measured in kilograms, included in one cubic meter of the concrete mixture. Blast furnace slag is a byproduct of the iron and steel industry and is commonly used as a supplementary cementitious material in concrete production.",icon="ℹ️")
flyash=st.number_input("Fly Ash (kg in a m^3 mixture)")
st.warning("The amount of fly ash, measured in kilograms, added to one cubic meter of the concrete mixture. Fly ash is a waste product from coal combustion and is often used as a partial replacement for cement in concrete to enhance its properties.",icon="ℹ️")
water=st.number_input("Water (kg in a m^3 mixture)")
st.warning("The volume of water, measured in kilograms, incorporated in one cubic meter of the concrete mixture. Water is required for the hydration process of cement and is crucial for the hardening of concrete.",icon="ℹ️")
sp=st.number_input("Superplasticizer (kg in a m^3 mixture)")
st.warning("The quantity of superplasticizer, measured in kilograms, utilized in one cubic meter of the concrete mixture. Superplasticizers are chemical admixtures that are added to concrete to enhance its workability and flow without compromising its strength.",icon="ℹ️")
ca=st.number_input("Coarse Aggregate (kg in a m^3 mixture)")
st.warning("The weight of coarse aggregate, measured in kilograms, present in one cubic meter of the concrete mixture. Coarse aggregate consists of larger particles such as crushed stone, gravel, or recycled concrete, and provides strength and stability to the concrete.",icon="ℹ️")
fa=st.number_input("Fine Aggregate (kg in a m^3 mixture)")
st.warning("The amount of fine aggregate, measured in kilograms, included in one cubic meter of the concrete mixture. Fine aggregate typically consists of sand and is responsible for filling the gaps between coarse aggregates, contributing to the overall strength and workability of concrete.",icon="ℹ️")
age=st.number_input("Age (day)")
st.warning("The age of the concrete specimen, measured in days, at which the compressive strength is determined. Concrete gains strength over time as the hydration process progresses, so the age of the concrete is an important factor in assessing its compressive strength.",icon="ℹ️")

model=pickle.load(open("rfRmodel.pkl","rb"))


btn=st.button("Predict Cement Strength", type="primary")


if btn:
  c_w=cement/water
  f_c=flyash/cement
  c_a=cement/fa
  c_aa=fa+ca
  sp_c=sp/cement
  with st.spinner('Predicting...'):
    pred=model.predict(np.array([cement,slag,flyash,water,sp,ca,fa,age,c_w,f_c,c_a,c_aa,sp_c]).reshape(1,-1))
    time.sleep(1)
    answer="Concrete compressive strength is " + str(np.round(pred[0],2)) + " MPa, megapascals"
  st.success(answer)
