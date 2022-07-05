import React,{useEffect, useState} from "react";
import { View, TextInput, Text, FlatList, TouchableOpacity, KeyboardAvoidingView, ActivityIndicator, ScrollView} from "react-native";
import { globalStyles } from "../styles/gobal";
import { Ionicons } from '@expo/vector-icons'; 


const Chat = () => {
  const [message, setMessage] = useState()
  const [DATA,setDATA] = useState([])
  const [loading,setLoading]= useState(true)
  const flatListRef = React.useRef();

  const clearMessage = () => {
    setMessage('');
  }  
 
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

  const Item = ({ message }) => (
    <View style={globalStyles.item}>
      <Text  style={{fontFamily: 'JosefineSansMedium'}}>{message}</Text>
    </View>
  );

  const renderItem = ({ item }) => (
    <Item message={item.message} />
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
    <ScrollView horizontal={false}>

       <Text style={globalStyles.boxFour}>Chat</Text>
       <View style={globalStyles.Chat}>
      
{
        loading? 
      <ActivityIndicator size="small" color="#0000ff" />
      :
      <ScrollView horizontal={true}>
      <FlatList
        ref={flatListRef}
        data={DATA}
        renderItem={renderItem}
        keyExtractor={item => item._id}
         onLayout={() => flatListRef.current.scrollToEnd({ animated: true })}
        />
        </ScrollView>  
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
          onPress={() =>{ 
            if (message === "") {
            console.log("Message empty")
          } else {
          submitData();
          clearMessage();
          fetchData()
           } }}>
          <Ionicons name="send" size={18} color="black" />
         </TouchableOpacity>
         
       </View>
      
       </View>
       </ScrollView>
    </KeyboardAvoidingView>
  );
};


  export default Chat;