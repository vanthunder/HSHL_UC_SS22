import React,{useState} from "react";
import { View, StyleSheet, TextInput, Button, Text, SafeAreaView } from "react-native";
import { globalStyles } from "../styles/gobal";



const Chat = () => {



  const [name, setName] = useState();
  const [password, setMessage] = useState();




  const submitData = ()=>{
    fetch("http://34.159.99.140:1666/send-data",{
        method:"post",
        headers:{
          'Content-Type': 'application/json',
         'Access-Control-Allow-Origin': '*'
        },

        body:JSON.stringify({
           name,
          
        })
    })

    .then(response => response.json())
    .then(data => console.log(data));
}




        
  

  return (
    <View style={globalStyles.container}>
      
      <Text style={globalStyles.boxThree}>Chat</Text>
     
      <TextInput
        style={globalStyles.Chatinput}
        value={name}
        onChangeText={text => setName(text)}
        placeholder="Hier können Sie tippen"
      />

      <Button 
              style={globalStyles.ButtonStyle}
              mode="contained" 
              title="senden"
              onPress={() => submitData()}>
            r
      </Button>
    </View>
  );
};


  export default Chat;