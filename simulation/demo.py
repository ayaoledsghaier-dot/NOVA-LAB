
from pathlib import Path
from datetime import datetime
import json

# ==========================================
# EDUCATIONAL MALWARE SIMULATION
# Safe project for cybersecurity students
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
LAB_DIR = BASE_DIR / "simulation_results"
LOG_FILE = LAB_DIR / "simulation_log.txt"
REPORT_FILE = LAB_DIR / "report.json"


def create_lab():
    """Create a dedicated folder for harmless test files."""
    LAB_DIR.mkdir(exist_ok=True)

    print("[+] Laboratory folder created")


def simulate_file_reception():
    print("\n[PHASE 1] FILE RECEPTION")
    print("[+] A simulated suspicious file was received")
    print("[+] No real file was downloaded")


def simulate_inspection():
    print("\n[PHASE 2] FILE INSPECTION")
    print("[+] File type: Educational simulation")
    print("[+] Source code inspection: completed")
    print("[+] No executable malware detected")


def simulate_fake_activity():
    print("\n[PHASE 3] SIMULATED ACTIVITY")

    fake_data = {
        "username": "test_user",
        "device": "LAB-PC",
        "date": datetime.now().isoformat(),
        "information": "FICTITIOUS DATA - NOT REAL"
    }

    test_file = LAB_DIR / "test_data.json"

    with test_file.open("w", encoding="utf-8") as file:
        json.dump(fake_data, file, indent=4)

    print("[+] Fictitious test data created")
    print("[+] File location:", test_file)


def simulate_detection():
    print("\n[PHASE 4] DETECTION")

    print("[+] Test file detected in laboratory folder")
    print("[+] No personal files were accessed")
    print("[+] No network communication occurred")
    print("[+] No system settings were changed")


def save_report():
    print("\n[PHASE 5] REPORT")

    report = {
        "project": "Educational Malware Simulation",
        "date": datetime.now().isoformat(),
        "result": "Completed",
        "real_malware": False,
        "data_theft": False,
        "network_connection": False,
        "system_modification": False
    }

    with REPORT_FILE.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    with LOG_FILE.open("w", encoding="utf-8") as file:
        file.write("EDUCATIONAL SIMULATION COMPLETED\n")
        file.write("No real malware was executed.\n")
        file.write("No personal data was collected.\n")

    print("[+] Report saved:", REPORT_FILE)
    print("[+] Log saved:", LOG_FILE)


def main():
    print("=" * 45)
    print("   EDUCATIONAL MALWARE SIMULATION")
    print("=" * 45)

    create_lab()
    simulate_file_reception()
    simulate_inspection()
    simulate_fake_activity()
    simulate_detection()
    save_report()

    print("\n[+] SIMULATION COMPLETED SUCCESSFULLY")
    print("[+] Your computer was not attacked.")
    print("=" * 45)


if __name__ == "__main__":
    main()



