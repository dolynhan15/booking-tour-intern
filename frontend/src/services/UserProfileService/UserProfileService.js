import axios from "axios";

class UserProfileService {
  get entity() {
    return "http://127.0.0.1:8000/user/profiles";
  }

  async getUserProfileById(id) {
    const config = {
      headers: {
        "Authorization": `Bearer ${localStorage.getItem("access_token")}`,
      }
    };
    const response = await axios.get(`${this.entity}/${id}/`, config);
    return response.data
  }
}

export default new UserProfileService();
