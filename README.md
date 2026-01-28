# Dark Web & Threat Intelligence Monitoring Tool

## Overview
This Python-based tool automates **threat intelligence monitoring** by collecting data from **public security sources** and detecting potential **exploits, data leaks, and exposed credentials**.  
It generates structured alerts in CSV format, can optionally send **email notifications**, and includes an **interactive dashboard** for visualization.

This project is **safe, fully laptop-friendly**, and designed for cybersecurity enthusiasts, SOC analysts, or anyone looking to demonstrate **real-world threat intelligence skills**.

---

## Features
- Collects data from **3 public sources**:
  1. **Exploit-DB RSS feed** – lists known exploits
  2. **Hacker News RSS feed** – tracks security news and leaks
  3. **GitHub public repositories** – detects keywords in repo names
- Detects **keywords**: `password`, `API_KEY`, `leak`, `exploit`, `RCE`, `SQLi`, `admin`, `token`
- Generates **structured alerts**:
  - CSV file (`darkweb_alerts.csv`) with:
    - Date/Time
    - Source
    - Keyword
    - Link
    - Snippet/context
- Optional **email notifications** for instant alerts
- Optional **interactive dashboard** using Streamlit
- Fully documented and ready for **GitHub portfolio**

---

## Installation
1. Clone the repository:

```bash
git clone https://github.com/YourUsername/darkweb-monitor.git
cd darkweb-monitor
