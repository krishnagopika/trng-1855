import streamlit as st
import pandas as pd


st.title('Streamlit Demo')

# Magic
"""

## Header in MD

"""

# write

st.write("Sample text")

df = pd.DataFrame({

    'coloumn 1': [1,2,3],
    'coloumn 2':[3,4,5]
    
})

#df

st.write(df)


# widgets
rating = st.slider("Rating", min_value=0, max_value=10)

rating


if st.button("click me"):
    st.write("clicked")




# Layout
st.sidebar.text_input("Full Name", key="name")

# Session state
st.session_state.name

st.image("trng-1855/trng-git-repo/trng-1855/week-7/phantom_galaxy.jpg")
