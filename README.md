# PyPhisherSim

**PyPhisherSim** is an educational phishing simulation tool designed for cybersecurity awareness training and ethical use only. This tool allows you to simulate phishing pages for educational testing in safe, controlled environments such as localhost or via a secure Cloudflare tunnel.

> ⚠️ **DISCLAIMER**  
> This tool is for **educational and ethical use only**.  
> Unauthorized use of this tool to target individuals or systems without consent is **strictly prohibited** and may be **illegal**.  
> Use this tool only for awareness training, penetration testing (with permission), and security education.

---

## 🛠️ Installation

Follow the steps below to install and run PyPhisherSim on your Linux system.

### 1. Update system packages
```bash
sudo apt update
2. Install Python (if not already installed)
sudo apt install python3 python3-pip -y

3. Clone the repository
git clone https://github.com/yourusername/pyphishersim.git
cd pyphishersim

4. Install required Python packages
pip3 install -r requirements.txt

📂 Template Selection

PyPhisherSim currently includes 2 phishing templates, with more coming in future updates.

Available Templates:

Login Page Clone – A basic clone of a login screen for training purposes.

Fake Update Page – Simulates a software update prompt.

To select a template, you will be prompted when running the script.

🚀 Running the Tool

You can run the tool either on:

Localhost – for internal testing.

Cloudflare Tunnel – to simulate an external-accessible environment.

Option 1: Run on Localhost
python3 pyphishersim.py --localhost

Option 2: Run via Cloudflare Tunnel

First, install Cloudflared:

sudo apt install cloudflared


Then run the tool with:

python3 pyphishersim.py --cloudflare


The terminal will provide a public URL via Cloudflare for testing.

🔒 Important Notes

This tool is intended for demo, testing, and training purposes only.

Always ensure you have authorization before conducting any kind of phishing simulation.

Logs and submissions can be monitored in the logs/ directory.

📬 Feedback & Contributions

We welcome contributions and suggestions!
Submit a pull request or open an issue to report bugs or suggest new templates.

📅 Coming Soon

✅ More templates

✅ Dashboard to view submissions

✅ Email phishing simulation (internal use)
