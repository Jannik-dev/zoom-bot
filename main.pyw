from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pyautogui as py
import json
import tkinter as tk
import os


class ZoomData:
    def __init__(self, meetingId, abbreviation, professor, pwd):
        self.meetingId = meetingId
        self.pwd = pwd
        self.abbreviation = abbreviation
        self.professor = professor


def getZoomDataEntries():
    with open(os.path.abspath('meeting-data.json')) as f:
        content = json.load(f)["zoom_data"]
        zoomData = []
        for item in content:
            zoomData.append(ZoomData(
                item["meeting_id"], item["abbreviation"], item["professor"], item["password"]))
    return zoomData


def createCourseTitle(course):
    return course.abbreviation + " by " + course.professor


def joinMeeting(zoomData):
    driver = webdriver.Edge(service=Service(
        EdgeChromiumDriverManager().install()))
    driver.get('https://zoom.us/join')

    # to let the webpage open completely
    cookies = py.locateCenterOnScreen(
        'img/decline-cookies.png', confidence=0.7)
    while cookies == None:
        cookies = py.locateCenterOnScreen(
            'img/decline-cookies.png', confidence=0.7)

    driver.find_element(
        By.XPATH, "//button[@id='onetrust-reject-all-handler']").click()  # decline cookies
    driver.find_element(
        By.XPATH, "//input[@id='join-confno']").send_keys(zoomData.meetingId)
    driver.find_element(By.XPATH, "//a[@id='btnSubmit']").click()

    # open zoom
    open_meeting = py.locateCenterOnScreen('img/zoom-open.png', confidence=0.7)
    while open_meeting == None:
        open_meeting = py.locateCenterOnScreen(
            'img/zoom-open.png', confidence=0.7)
    py.moveTo(open_meeting)
    py.click()

    # enter passcode
    enter_meeting_passcode = py.locateCenterOnScreen(
        'img/enter-meeting-passcode.png', confidence=0.7)
    while enter_meeting_passcode == None:
        enter_meeting_passcode = py.locateCenterOnScreen(
            'img/enter-meeting-passcode.png', confidence=0.7)
    py.write(zoomData.pwd)


zoomDataEntries = getZoomDataEntries()

entries = {}
for entry in zoomDataEntries:
    entries[createCourseTitle(entry)] = entry

# ui for selecting course
window = tk.Tk()
window.title('Select a meeting')

window.geometry('1000x800')

selectedVal = tk.StringVar()


def print_selection():
    key = lb.get(lb.curselection())
    joinMeeting(entries[key])


titles = list(entries.keys())

meetingsList = tk.StringVar()
meetingsList.set(titles)

lb = tk.Listbox(window, listvariable=meetingsList, width=80, height=25)
lb.pack()

b1 = tk.Button(window, text='Enter meeting data',
               width=15, height=2, command=print_selection)
b1.pack()

window.mainloop()
