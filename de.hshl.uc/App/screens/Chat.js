import React,{useState} from "react";
import { View, TextInput, Button, Text, FlatList, TouchableOpacity, KeyboardAvoidingView, ScrollView} from "react-native";
import { globalStyles } from "../styles/gobal";
import { Ionicons } from '@expo/vector-icons'; 


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
    .then(data =>{
      console.log(data)
    });
}




        
  

  return (
    <KeyboardAvoidingView>
    <ScrollView>
 
       <Text style={globalStyles.boxFour}>Chat</Text>
       <View style={globalStyles.Chat}>
      
           <Text style={{fontFamily: 'JosefineSansMedium'}}>
           1 2 3 Test
           </Text>
       
     
        <View style={globalStyles.Chatinput}>
         <TextInput
          style={{fontFamily: 'JosefineSansMedium'}}
          value={name}
          onChangeText={text => setName(text)}
          placeholder="Ihre Nachricht"
         />
  
         <TouchableOpacity
           style={globalStyles.ButtonStyle}
          onPress={() => submitData()}>
          <Ionicons name="send" size={18} color="black" />
         </TouchableOpacity>
       </View>
      
      </View>
    
    </ScrollView>
    </KeyboardAvoidingView>
  );
};


  export default Chat;