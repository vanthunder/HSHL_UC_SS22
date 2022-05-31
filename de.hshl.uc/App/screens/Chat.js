import React,{useState} from "react";
import { View, StyleSheet, TextInput, Button, Text, FlatList, TouchableOpacity} from "react-native";
import { globalStyles } from "../styles/gobal";
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'



const Chat = () => {



  const [name, setName] = useState();





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
    <KeyboardAwareScrollView>
    <View style={globalStyles.container}>
       <Text style={globalStyles.boxOne}>Chat</Text>
       <View style={globalStyles.Chat}>
      
           <Text>1 2 3 Test</Text>
       
     
        <View style={globalStyles.Chatinput}>
         <TextInput
          style={globalStyles.Message}
          value={name}
          onChangeText={text => setName(text)}
          placeholder="Hier können Sie tippen"
         />
  
         <TouchableOpacity
           style={globalStyles.ButtonStyle}
          onPress={() => submitData()}
      >
          <Text>Senden</Text>
         </TouchableOpacity>
       </View>
      
      </View>
    </View>
    </KeyboardAwareScrollView>
  );
};


  export default Chat;