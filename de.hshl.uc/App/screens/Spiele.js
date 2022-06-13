import React from 'react';
import { StyleSheet, View, Text, TouchableOpacity } from 'react-native';
import { globalStyles } from "../styles/gobal";

export default function Spiele(navigation) {
  const pressUmfrage = () => {
    navigation.navigate('Umfrage')
  }
  const pressSpiele = () => {
    navigation.navigate('Spiele')
  }
  const pressChat = () => {
    navigation.navigate('Chat')
  }
  return (
 <View style={globalStyles.container}>
   
  
  <TouchableOpacity
   style={globalStyles.boxOne}
   onPress={(pressUmfrage)}>
   <Text  style={globalStyles.Titel}>Phong</Text>
   </TouchableOpacity>

    
 
   <TouchableOpacity
   style={globalStyles.boxTwo}
   onPress={(pressSpiele)}>
   <Text style={globalStyles.Titel}>TickTackToe</Text>
   </TouchableOpacity>
   
   <TouchableOpacity
   style={globalStyles.boxThree}
   onPress={(pressChat)}>
   <Text style={globalStyles.Titel}>x</Text>
   </TouchableOpacity>
  
  </View>
  );

}