import React from 'react';
import { StyleSheet, View, Text, TouchableOpacity, ScrollView } from 'react-native';


export default function Umfrage() {
  return (
    <ScrollView>
    <View style={styles.container}>
    <Text style={styles.boxOne}>An welchem Campus studierst du?</Text>
     
     <TouchableOpacity style={styles.boxTwo}> 
     <Text style={{fontFamily: 'JosefineSansMedium', fontSize:50}}>Hamm</Text>
     </TouchableOpacity>
    
     <TouchableOpacity style={styles.boxFive}> 
     <Text style={{fontFamily: 'JosefineSansMedium', fontSize:50}}>Lippstadt</Text>
     </TouchableOpacity>
     </View>
     <View style={styles.container}>
      <Text style={styles.boxOne}>Wo wohnst du?</Text>
     
      <TouchableOpacity style={styles.boxTwo}> 
      <Text style={{fontFamily: 'JosefineSansMedium', fontSize:50}}>Eigene Wohnung</Text>
      </TouchableOpacity>
     
      <TouchableOpacity style={styles.boxThree}> 
      <Text style={{fontFamily: 'JosefineSansMedium', fontSize:50}}>Bei den Eltern</Text>
      </TouchableOpacity>
     
      <TouchableOpacity style={styles.boxFour}>
      <Text style={{fontFamily: 'JosefineSansMedium', fontSize:50}}>Wohnheim</Text>
      </TouchableOpacity>
    </View>
    </ScrollView>
  );

}const styles = StyleSheet.create({
    container: {
      backgroundColor: '#EBEFF0',
      paddingBottom: 30,
      paddingTop: 20,
      paddingLeft: 20,
      paddingRight: 20,
    },
    boxOne: {
      height: 175,
      backgroundColor: '#8BC1E9',
      justifyContent: 'space-between',
      textAlign: 'center',
      textAlignVertical: 'center',
      borderRadius: 25,
      fontFamily: "JosefineSansMedium",
      fontSize: 50,
      marginBottom: 30,
      paddingTop:10
    },
    boxTwo: {
      height: 125,
      backgroundColor: '#B28BBC',
      borderTopLeftRadius: 25,
      borderTopRightRadius: 25,
      justifyContent:"center",
      alignItems: "center",
    
    },
    boxThree: {
      height: 125,
      backgroundColor: '#4B6E74',
      justifyContent:"center",
      alignItems: "center",
    },
    boxFour: {
     height: 125,
      backgroundColor: '#F7AF9D',
      borderBottomLeftRadius: 25,
      borderBottomRightRadius: 25,
      justifyContent:"center",
      alignItems: "center",
    
    },
    boxFive: {
      height: 125,
      backgroundColor: '#4B6E74',
      justifyContent:"center",
      alignItems: "center",
      borderBottomLeftRadius: 25,
      borderBottomRightRadius: 25,
    },
    
  });
  