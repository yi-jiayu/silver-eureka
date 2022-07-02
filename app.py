import pandas as pd
import streamlit as st
import spacy

nlp = spacy.load("en_core_web_lg")

gics = pd.read_csv("gics.csv")
subindustries = pd.DataFrame(data={"name": gics["SubIndustry"].unique()})
subindustries["nlp"] = subindustries["name"].apply(lambda x: nlp(x))

st.write("# Industry search")

query = st.text_input("Search industries")

if query:
    subindustries["similarity"] = subindustries["nlp"].apply(
        lambda x: x.similarity(nlp(query))
    )
else:
    subindustries["similarity"] = 0

st.table(
    subindustries[["name", "similarity"]].sort_values("similarity", ascending=False)
)
