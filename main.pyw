import pyautogui as autogui
import json
import tkinter as tk
import os
import subprocess
import platform


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

def getPlatfromCommand(x, zoomData):
    switcher = {
        'Windows':"%APPDATA%\Zoom\\bin\Zoom.exe --url=\"zoommtg://zoom.us/join?action=join&confno=" + zoomData.meetingId + "\"",
        'Linux':"zoom --url=\"zoommtg://zoom.us/join?action=join&confno=" + zoomData.meetingId + "\"",
    }
    val = switcher.get(x)
    if val == None:
        raise Exception("Unsupported platfrom!")
    return val

def joinMeeting(zoomData):
    subprocess.Popen(getPlatfromCommand(platform.system(), zoomData), shell=True)

    # enter passcode
    enter_meeting_passcode = autogui.locateCenterOnScreen('img/enter-meeting-passcode.png', confidence=0.7)
    while enter_meeting_passcode == None:
        enter_meeting_passcode = autogui.locateCenterOnScreen('img/enter-meeting-passcode.png', confidence=0.7)
    autogui.write(zoomData.pwd)


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
