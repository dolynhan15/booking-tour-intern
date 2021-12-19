import axios from 'axios'

class LoginService {
  get entity() {
    return "http://127.0.0.1:8000/user";
  }

  async login(data) {
    try {
      const loginData = {
        "username": data["email"],
        "password": data["password"]
      }
      const response = await axios.post(`${this.entity}/login`, loginData);
      if (response) {
        return response["data"]
      }
    } catch (e) {
      console.log(e);
    }
  }
}

export default new LoginService();
