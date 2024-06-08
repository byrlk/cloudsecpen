# CloudSecPen

CloudSecPen is a security penetration testing framework designed for both Azure and AWS environments. This tool provides a user-friendly menu interface to facilitate the enumeration, information gathering, lateral movement, privilege escalation, exploitation, and credential attacks on cloud infrastructures. It integrates multiple third-party tools, allowing security professionals to perform in-depth security assessments with ease.

## Features

### Enumeration
- **Email Enumeration**
  - o365creeper: [GitHub](https://github.com/LMGsec/o365creeper)
  - Office 365 User Enumeration: [GitHub](https://github.com/gremwell/o365enum)

- **Cloud Resource Enumeration**
  - CloudBrute: [GitHub](https://github.com/0xsha/CloudBrute)
  - cloud_enum: [GitHub](https://github.com/initstring/cloud_enum)
  - ScoutSuite: [GitHub](https://github.com/nccgroup/ScoutSuite)
  - BlobHunter: [GitHub](https://github.com/cyberark/blobhunter)
  - CloudFox: [GitHub](https://github.com/BishopFox/cloudfox)

### Information Gathering
- **Azure AD Interaction and Assessment**
  - ROADtools: [GitHub](https://github.com/dirkjanm/ROADtools)

### Lateral Movement
- **Azure Object Graphing**
  - Stormspotter: [GitHub](https://github.com/Azure/Stormspotter)

- **Privilege Entity Discovery**
  - SkyArk: [GitHub](https://github.com/cyberark/SkyArk)

- **Vulnerability Scanning**
  - omigood: [GitHub](https://github.com/marcosimioni/omigood)

### Privilege Escalation
- **Privilege Escalation Tools**
  - AzureADLateralMovement: [GitHub](https://github.com/talmaor/AzureADLateralMovement)

### Exploitation
- **Script-Based Exploitation**
  - MicroBurst: [GitHub](https://github.com/NetSPI/MicroBurst)

- **Exploitation via Teams**
  - Microsoft-Teams-GIFShell: [GitHub](https://github.com/bobbyrsec/Microsoft-Teams-GIFShell)

### Credential Attacks
- **Password Spraying**
  - MSOLSpray: [GitHub](https://github.com/MartinIngesen/MSOLSpray)
  - o365spray: [GitHub](https://github.com/0xZDH/o365spray)

- **MFA and Credential Dumping**
  - MFASweep: [GitHub](https://github.com/dafthack/MFASweep)
  - adconnectdump: [GitHub](https://github.com/dirkjanm/adconnectdump)

## AWS Tools

### Enumeration
- weirdAAL: [GitHub](https://github.com/carnal0wnage/weirdAAL)
- enumerate-iam: [GitHub](https://github.com/andresriancho/enumerate-iam)
- s3enum: [GitHub](https://github.com/koenrh/s3enum)
- S3Scanner: [GitHub](https://github.com/sa7mon/S3Scanner)

### Information Gathering
- gitleaks: [GitHub](https://github.com/zricethezav/gitleaks)
- truffleHog: [GitHub](https://github.com/dxa4481/truffleHog)

### Lateral Movement
- cloudjack: [GitHub](https://github.com/prevade/cloudjack)
- Redboto: [GitHub](https://github.com/elitest/Redboto)

### Privilege Escalation
- barq: [GitHub](https://github.com/Voulnet/barq)
- purplepanda: [GitHub](https://github.com/carlospolop/purplepanda)

### Exploitation
- pacu: [GitHub](https://github.com/RhinoSecurityLabs/pacu)

### Credential Attacks
- aws-vault: [GitHub](https://github.com/99designs/aws-vault)

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/cloudsecpen.git
   cd cloudsecpen

2. Install dependencies:
   python3 dependencies.py

## Usage

1. Run the script:
   python3 main.py

2. Follow the menu prompts to select the desired cloud environment (Azure or AWS) and the specific tool or action you want to perform.

## Dependencies

The project includes dependencies for various tools used in the enumeration, information gathering, lateral movement, privilege escalation, exploitation, and credential attacks. Ensure you have git, pip, and go installed for managing dependencies.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.