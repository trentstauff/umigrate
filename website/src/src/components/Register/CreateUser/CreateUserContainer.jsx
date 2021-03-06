import React, { Component } from "react";
import Axios from "axios";
import Modal from "react-bootstrap/Modal";
import ModalHeader from "react-bootstrap/ModalHeader";
import ModalTitle from "react-bootstrap/ModalTitle";
import AuthContext from "../../../contexts/AuthContext";
import CreateUserView from "./CreateUserView";
import { BASE_URL } from "../../../utils/endpoints";

class CreateUserContainer extends Component {
  static contextType = AuthContext;

  state = {
    showFailureModal: false,
    file: "",
    imagePreviewUrl: "",
  };

  handleSubmit = (e) => {

    //Todo: fix this
    const data = new FormData();
    data.append("first_name", document.getElementById("firstName").value);
    data.append("last_name", document.getElementById("lastName").value);
    data.append(
      "preferred_name",
      document.getElementById("preferredName").value
    );
    data.append("sex", document.getElementById("sex").value);
    data.append("birthday", document.getElementById("birthday").value);
    data.append("bio", document.getElementById("bio").value);
    data.append(
      "enrolled_program",
      document.getElementById("enrolledProgram").value
    );
    data.append("region", document.getElementById("region").value);
    data.append("phone_number", document.getElementById("phoneNumber").value);
    data.append("current_term", document.getElementById("term").value);
    data.append("photo", this.state.file);

    Axios.patch(BASE_URL + "auth/user/", data, {
      headers: { "content-type": "multipart/form-data" },
    })
      .then((response) => {
        this.context.setRegistered(true);
        sessionStorage.setItem("USER_DATA", JSON.stringify(response.data));
      })
      .catch((error) => {
        console.log(error);
        console.log(error.response);
        this.setState({ showFailureModal: true });
      });

    e.preventDefault();
  };

  handleClose = () => {
    this.setState({ showFailureModal: false });
  };

  getFailureModal = () => {
    return (
      <Modal show={this.state.showFailureModal} onHide={this.handleClose}>
        <ModalHeader>
          <ModalTitle>An error has occurred!</ModalTitle>
        </ModalHeader>
      </Modal>
    );
  };

  handleImageUpload = (e) => {
    let reader = new FileReader();
    let file = e.target.files[0];
    if (!file) {
      this.setState({
        file: "",
        imagePreviewUrl: "",
      });
      return;
    }
    reader.readAsDataURL(file);
    reader.onloadend = () => {
      this.setState({
        file: file,
        imagePreviewUrl: reader.result,
      });
    };

    e.preventDefault();
  };

  render() {
    return (
      <div>
        {this.getFailureModal()}
        <CreateUserView
          handleSubmit={this.handleSubmit}
          handleImageUpload={this.handleImageUpload}
          imagePreviewUrl={this.state.imagePreviewUrl}
        />
      </div>
    );
  }
}

export default CreateUserContainer;
