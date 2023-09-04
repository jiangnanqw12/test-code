import subprocess

def get_wifi_passwords():
    command = "netsh wlan show profiles"
    wifi_profiles = subprocess.check_output(command, shell=True, encoding="utf-8").split("\n")
    wifi_profiles = [i.split(":")[1][1:-1] for i in wifi_profiles if "所有用户配置文件 :" in i]

    for wifi_name in wifi_profiles:
        try:
            password_command = f"netsh wlan show profile name=\"{wifi_name}\" key=clear"
            password_details = subprocess.check_output(password_command, shell=True, encoding="utf-8").split("\n")
            password_details = [i.split(":")[1][1:-1] for i in password_details if "关键内容" in i]

            if password_details:
                print(f"WiFi Name: {wifi_name}, Password: {password_details[0]}")
            else:
                print(f"WiFi Name: {wifi_name}, Password: Not found!")
        except IndexError:
            print(f"WiFi Name: {wifi_name}, Password: Could not be retrieved!")

if __name__ == "__main__":
    get_wifi_passwords()
