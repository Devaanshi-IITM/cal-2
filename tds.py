import streamlit as st

def greatest_num(x,y,z):
    if x>= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

st.title("the greatest no. is")

x = st.number_input("x:")
y = st.number_input("y:")
z = st.number_input("z:")

if st.button("gretest number : "):
    great = greatest_num(x,y,z)
    st.write("The answer is:", great)
