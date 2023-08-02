import streamlit
import snowflake.connector
import pandas
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()



streamlit.title('Zena\'s Amazing Athleisure Catalog')

my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

df = pandas.DataFrame(my_catalog)



# put the first column into a list
color_list = df[0].values.tolist() 
print(color_list)

option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))

# We'll build the image caption now, since we can 
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'

# use the option selected to go back and get all the info from the database

my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '" + option + "';") df2 = my_cur.fetchone()


