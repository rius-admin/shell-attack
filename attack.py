#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Script by Mr.Rius (Diperbarui)

import requests
import os
import threading
import queue
import time
import random
from urllib.parse import urljoin

# Bersihkan layar saat program dijalankan
os.system('cls' if os.name == 'nt' else 'clear')

def Space(j):
    print(" " * j)

# Menampilkan tampilan awal
print("\n" * 1)  
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
    """Brute-force dengan kecepatan yang lebih stabil"""
    while not q.empty():
        sub_link = q.get()
        req_link = urljoin(base_url, sub_link)  # Pastikan path tetap valid
        try:
            response = session.get(req_link, timeout=2)  # Timeout lebih panjang untuk stabilitas
            if response.status_code == 200:
                print(f"✔ Hasil ditemukan => {req_link} (Status Code: {response.status_code})")
            else:
                print(f"[-] Coba: {req_link} (Status: {response.status_code})")
        except requests.exceptions.RequestException:
            print(f"[!] Error mengakses {req_link}")  
        finally:
            time.sleep(random.uniform(0.3, 0.8))  # Tambahkan delay agar tidak terlalu cepat
        q.task_done()

def findAdmin():
    """Brute-force scanner dengan pengaturan kecepatan lebih stabil"""
    try:
        with open("shell.txt", "r") as f:
            paths = f.read().splitlines()
    except FileNotFoundError:
        print("[!] yha anda kurang beruntung cuk ^_-")
        return
    
    link = input("       contoh ; target.co \n bot-robots(scan) > ").strip()
    print(" ") 
    print("        \n\n    bot-robots(scan) : \n")

    if not link.startswith(("http://", "https://")):
        link = "http://" + link

    if not link.endswith("/"):
        link += "/"  # Pastikan URL diakhiri "/"

    q = queue.Queue()
    for path in paths:
        q.put(path)

    with requests.Session() as session:
        threads = []
        max_threads = 15  # Mengurangi jumlah thread agar tidak terlalu cepat

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
