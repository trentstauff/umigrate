import React, { useContext, useState } from 'react';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';
import AuthContext from "../../contexts/AuthContext";
import { BASE_URL, LOGIN_ENDPOINT, USER_PROFILE_ENDPOINT } from "../../constants/apiEndpoints";
import Axios from "axios";

const LoginPage = ({navigation}) => {
  const auth = useContext(AuthContext);
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();

  const handleSignIn = () => {
    Axios.post(BASE_URL + LOGIN_ENDPOINT, {email, password})
      .then((response) => {
        // Set authentication token to the header
        Axios.defaults.headers.common['Authorization'] = `Token ${response.data.key}`;
        Axios.get(BASE_URL + USER_PROFILE_ENDPOINT)
          .then(() => {
            auth.setAuthenticated(true);
          })
          .catch((error) => {
            console.log(error);
            console.log(error.response);
          })
      })
      .catch((error) => {
        console.log(error);
        console.log(error.response);
      });
  };

  const signUpRedirect = () => {
    navigation.navigate('Register');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Login Page!</Text>
      <View>
        <View style={styles.row}>
          <Text>Email: </Text>
          <TextInput
            style={styles.textInput}
            onChangeText={text => setEmail(text)}
          />
        </View>
        <View style={styles.row}>
          <Text>Password: </Text>
          <TextInput
            style={styles.textInput}
            onChangeText={text => setPassword(text)}
          />
        </View>
      </View>
      <View style={styles.buttonContainer}>
        <Button title="Sign in" onPress={handleSignIn} />
        <Button title="Sign up" onPress={signUpRedirect} />
      </View>
    </View>
  );
};

export default LoginPage;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#eeeeee',
    alignItems: 'center',
    justifyContent: 'center'
  },
  title: {
    marginTop: "40%"
  },
  row: {
    flexDirection: "row",
    justifyContent: "space-between",
    marginTop: 10,
    marginBottom: 10
  },
  textInput: {
    height: 40,
    width: 200,
    padding: 10,
    borderColor: "#000000",
    borderWidth: 2
  },
  buttonContainer: {
    flex: 1,
    justifyContent: "space-around",
    marginBottom: "50%"
  }
});