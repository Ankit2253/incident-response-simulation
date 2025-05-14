# Incident Response Simulation Lab

This repository contains all artifacts for a hands-on IR lab:

- **lab-setup/**: Scripts and configs to prepare victim & attacker.
- **malware/**: Sample dropper and payload.
- **splunk/**: SPL queries to detect IOCs.
- **ioc-extraction/**: Python script to automate VT lookups.
- **reports/**: Template incident report in Markdown.

## Prerequisites
- Windows 10 VM (victim) with Sysmon & PowerShell
- Kali Linux (attacker) with Gophish
- Splunk Free or Wazuh instance

## Lab Workflow
1. Launch Gophish (`lab-setup/gophish_campaign_setup.sh`).
2. Send phishing emails with link to `malware/dropper.ps1`.
3. Enable Sysmon (`lab-setup/sysmon-config.xml`).
4. Execute dropper on victim.
5. Run SPL queries (`splunk/queries.spl`).
6. Extract IOCs via `python ioc-extraction/vt_lookup.py`.
7. Document findings in `reports/incident_report.md`.

## Usage
```bash
# Prepare lab
bash lab-setup/gophish_campaign_setup.sh
# After executing dropper on victim, analyze logs:
# In Splunk:
| . import queries.spl
# Extract IOCs:
python ioc-extraction/vt_lookup.py --hash 1234abcd...
