import React,{useEffect, useState} from "react";
import { View, TextInput, Text, FlatList, TouchableOpacity, KeyboardAvoidingView, ActivityIndicator, ScrollView} from "react-native";
import { globalStyles } from "../styles/gobal";
import { Ionicons } from '@expo/vector-icons'; 


const Chat = () => {

  /**Variablen zum Abspeichern von Daten */

  const [message, setMessage] = useState()
  const [DATA,setDATA] = useState([])
  const [loading,setLoading]= useState(true)
  const flatListRef = React.useRef();

/** Textfeld wird wieder leer nach absenden der Nachricht */

  const clearMessage = () => {
    setMessage('');
  }  
 
  /** Methode zum Auslesen der Daten von MongoDB */
  const fetchData = ()=>{
    fetch("http://34.159.99.140:1666/get-data")
    .then(res=>res.json())
    .then(results=>{

        setDATA(results)
        setLoading(false)

    })
 };
/** Aufruf der Methode zum Auslesen der Daten um diese dann in den Variablen zu speichern */

 useEffect(()=>{
  fetchData()
},[])

/** Erzeugen einer Itemliste, welche später in der Flatlist ausgelesen wird mit den festgelegeten 
    Styles*/

  const Item = ({ message }) => (
    <View style={globalStyles.item}>
      <Text  style={{fontFamily: 'JosefineSansMedium'}}>{message}</Text>
    </View>
  );

  /** Festelegen vom Inhalt des Items. Hier sollen nur die Chatnachrichten der MongoDB erfasst werden */
  const renderItem = ({ item }) => (
    <Item message={item.message} />
  );

  /** Übermitteln der Chatnarchrichten die gesendet werden sollen an die MongoDB */

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

    /** Keyboard Avoiding View bedeutet, dass die Seite auf dem Handy verschoben wird, damit die Tastatur, dass Textfeld nicht
        verdeckt
     */
    <KeyboardAvoidingView
     /** Verschachtelt das Scrollen ineinander damit die Flatlist ohne Probleme dargestellt werden kann */
     >    


    <ScrollView horizontal={false}>

       <Text style={globalStyles.boxFour}>Chat</Text>
       <View style={globalStyles.Chat}>

    
{    /** Ausführen einer Ladeanimation falls die Datenbank leer sein sollte 
      Icon von https://reactnative.dev/docs/activityindicator
    */
        loading? 
      <ActivityIndicator size="small" color="#0000ff" />
      :
      <ScrollView horizontal={true}>

    
      <FlatList
        /**Hier werden die Daten der Mongo DB ausgelesen und nach ihrer item id sortiert. Außerdem ist eine Funktion implementiert,
         damit die Liste immer zum aktuellen Listenende scrollt. Diese Funktion wird pro Seitenaufruf einmal ausgeführt. Neue Nachrichten
         können also nicht gleich gelesen werden.
       */
        ref={flatListRef}
        data={DATA}
        renderItem={renderItem}
        keyExtractor={item => item._id}
         onLayout={() => flatListRef.current.scrollToEnd({ animated: true })}
        />
        </ScrollView>  
      }
    
        <View style={globalStyles.Chatinput}
        /** Hier wird ein Eingabefeld für die Narchichten erzeugt */>
        
         <TextInput
          style={{fontFamily: 'JosefineSansMedium'}}
          value={message}
          onChangeText={text => setMessage(text)}
          placeholder="Ihre Nachricht"
         />

         
       
         <TouchableOpacity
          /** Button zum Absenden der Nachrichten und zurücksetzen des Textfeldes.
            Leere Textnachrichten können nicht gesendet werden. 
        */
           style={globalStyles.ButtonStyle}
          onPress={() =>{ 
            if (message === "") {
            console.log("Message empty")
          } else {
          submitData();
          clearMessage();
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