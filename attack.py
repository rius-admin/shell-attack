#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Script by Mr.Rius

import requests
import os

def Space(j):
    i = 0
    while i <= j:
        print(" ", end="")
        i += 1
    print("")

print("===================================================================== ")
print("          ")
print("          ")
print("   ╔══╗╔╗╔╗╔═╗╔╗─╔╗     ╔══╗╔══╗╔══╗╔══╗╔═╗╔╦╗ ") 
print("   ╚╗╗║║╚╝║║╦╝║║─║║     ║╔╗║╚╗╔╝╚╗╔╝║╔╗║║╔╝║╔╝ ")
print("   ╔╩╝║║╔╗║║╩╗║╚╗║╚╗   ║╠╣║─║║──║║─║╠╣║║╚╗║╚╗ ")
print("   ╚══╝╚╝╚╝╚═╝╚═╝╚═╝   ╚╝╚╝─╚╝──╚╝─╚╝╚╝╚═╝╚╩╝ ") 
print("   ─────────────────    ────────────────────── ")
print("          ")
print("          ")
print("===================================================================== ")

def findAdmin():
    """Brute-force scanner yang cepat & stabil"""
    try:
        with open("shell.txt", "r") as f:
            paths = f.read().splitlines()
    except FileNotFoundError:
        print("[!] File shell.txt tidak ditemukan.")
        return
    
    link = input("contoh ; target.co  \n bot-robots(scan) : ").strip()
    print("\n\nbot-robots(scan) : \n")

    if not link.startswith(("http://", "https://")):
        link = "http://" + link

    with requests.Session() as session:  # Gunakan session untuk mempercepat koneksi
        for sub_link in paths:
            req_link = f"{link}/{sub_link}"
            try:
                response = session.get(req_link, timeout=3)  # Timeout lebih cepat (3 detik)
                if response.status_code == 200:
                    print(f"hasil  => {req_link} (Status Code: {response.status_code})")
            except requests.exceptions.RequestException:
                continue  # Lewati jika error, lanjut ke URL berikutnya

def Credit():
    Space(9)
    print("  ------------------------")
    Space(9)
    print("[•] Cyber Sederhana Team [•]")
    Space(9)
    print("  ------------------------")
    Space(9)
    print(" ")

Credit()
findAdmin()
