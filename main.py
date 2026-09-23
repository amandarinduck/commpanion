import streamlit as st
import scrython

st.title("MTG Commpanion: Life Tracker and Card Lookup", text_alignment="center")

players = st.number_input("How many players?", min_value=0, step=1)
boxes = []
for i in range(players):
    playerbox = st.number_input(f"Player {i + 1}", min_value=0, value=40, step=1)
    boxes.append(playerbox)


if st.button("Life Totals"):
    st.write(box for box in boxes)

card = st.text_input("look up a card here")


def get_card_by_name(name: str):
    card1 = scrython.cards.Named(fuzzy=name, rate_limit=False)
    st.write(card1.name)
    st.write(card1.mana_cost)
    st.write(card1.type_line)
    st.write(card1.oracle_text)
    st.image(card1.image_uris["normal"])


get_card_by_name(card)
