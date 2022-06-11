import React,{useState} from "react";
import { View, StyleSheet, TextInput, Button, Text } from "react-native";
import { globalStyles } from "../styles/gobal";




const CreateUser = () => {



  const [name, setName] = useState();
  const [password, setPassword] = useState();




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
      <TextInput
        style={styles.input}
        value={name}
        onChangeText={text => setName(text)}
        placeholder="Name"
      />
      <TextInput
        style={styles.input}
        value={password}
        onChangeText={text => setPassword(text)}
        placeholder="Passwort"
      />
   <Button 
        
              mode="contained" 
             title="senden"
              onPress={() => submitData()}>
r
             </Button>
    </View>
  );
};

const styles = StyleSheet.create({
  input: {
    
    height: 40,
    margin: 12,
    borderWidth: 1,
    padding: 10,
  },
});
export default CreateUser