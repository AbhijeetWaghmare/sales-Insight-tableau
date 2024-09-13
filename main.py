import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


st.set_page_config(page_title="Sales Insight with Streamlit", layout="wide")
st.title(":rainbow[Sales Insight] — :blue[ End-to-End Data Analysis Project]")
st.caption("#python#tableau#sql")
st.divider()

st.subheader("Abhijeet Waghmare :grey[python developer, data analyst]")

html_code = """
        
        <a href="https://www.linkedin.com/in/abhijeet-waghmare-6268892a9" target="_blank">
            <img src="https://img.icons8.com/?size=100&id=xuvGCOXi8Wyg&format=png&color=000000" alt="LinkedIn" width="40" height="40">
        </a>
        |
        <a href="mailto:abhijeetwaghmare2000@gmail.com">
            <img src="https://img.icons8.com/?size=100&id=P7UIlhbpWzZm&format=png&color=000000" alt="Gmail" width="40" height="40">
            
        </a>
        """
# Display the HTML in Streamlit
st.markdown(html_code, unsafe_allow_html=True)
st.divider()
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Problem Statement", "Aim Grids", "Data Discovery", "Observations","Tableau Dashboard"])


with tab1:
    st.header("Problem Statement")
    st.write(
        """
         ### AtliQ Hardware is a company that supplies hardware peripherals to different clients, such as Nomad stores, Excel stores, and SURGE stores. These are all the clients, and this is a hardware company that will supply computers and other peripheral networking equipment to them. They have a head office in Delhi, India, and they have regional offices in different states of India.

        #### Bhavin Patel is the sales director of this company, and he's managing the business from the head office, but they have regional managers per state, per region, or per district. And what's happening with this company is that sales are declining, and Bhavin Patel, as a sales director, is having a lot of struggle tracking where the business is failing (when the business is smaller, let's say you have 10 employees; a small business you can manage, but when your business is bigger and you have multiple offices, it's actually hard to manage). He is not getting the right picture (and that's when data analysis can help you).

        #### So for Bhavin Patel, when he talks with the regional managers or regarding the business in their areas, the managers have a tendency to paint a rosy picture. So sometimes, you know, they don't lie, but they put sugar coating around the facts, and as a sales director, Bhavin doesn't have any idea what actually happens at ground level; you know, he doesn't have data insights. So that's the challenge that he goes through, and when he calls these regional managers, they will give him these big Excel files, you know, and these Excel files, as humans, we're not good at consuming so many numbers. You know we want simple insights, so he's frustrated because these managers are giving him so many Excel files, and he's like, Why the hell are you giving me 69 Excel files? I don't understand; I have to merge those files and get the insights myself, and it's very tedious, and Excel is kind of a boring tool.

        #### So what he wants is some simple answers. You know, he wants to know: What are my top five customers? What are my two weakest regions where sales are declining? What is my aggregate revenue for the last 365 days? It is called year-to-date revenue. All these simple answers are hard to get, but there is a saying called A picture is worth a thousand words.
    """
    )


with tab2:
    st.header("Aim Grids")
    st.markdown(
        """
                
### Aim's grid includes four components: Purpose (project goals), Stakeholders (involved teams), End Result (desired outcomes), and Success Criteria (measures of success).

##  Purpose (project goals)
- To unlock sales insights thhat are not visible  before for sales team for decision support & automate them to reduced manual time spent in data gathering.


##  Stakeholders (involved teams)
- sales Director
- Marketing Team
- Custome Service Team
- Data % Analysis Team
- IT

## End Result (desired outcomes),
- An automated dashboard providing quick & latest sales insight in order to support data driven decision making.

##  Success Criteria (measures of success)
- Dashboard(s) uncovering sales order insights with latest data available
- Sales team able to take better decisions & prove 10% cost savings of total spend
- Sales analyst stop data gathering manually in order to save 20% of their business time and reinvest it value added activity
"""
    )


