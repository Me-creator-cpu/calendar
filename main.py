import streamlit as st
import pandas as pd
import numpy as np

import requests
import json


class Reservation:
    def __init__(self,name,date,time,num_people):
        self.name  =name
        self.date = date
        self.time = time
        self.num_people = num_people

class ReservationApp:
    def __init__(self):
        self.reservations = []

    def add_reservation(self):
        name = st.text_input("Name", value="Test anon")
        date = st.date_input("Date")
        time = st.time_input("Time")
        num_people = int(st.number_input("Num people", min_value=int(1), value=int(1)))

        if st.button("Make reservation"):
            reservation = Reservation(name,date,time,num_people)
            self.reservations.append(reservation)

            st.write(f"Reservation created for {name} on {date} at {time} for {num_people} people.")
            st.balloons()

    def view_reservations(self):
        if not self.reservations:
            st.write(f"No reservation found")
            return
        for idx, res in enumerate(self.reservations, start=1):
            st.write(f"Reservation ID={idx} : {res.name} on {res.date} at {res.time} for {res.num_people} people.")

    def cancel_reservation(self):
        if not self.reservations:
            st.write(f"No reservation to cancel")
            return
        self.view_reservations()
        try:
            choice = int(st.number_input("Enter the reservation ID to cancel"))
            if 1 <= choice <= len(self.reservations):
                canceled = self.reservations.pop(choice - 1)
                st.write(f"Reservation canceled for {canceled.name} on {canceled.date} at {canceled.time} for {canceled.num_people} people.")
            else:
                st.write(f"Invalid choice, nothing to cancel")
        except ValueError:
            st.write(f"Invalid input, please enter a valid number")

    def run(self):
        #while True:
        st.write(f"Booking app")
        if st.button("Add reservation"):
            self.add_reservation()
        if st.button("View reservations"):
            self.view_reservations()
        if st.button("Cancel reservation"):
            self.cancel_reservation()
        if st.button("Exit app"):
            st.write(f"Exiting app, bye bye")
            #break

if st.button("Demo"):
    st.switch_page("/demo.py")

if  __name__ == "__main__":
    app = ReservationApp()
    app.run()

