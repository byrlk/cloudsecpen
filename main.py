import os
import subprocess
import requests as req
import re

def print_ascii_art():
    art = """
       .__                   .___                                         
  ____ |  |   ____  __ __  __| _/______ ____   ____ ______   ____   ____  
_/ ___\\|  |  /  _ \\|  |  \\/ __ |/  ___// __ \\_/ ___\\\\____ \\_/ __ \\ /    \\ 
\\  \\___|  |_(  <_> )  |  / /_/ |\\___ \\\\  ___/\\  \\___|  |_> >  ___/|   |  \\
 \\___  >____/\\____/|____/\\____ /____  >\\___  >\\___  >   __/ \\___  >___|  /
     \\/                       \\/    \\/     \\/     \\/|__|        \\/     \\/ c

    Author: Luka Bayer
    Version: 1.0/Beta
    Date: 06/2024
    """
    print(art)

# Function to check if a tool is installed by checking if the folder exists
def is_tool_installed(tool_path):
    return os.path.isdir(tool_path)

# Function to install a tool by cloning the repository
def install_tool(url, category_path):
    try:
        os.makedirs(category_path, exist_ok=True)
        tool_name = url.split('/')[-1]
        tool_path = os.path.join(category_path, tool_name)
        if not os.path.isdir(tool_path):
            subprocess.run(['git', 'clone', url, tool_path], check=True)
            print(f'{tool_name} installed successfully in {category_path}.')
        else:
            print(f'{tool_name} is already installed in {category_path}.')
    except Exception as e:
        print(f"Error installing tool from {url}: {e}")

# Function to install all tools
def install_all_tools(tools, base_path):
    for selection, url in tools.items():
        if isinstance(url, str):
            category_path = os.path.join(base_path, selection.rsplit(".", 1)[0].replace(".", "_"))
            install_tool(url, category_path)

# Function to run the email verification tool
def validate_email(email):
    try:
        url = 'https://login.microsoftonline.com/common/GetCredentialType'
        body = '{"Username":"%s"}' % email
        request = req.post(url, data=body)
        response = request.text
        valid = re.search('"IfExistsResult":0,', response)
        invalid = re.search('"IfExistsResult":1,', response)
        return valid, invalid
    except Exception as e:
        print(f"Error validating email {email}: {e}")
        return None, None

def run_o365creeper():
    email = input("Enter the email address to validate: ")
    valid, invalid = validate_email(email)
    if invalid:
        print(f'{email} - INVALID')
    elif valid:
        print(f'{email} - VALID')
    else:
        print(f'{email} - UNKNOWN')

# Flattened dictionary for Azure tools
azure_tools = {
    "2.1.1.1": "https://github.com/LMGsec/o365creeper",
    "2.1.1.2": "https://github.com/gremwell/o365enum",
    "2.1.2.1": "https://github.com/0xsha/CloudBrute",
    "2.1.2.2": "https://github.com/initstring/cloud_enum",
    "2.1.2.3": "https://github.com/nccgroup/ScoutSuite",
    "2.1.2.4": "https://github.com/cyberark/blobhunter",
    "2.1.2.5": "https://github.com/BishopFox/cloudfox",
    "2.2.1.1": "https://github.com/dirkjanm/ROADtools",
    "2.3.1.1": "https://github.com/Azure/Stormspotter",
    "2.3.2.1": "https://github.com/cyberark/SkyArk",
    "2.3.3.1": "https://github.com/marcosimioni/omigood",
    "2.4.1.1": "https://github.com/talmaor/AzureADLateralMovement",
    "2.5.1.1": "https://github.com/NetSPI/MicroBurst",
    "2.5.2.1": "https://github.com/bobbyrsec/Microsoft-Teams-GIFShell",
    "2.6.1.1": "https://github.com/MartinIngesen/MSOLSpray",
    "2.6.1.2": "https://github.com/0xZDH/o365spray",
    "2.6.2.1": "https://github.com/dafthack/MFASweep",
    "2.6.2.2": "https://github.com/dirkjanm/adconnectdump"
}

# Flattened dictionary for AWS tools
aws_tools = {
    "3.1.1": "https://github.com/carnal0wnage/weirdAAL",
    "3.1.2": "https://github.com/andresriancho/enumerate-iam",
    "3.1.3": "https://github.com/koenrh/s3enum",
    "3.1.4": "https://github.com/sa7mon/S3Scanner",
    "3.2.1": "https://github.com/zricethezav/gitleaks",
    "3.2.2": "https://github.com/dxa4481/truffleHog",
    "3.3.1": "https://github.com/prevade/cloudjack",
    "3.3.2": "https://github.com/elitest/Redboto",
    "3.4.1": "https://github.com/Voulnet/barq",
    "3.4.2": "https://github.com/carlospolop/purplepanda",
    "3.5.1": "https://github.com/RhinoSecurityLabs/pacu",
    "3.6.1": "https://github.com/99designs/aws-vault"
}

