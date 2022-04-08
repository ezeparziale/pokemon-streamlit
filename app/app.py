from pyparsing import col
import streamlit as st
import json

st.set_page_config(page_title="Pokemon", page_icon="./app/static/img/favicon.ico")

bootstrap = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
"""

css = """
    <link rel="stylesheet" href="./app/static/css/style.css">
"""

st.markdown(bootstrap, unsafe_allow_html=True)

with open("./app/static/css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/International_Pok%C3%A9mon_logo.svg/2560px-International_Pok%C3%A9mon_logo.svg.png")

@st.cache
def load_data():
    f = open("app/data/data.json")
    return json.load(f)

@st.cache
def load_types(data):
    types = []
    for key, value in data.items():
        for x in value["types"]:
            types.append(x)
    return set(types)

data = load_data()

types = load_types(data)

with st.sidebar:
    options = st.multiselect(
        'Types',
        types,
        types)

col1, col2, col3 = st.columns(3)

def button(text):
    button = f"""
    <button type="button" class="btn btn-{text}">{text.capitalize()}</button>"""
    return button

def print_data(item):
    title = f"""<div class='col text-center'><h2>{item["name"].capitalize()}</h2></div>
    """
    st.markdown(title, unsafe_allow_html=True)
    st.image(item["img"])
    html = "<div class='col text-center'>"
    for x in item["types"]:
        html += button(x)
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)
    st.write("")


col_num = 1

for key, value in data.items():
    with st.container():
        if any(item in value["types"] for item in options):
            if col_num==1:
                with col1:
                    print_data(value)
            elif col_num==2:
                with col2:
                    print_data(value)
            elif col_num==3:
                with col3:
                    print_data(value)


            if col_num == 3:
                col_num = 1
            else:
                col_num += 1
