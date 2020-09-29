import React, { Component } from "react";
import { ListGroup } from "react-bootstrap";
import MessageView from "./MessageView";
import TextBoxContainer from "../TextBox";
import listResource from "../../../utils/api/resources/listResource";
import AuthContext from "../../../contexts/AuthContext";
import {
  BASE_URL,
  ROOMS_ENDPOINT,
  MESSAGES_EXTENSION,
  MESSAGING_WEBSOCKET
} from "../../../constants/urls/apiUrls";
import likeResource from "../../../utils/api/resources/likeResource";
import cleanLoadedResources from "../../../utils/api/misc/cleanLoadedResources";
import { USER_DATA } from "../../../constants/misc/sessionStorageKeys";

class MessageContainer extends Component {
  static contextType = AuthContext;

  state = {
    messages: [],
    text: "",
    page: 0,
    prevY: 0
  };

  ws;

  componentDidMount = () => {
    listResource(this, (data) => this.setState({messages: cleanLoadedResources(this.state.messages.reverse(), data).reverse(), page: this.state.page + 1}),
      BASE_URL + ROOMS_ENDPOINT + this.props.room.id + MESSAGES_EXTENSION);

    this.ws = new WebSocket(MESSAGING_WEBSOCKET + this.props.room.id + "/");

    this.ws.onopen = () => {
      console.log("Connected");
      this.setState({prevY: 0});
    };

    this.ws.onmessage = (ev) => {
      let message = JSON.parse(ev.data);
      this.setState({messages: [...this.state.messages, message]});
    };

    this.ws.onclose = () => {
      this.setState({ws: new WebSocket(MESSAGING_WEBSOCKET + this.props.room.id + "/")});
    };

    window.onscroll = () => {
      if(window.pageYOffset === 0) {
        let options = {
          root: null,
          rootMargin: '200px',
          threshold: 1.0
        };

        this.observer = new IntersectionObserver(
          this.handleObserver,
          options
        );

        this.observer.observe(this.loadingRef);
      }
    }
  };

  loadPosts = () => {
    listResource(this, (data) => this.setState({messages: cleanLoadedResources(this.state.messages.reverse(), data).reverse(), page: this.state.page + 1}),
    BASE_URL + ROOMS_ENDPOINT + this.props.room.id + MESSAGES_EXTENSION, this.state.page);
  };

  handleObserver = (entities, options) => {
    const y = entities[0].boundingClientRect.y;
    if (this.state.prevY < y) {
      this.loadPosts();
    }
    this.setState({prevY: y});
  };

  handleSend = () => {
    let messageBody = this.state.text.trim();

    if(messageBody.length !== 0){
      this.ws.send(JSON.stringify({
        'message_body': messageBody
      }));
      this.setState({text: ""})
    }
  };

  handleChange = (e) => {
    this.setState({text: e.target.value});
  };

  handleLike = (id) => {
    likeResource(this, BASE_URL + ROOMS_ENDPOINT + "messages/", id);
  };

  render() {
    let room = this.props.room;

    let roomTitle = room.isDirectMessaging ?
      (JSON.parse(sessionStorage.getItem(USER_DATA)).id === room.members[0].id ?
        room.members[0].preferred_name : room.members[1].preferred_name)
      : room.title;

    return (
      <div>
        <h3>
          {roomTitle}
        </h3>
        <div>
          <div ref={loadingRef => (this.loadingRef = loadingRef)}>
              <span>Scroll up from below to retrieve previous messages.</span>
          </div>
          <ListGroup>
            {this.state.messages.map((message) => (
              <MessageView
                key={message.id}
                id={message.id}
                messageBody={message.message_body}
                creator={message.creator}
                datetimeCreated={message.datetime_created}
                handleLike={this.handleLike}
              />
            ))}
          </ListGroup>
        </div>
        <TextBoxContainer
          handleSend={this.handleSend}
          handleChange={this.handleChange}
          text={this.state.text}
        />
      </div>
    );
  }
}

export default MessageContainer;