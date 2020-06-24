# -*- coding: utf-8 -*-
import requests
import json
import time
import os
from threading import Thread, Timer
import subprocess

SESAME_ID = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxx"
KENCHI_FLAG = False
CELL_DEVICE_IP = "192.168.11.34"


def detection():
    cmd = "sudo arp-scan -l --interface en0 | grep " + CELL_DEVICE_IP
    process = (
        subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    ).decode("utf-8")
    if process == "":
        print("deviceが検出されませんでした。")
        return False
    else:
        print("deviceが検出されました。")
        return True


def open_sesame():
    url_control = "https://api.candyhouse.co/public/sesame/" + SESAME_ID
    head_control = {"Authorization": API_KEY, "Content-type": "application/json"}
    response_control = requests.get(url_control, headers=head_control)
    time.sleep(1)
    payload_control = {"command": "unlock"}
    response_control = requests.post(
        url_control, headers=head_control, data=json.dumps(payload_control)
    )
    print(response_control.text)


if __name__ == "__main__":

    detection_count = 0
    un_detection_count = 1000
    while True:
        print("Deviceを検出中です")
        if detection() == True:
            detection_count = detection_count + 1
            un_detection_count = 0
        else:
            detection_count = 0
            un_detection_count = un_detection_count + 1
        print("検出回数：", detection_count)
        print("非検出回数：", un_detection_count)
        if detection_count == 1:
            open_sesame()
