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
<View style={globalStyles.containerTwo}>
       <Text style={globalStyles.boxFour}>Chat</Text>
       <View style={globalStyles.Spieleauswahl}>
  <TouchableOpacity
   style={globalStyles.boxTwo}
   onPress={(pressUmfrage)}>
   <Text  style={globalStyles.Titel}>Phong</Text>
   </TouchableOpacity>

    
 
   <TouchableOpacity
   style={globalStyles.boxThree}
   onPress={(pressSpiele)}>
   <Text style={globalStyles.Titel}>TickTackToe</Text>
   </TouchableOpacity>
   
   <TouchableOpacity
   style={globalStyles.boxFive}
   onPress={(pressChat)}>
   <Text style={globalStyles.Titel}>x</Text>
   </TouchableOpacity>
   </View>
  </View>
  );

}