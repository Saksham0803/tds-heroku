import streamlit as st
def main():
  st.title("Subtraction of 2 numbers")
  html_temp = """
  <div style="background-color:tomato;padding:10px">
  <h2 style="color:white;text-align:center;">Streamlit subtraction App <h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  number1 = st.number_input("Enter first number",min_value=-100000000000000000000.0,max_value=1000000000000.0)
  number = st.number_input("Enter second number",min_value=-100000000000000000000.0,max_value=1000000000000.0)
  result = 0
  if st.button("subtract"):
    result = number1 - number
  st.success(f"The difference of 2 numbers is {result}")
  if st.button("About"):
    st.text("Lets Learn")
    st.text("Built with Streamlit")
if __name__ == "__main__":
    main()