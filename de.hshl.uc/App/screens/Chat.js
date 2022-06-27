import React,{useEffect, useState} from "react";
import { View, TextInput, Button, Text, FlatList, TouchableOpacity, KeyboardAvoidingView, ScrollView} from "react-native";
import { globalStyles } from "../styles/gobal";
import { Ionicons } from '@expo/vector-icons'; 


const Chat = () => {
 
  const [message, setMessage] = useState()
 

  const DATA = [
    {
      id: 'bd7acbea-c1b1-46c2-aed5-3ad53abb28ba',
      name: 'First Item',
    },
    {
      id: '3ac68afc-c605-48d3-a4f8-fbd91aa97f63',
      name: 'Second Item',
    },
    {
      id: '58694a0f-3da1-471f-bd96-145571e29d72',
      name: 'Third Item',
    },
  ];
  
  const Item = ({ name }) => (
    <View>
      <Text>{name}</Text>
    </View>
  );

  const renderItem = ({ item }) => (
    <Item name={item.name} />
  );

  const submitData = ()=>{
    fetch("http://34.159.165.27:1666/send-data",{
        method:"post",
        headers:{
          'Content-Type': 'application/json',
         'Access-Control-Allow-Origin': '*'
        },

        body:JSON.stringify({
           message,
          
        })
    })

    .then(response => response.json())
    .then(data =>{
      console.log(data)
    });
}




        
  

  return (
    <KeyboardAvoidingView>
 
       <Text style={globalStyles.boxFour}>Chat</Text>
       <View style={globalStyles.Chat}>
      
       <FlatList
        data={DATA}
        renderItem={renderItem}
        keyExtractor={item => item._id}
        />
       
     
        <View style={globalStyles.Chatinput}>
         <TextInput
          style={{fontFamily: 'JosefineSansMedium'}}
          value={message}
          onChangeText={text => setMessage(text)}
          placeholder="Ihre Nachricht"
         />
  
         <TouchableOpacity
           style={globalStyles.ButtonStyle}
          onPress={() => submitData()}>
          <Ionicons name="send" size={18} color="black" />
         </TouchableOpacity>
       </View>
      
      </View>
    
    </KeyboardAvoidingView>
  );
};


  export default Chat;