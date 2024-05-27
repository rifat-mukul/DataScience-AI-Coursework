import requests

class RandomUser:
    def __init__(self):
        self.data = self.get_user_data()
    
    def get_user_data(self):
        url = 'https://randomuser.me/api/'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['results'][0]
        else:
            raise Exception(f"Failed to retrieve data. Status code: {response.status_code}")
    
    def get_cell(self):
        return self.data['cell']
    
    def get_city(self):
        return self.data['location']['city']
    
    def get_dob(self):
        return self.data['dob']['date']
    
    def get_email(self):
        return self.data['email']
    
    def get_first_name(self):
        return self.data['name']['first']
    
    def get_full_name(self):
        name = self.data['name']
        return f"{name['title']} {name['first']} {name['last']}"
    
    def get_gender(self):
        return self.data['gender']
    
    def get_id(self):
        return self.data['id']
    
    def get_id_number(self):
        return self.data['id']['value']
    
    def get_id_type(self):
        return self.data['id']['name']
    
    def get_info(self):
        return self.data
    
    def get_last_name(self):
        return self.data['name']['last']
    
    def get_login_md5(self):
        return self.data['login']['md5']
    
    def get_login_salt(self):
        return self.data['login']['salt']
    
    def get_login_sha1(self):
        return self.data['login']['sha1']
    
    def get_login_sha256(self):
        return self.data['login']['sha256']
    
    def get_nat(self):
        return self.data['nat']
    
    def get_password(self):
        return self.data['login']['password']
    
    def get_phone(self):
        return self.data['phone']
    
    def get_picture(self):
        return self.data['picture']
    
    def get_postcode(self):
        return self.data['location']['postcode']
    
    def get_registered(self):
        return self.data['registered']['date']
    
    def get_state(self):
        return self.data['location']['state']
    
    def get_street(self):
        return self.data['location']['street']['name']
    
    def get_username(self):
        return self.data['login']['username']
    
    def get_zipcode(self):
        return self.get_postcode()

# Example Usage
if __name__ == "__main__":
    user = RandomUser()
    
    print("Full Name:", user.get_full_name())
    print("Email:", user.get_email())
    print("Username:", user.get_username())
    print("Gender:", user.get_gender())
    print("Date of Birth:", user.get_dob())
    print("Street:", user.get_street())
    print("City:", user.get_city())
    print("State:", user.get_state())
    print("Postcode:", user.get_postcode())
    print("Phone:", user.get_phone())
    print("Cell:", user.get_cell())
    print("Nationality:", user.get_nat())
    print("Registered Date:", user.get_registered())
    print("ID:", user.get_id())
    print("ID Type:", user.get_id_type())
    print("ID Number:", user.get_id_number())
    print("Login Username:", user.get_username())
    print("Login Password:", user.get_password())
    print("Login MD5:", user.get_login_md5())
    print("Login Salt:", user.get_login_salt())
    print("Login SHA1:", user.get_login_sha1())
    print("Login SHA256:", user.get_login_sha256())
    print("Picture:", user.get_picture())
