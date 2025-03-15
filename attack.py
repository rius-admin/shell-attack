#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Script by Mr.Rius

import requests
import os
import threading
import queue
from urllib.parse import urljoin

# Bersihkan layar saat program dijalankan
os.system('cls' if os.name == 'nt' else 'clear')

def Space(j):
    i = 0
    while i <= j:
        print(" ", end="")
        i += 1
    print("")

# Menampilkan tampilan awal dengan spasi kosong
print("\n" * 1)  # Menambah 1 baris kosong agar terminal terlihat lebih rapi

print("===================================================================== ")
print("          ")
print("          ")
print("             ╔══╗╔╗╔╗╔═╗╔╗─╔╗     ╔══╗╔══╗╔══╗╔══╗╔═╗╔╦╗ ") 
print("             ╚╗╗║║╚╝║║╦╝║║─║║     ║╔╗║╚╗╔╝╚╗╔╝║╔╗║║╔╝║╔╝ ")
print("             ╔╩╝║║╔╗║║╩╗║╚╗║╚╗    ║╠╣║─║║──║║─║╠╣║║╚╗║╚╗ ")
print("             ╚══╝╚╝╚╝╚═╝╚═╝╚═╝    ╚╝╚╝─╚╝──╚╝─╚╝╚╝╚═╝╚╩╝ ") 
print("             ─────────────────    ────────────────────── ")
print("          ")
print("          ")
print("===================================================================== ")

# Fungsi utama untuk brute-force
def brute_force(session, base_url, q):
    """Brute-force dengan multi-threading kecepatan tinggi"""
    while not q.empty():
        sub_link = q.get()
        req_link = urljoin(base_url, sub_link)  # Pastikan path tetap valid
        try:
            response = session.get(req_link, timeout=0.8)  # Timeout lebih cepat (0.8 detik)
            if response.status_code == 200:
                print(f"✔ Hasil ditemukan => {req_link} (Status Code: {response.status_code})")
        except requests.exceptions.RequestException:
            pass  # Lewati error agar tetap berjalan stabil
        q.task_done()

def findAdmin():
    """Brute-force scanner tercepat"""
    try:
        with open("shell.txt", "r") as f:
            paths = f.read().splitlines()
    except FileNotFoundError:
        print("[!] yha anda kurang beruntung^_-")
        return
    
    link = input("       contoh ; target.co \n bot-robots(scan) > ").strip()
    print("        \n\n bot-robots(scan) : \n")

    if not link.startswith(("http://", "https://")):
        link = "http://" + link

    if not link.endswith("/"):
        link += "/"  # Pastikan URL diakhiri "/"

    q = queue.Queue()
    for path in paths:
        q.put(path)

    with requests.Session() as session:
        threads = []
        max_threads = 50  # Pakai 50 thread agar brute sangat cepat

        for _ in range(max_threads):
            t = threading.Thread(target=brute_force, args=(session, link, q))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()  # Menunggu semua thread selesai

def Credit():
    Space(9)
    print("       ------------------------")
    Space(9)
    print("    [•] Cyber Sederhana Team [•]")
    Space(9)
    print("       ------------------------")
    Space(9)
    print(" ")

Credit()
findAdmin()
