# 🚀 Network Ping Tool

**Ping your network like a pro – now with multi-host support and detailed statistics!**

A cross-platform Python tool to check connectivity, measure latency, and diagnose network issues. Ideal for sysadmins, developers, or anyone who wants full control over network monitoring.

---

## ⚡ Features

- Ping **multiple IPs/domains** at once  
- Display **packet loss and latency statistics**  
- Save all results automatically to a **log file**  
- Works on **Windows, Linux, and MacOS**  
- Clean, user-friendly command-line interface  

---

## 🛠 How to Use

1. **Clone the repository**  
```bash
git clone https://github.com/briangodz/network-ping-tool.git
```
2. **Run the Tool**
```bash
cd network-ping-tool
python ping_tool.py
```
3. **Follow prompts:**
- Enter IPs/domains separated by commas (e.g., `8.8.8.8, google.com`)
- Enter number of ping packets per host (default 4)
4. **Check results:**
  - Results appear in terminal
  - Full log saved in `ping_results_TIMESTAMP.txt` (example: `ping_results_20250911_003015.txt`)
