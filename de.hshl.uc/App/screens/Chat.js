import React,{useEffect, useState} from "react";
import { View, TextInput, Button, Text, FlatList, TouchableOpacity, KeyboardAvoidingView, ActivityIndicator} from "react-native";
import { globalStyles } from "../styles/gobal";
import { Ionicons } from '@expo/vector-icons'; 


const Chat = () => {
 
  const [message, setMessage] = useState()
  const [DATA,setDATA] = useState([])
  const [loading,setLoading]= useState(true)
 
  const fetchData = ()=>{
    fetch("http://34.159.99.140:1666/get-data")
    .then(res=>res.json())
    .then(results=>{

        setDATA(results)
        setLoading(false)

    })
 };

 useEffect(()=>{
  fetchData()
},[])
  
  const Item = ({ name }) => (
    <View>
      <Text>{name}</Text>
    </View>
  );

  const renderItem = ({ item }) => (
    <Item name={item.name} />
  );

  const submitData = ()=>{
    fetch("http://34.159.99.140:1666/send-data",{
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
      {
        loading? 
      <ActivityIndicator size="small" color="#0000ff" />
      :
      <FlatList
        data={DATA}
        renderItem={renderItem}
        keyExtractor={item => item._id}
        />
      }
      
       
     
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