# Menu structure for Azure
azure_menu_structure = {
    "2.1 Enumeration": {
        "2.1.1 Email Enumeration": [
            "2.1.1.1 o365creeper",
            "2.1.1.2 Office 365 User Enumeration"
        ],
        "2.1.2 Cloud Resource Enumeration": [
            "2.1.2.1 CloudBrute",
            "2.1.2.2 cloud_enum",
            "2.1.2.3 ScoutSuite",
            "2.1.2.4 BlobHunter",
            "2.1.2.5 CloudFox"
        ]
    },
    "2.2 Information Gathering": {
        "2.2.1 Azure AD Interaction and Assessment": [
            "2.2.1.1 ROADtools"
        ]
    },
    "2.3 Lateral Movement": {
        "2.3.1 Azure Object Graphing": [
            "2.3.1.1 Stormspotter"
        ],
        "2.3.2 Privilege Entity Discovery": [
            "2.3.2.1 SkyArk"
        ],
        "2.3.3 Vulnerability Scanning": [
            "2.3.3.1 omigood"
        ]
    },
    "2.4 Privilege Escalation": {
        "2.4.1 Privilege Escalation Tools": [
            "2.4.1.1 AzureADLateralMovement"
        ]
    },
    "2.5 Exploitation": {
        "2.5.1 Script-Based Exploitation": [
            "2.5.1.1 MicroBurst"
        ],
        "2.5.2 Exploitation via Teams": [
            "2.5.2.1 Microsoft-Teams-GIFShell"
        ]
    },
    "2.6 Credential Attacks": {
        "2.6.1 Password Spraying": [
            "2.6.1.1 MSOLSpray.py",
            "2.6.1.2 o365spray"
        ],
        "2.6.2 MFA and Credential Dumping": [
            "2.6.2.1 MFASweep",
            "2.6.2.2 adconnectdump"
        ]
    }
}

# Menu structure for AWS
aws_menu_structure = {
    "3.1 Enumeration": [
        "3.1.1 weirdAAL",
        "3.1.2 enumerate-iam",
        "3.1.3 s3enum",
        "3.1.4 S3Scanner"
    ],
    "3.2 Information Gathering": [
        "3.2.1 gitleaks",
        "3.2.2 truffleHog"
    ],
    "3.3 Lateral Movement": [
        "3.3.1 cloudjack",
        "3.3.2 Redboto"
    ],
    "3.4 Privilege Escalation": [
        "3.4.1 barq",
        "3.4.2 urplepanda"
    ],
    "3.5 Exploitation": [
        "3.5.1 pacu"
    ],
    "3.6 Credential Attacks": [
        "3.6.1 aws-vault"
    ]
}

def display_menu(menu_structure, level=0):
    indent = "    " * level
    for key, value in menu_structure.items():
        print(f"{indent}{key}")
        if isinstance(value, dict):
            display_menu(value, level + 1)
        elif isinstance(value, list):
            for item in value:
                print(f"{indent}    {item}")

def handle_selection(selection, tools):
    if selection == "0":
        install_all_tools(tools, "azure" if "2" in selection else "aws")
    elif selection == "99":
        import dependencies
        dependencies.main()
    elif selection == "100":
        return
    else:
        if selection in tools:
            if selection == "2.1.1.1":
                run_o365creeper()
            else:
                tool_url = tools[selection]
                category_path = ("azure" if "2" in selection else "aws") + "/" + selection.rsplit(".", 1)[0].replace(".", "_")
                install_tool(tool_url, category_path)
        else:
            print(f"Invalid selection: {selection}. Could not find URL for this selection.")

def azure_menu():
    while True:
        print("Azure Tools Menu")
        print("0: Install All Tools")
        print("99: Install All Dependencies")
        print("100: Go Back")
        display_menu(azure_menu_structure)
        selection = input("Enter your choice (e.g., 2.1.1.1): ")
        if selection == "100":
            break
        handle_selection(selection, azure_tools)

def aws_menu():
    while True:
        print("AWS Tools Menu")
        print("0: Install All Tools")
        print("99: Install All Dependencies")
        print("100: Go Back")
        display_menu(aws_menu_structure)
        selection = input("Enter your choice (e.g., 3.1.1): ")
        if selection == "100":
            break
        handle_selection(selection, aws_tools)

def main_menu():
    print_ascii_art()
    print("\nMain Menu")
    print("1: Azure")
    print("2: AWS")
    print("0: Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        azure_menu()
    elif choice == "2":
        aws_menu()
    elif choice == "0":
        exit()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    while True:
        main_menu()
