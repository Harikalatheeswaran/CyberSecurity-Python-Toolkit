# 🧰 Socket & ICMP Tools - Week 1 Pentesting Toolkit

Welcome to **Week 1** of my offensive security mentorship journey. This repository contains Python-based networking tools developed using `socket` and `scapy` as part of foundational training.

---

## 📂 Repository Structure
```
Week-01_Socket_ICMP_Tools/
├── Week1_Notebook.ipynb          # Jupyter notebook with lessons, code, and explanations
├── tcp_server.py                 # Simple TCP echo server
├── tcp_client.py                 # Simple TCP client
├── icmp_ping.py                  # ICMP packet crafting & pinging via Scapy
├── base64_decoder.py             # Python script to decode Base64 encoded challenge string
├── Linux_Cheat_Sheet.md         # Personal Linux command reference
└── README.md                     # You’re reading it!
```

---

## 🧪 Tools & Concepts Covered
- **Python Sockets:** Basic TCP client-server communication
- **Scapy:** Crafting and sending ICMP packets (ping)
- **Base64 Decoding:** Simple encoding challenge solved in Python
- **Linux CLI:** Basic navigation, system commands, and package handling on Kali Linux

---

## 🚀 How to Run
Ensure you have Python 3 and necessary libraries installed.
```bash
pip install scapy
```

Then execute any script, for example:
```bash
python tcp_server.py
python tcp_client.py
```

Or run the entire interactive experience inside Jupyter:
```bash
jupyter notebook Week1_Notebook.ipynb
```

### Stay Curious!
