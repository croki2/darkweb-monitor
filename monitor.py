import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

# ===============================
# CONFIG
# ===============================
KEYWORDS = ["leak", "password", "exploit", "rce", "token", "apikey", "sql"]

results = []

def check_keywords(text, source, link):
    text_lower = text.lower()
    for kw in KEYWORDS:
        if kw in text_lower:
            results.append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "source": source,
                "keyword": kw,
                "link": link,
                "snippet": text[:120]
            })

# ===============================
# SOURCE 1: EXPLOIT-DB RSS
# ===============================
print("[+] Checking Exploit-DB RSS")
rss_url = "https://www.exploit-db.com/rss.xml"
rss = requests.get(rss_url).text
soup = BeautifulSoup(rss, "xml")

for item in soup.find_all("item")[:15]:
    title = item.title.text
    link = item.link.text
    check_keywords(title, "Exploit-DB", link)

# ===============================
# SOURCE 2: HACKER NEWS RSS
# ===============================
print("[+] Checking Hacker News RSS")
hn_url = "https://hnrss.org/frontpage"
hn = requests.get(hn_url).text
soup = BeautifulSoup(hn, "xml")

for item in soup.find_all("item")[:15]:
    title = item.title.text
    link = item.link.text
    check_keywords(title, "HackerNews", link)

# ===============================
# SOURCE 3: GITHUB SEARCH (HTML)
# ===============================
print("[+] Checking GitHub public search")
github_url = "https://github.com/search?q=password&type=repositories"
headers = {"User-Agent": "Mozilla/5.0"}
html = requests.get(github_url, headers=headers).text
soup = BeautifulSoup(html, "html.parser")

repos = soup.select("a.v-align-middle")[:10]

for repo in repos:
    name = repo.text.strip()
    link = "https://github.com" + repo["href"]
    check_keywords(name, "GitHub", link)

# ===============================
# SAVE RESULTS
# ===============================
df = pd.DataFrame(results)

if df.empty:
    print("[-] No alerts found")
else:
    df.to_csv("darkweb_alerts.csv", index=False)
    print("[+] Alerts saved to darkweb_alerts.csv")
    print(df.head())


# ===============================
# OPTIONAL: Send Email Alerts
# ===============================
import yagmail

if not df.empty:
    try:
        sender_email = "your_email@gmail.com"       # Replace with your email
        app_password = "your_app_password"         # Gmail app password
        receiver_email = "receiver_email@gmail.com" # Can be same as sender

        body = "Dark Web Monitoring Alerts:\n\n" + df.to_string(index=False)
        yag = yagmail.SMTP(sender_email, app_password)
        yag.send(to=receiver_email, subject="Dark Web Alerts", contents=body)
        print("[+] Email alert sent successfully")
    except Exception as e:
        print("[-] Failed to send email:", e)
