import streamlit as st
from streamlit.runtime.state import SessionState, session_state
import scrython
import random

# draw playerboxes

st.title("MTG Commpanion", text_alignment="center")

players = st.number_input("How many players?", min_value=0, step=1)
boxes = []
commander_damage = []

for i in range(players):
    cmdsidebar = st.sidebar.number_input(
        f"Player {i + 1}",
        min_value=0,
        value=0,
        step=1,  # TODO: implement dynamic tracking of commander damage, while still allowing for users to gain and lose life in playerbox
    )
    commander_damage.append(cmdsidebar)

    playerbox = st.number_input(
        f"Player {i + 1}",  # TODO: increase width over playerboxes for mobile, maybe tile layout?
        min_value=0,
        value=40,
        step=1,
    )
    boxes.append(playerbox)


# high roll on sidebar
if st.sidebar.button("High Roll", type="secondary", width="stretch"):
    for i in range(players):
        st.sidebar.markdown(
            f"Player {i + 1}: {random.randint(0, 20)}", text_alignment="center"
        )
st.sidebar.button("Reset", type="primary", width="stretch")


# card Lookup via scrython
card = st.text_input("Look up a card by searching below")


def get_card_by_name(name: str):
    card1 = scrython.cards.Named(fuzzy=name, rate_limit=False)
    st.write(card1.name)
    # st.write(card1.mana_cost)
    st.write(card1.type_line)
    # st.write(card1.oracle_text)
    st.image(card1.image_uris["normal"])


# fix for error when loading due to no value
if card.strip():
    get_card_by_name(card)
