import streamlit
streamlit.title('Zenas Athleisure')
import snowflake.connector
import pandas
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()



streamlit.title('Zena\'s Amazing Athleisure Catalog')
