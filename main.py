import streamlit as st

st.title("MTG Commander Life Tracker", text_alignment="center")

players = st.number_input("How many players?", min_value=0, step=1)
boxes = []
for i in range(players):
    playerbox = st.number_input(f"Player {i + 1}", min_value=0, value=40, step=1)
    boxes.append(playerbox)


if st.button("Life Totals"):
    st.write(box for box in boxes)