with tab3:
    st.header("Data Discovery")
    st.markdown(
        "The sales management system stores data in a MySQL database with the help of data engineers. Data will be uploaded to the data warehouse (ETL), and now we can retrieve data from the warehouse with the help of data engineers. After getting access we will export data to csv files. And use python for data processing."
    )
    customers = pd.read_csv("./dataset/customers.csv")
    markets = pd.read_csv("./dataset/markets.csv")
    products = pd.read_csv("./dataset/products.csv")
    date = pd.read_csv("./dataset/date.csv")
    transactions = pd.read_csv("./dataset/transactions.csv")

    st.code("import pandas as pd")
    st.code("""customers = pd.read_csv("dataset/customers.csv")""", language="python")
    st.code("""markets = pd.read_csv("dataset/markets.csv")""", language="python")
    st.code("""products = pd.read_csv("dataset/products.csv")""", language="python")
    st.code("""date = pd.read_csv("dataset/date.csv")""", language="python")
    st.code(
        """transactions = pd.read_csv("dataset/transactions.csv")""", language="python"
    )

    # customers
    st.code("""customers""")
    st.dataframe(customers)

    st.code("""customers.shape""")
    customers_shape = customers.shape
    st.write(customers_shape)

    st.code("""customers["customer_type"].unique()""")
    distinct_customer_type = customers["customer_type"].unique()
    st.write(distinct_customer_type)

    # markets
    st.code("""markets""")
    st.dataframe(markets)

    st.code("""markets["zone"].unique()""")
    distinct_zone = markets["zone"].unique()
    st.write(distinct_zone)

    st.code("""markets["markets_code"].value_counts().sum()""")
    distinct_markets_code = markets["markets_code"].value_counts().sum()
    st.write(distinct_markets_code)

    st.code("""markets.shape""")
    markets_shape = markets.shape
    st.write(markets_shape)

    # products
    st.code("""products""")
    st.dataframe(products)

    st.code("""products["product_type"].unique()""")
    distinct_products_type = products["product_type"].unique()
    st.write(distinct_products_type)

    st.code("""products.shape""")
    products_shape = products.shape
    st.write(products_shape)

    # date
    st.code("""date""")
    st.dataframe(date)

    st.code("""date.shape""")
    date_shape = date.shape
    st.write(date_shape)

    st.code("""date["year"].unique()""")
    distinct_year = date["year"].unique()
    st.write(distinct_year)

    # transactions
    st.code("""transactions""")
    st.dataframe(transactions)

    st.code("""transactions.shape""")
    transactions_shape = transactions.shape
    st.write(transactions_shape)

    st.code("""transactions[transactions['currency']=="USD"]""")
    transactions_with_usd = transactions[transactions["currency"] == "USD"]
    st.write(transactions_with_usd)


with tab4:
    st.header("Observations")
    st.markdown(
        """
                - Customer table = 38 customer/clients with 2 distinct type "E-commerence" and 'Brick & Mortar'
- Markets table = sales are across 3-4 zone and 17 (states/city)
- Product table =  total 279 product with 2 distinct type 'own' and ' distribution'
- date table = record count 1126 for year 2017 to 2020
- transactions table = actually table gives revenue


There some value/ entries that should be clean.
In Tableau  we will do data clean and data visualization
                """
    )


with tab5:
    st.header("Tableau Dashboard")
    st.caption("select desktop layout to see entire dashboard")
    st.page_link("https://public.tableau.com/app/profile/abhijeet.waghmare/viz/salesinsight_17235689843210/Dashboard1",label="Dashboard Link")
    dashboard = """<div> <div class='tableauPlaceholder' id='viz1725455194509' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;sa&#47;salesinsight_17235689843210&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='salesinsight_17235689843210&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;sa&#47;salesinsight_17235689843210&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>  </div>              <script type='text/javascript'>                    var divElement = document.getElementById('viz1725455194509');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1500px';vizElement.style.height='927px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1500px';vizElement.style.height='927px';} else { vizElement.style.width='100%';vizElement.style.height='1777px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(dashboard, height=1200, scrolling=True)

st.page_link("https://colab.research.google.com/drive/1XubprqqUPE4erxcoE4PO3B02eDYZ5W3x?usp=sharing", label="colab link")


footer_html = """<div style='text-align: center;'>
  <p>Developed with ❤️ by Abhijeet Waghmare</p>
</div>"""
st.markdown(footer_html, unsafe_allow_html=True)