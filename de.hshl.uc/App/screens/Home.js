import React from 'react';
import { StyleSheet, View, Text } from 'react-native';
import { TouchableOpacity } from 'react-native-gesture-handler';
import { globalStyles } from '../styles/gobal';

export default function Home( { navigation }) {
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
    <View styles={globalStyles.container}>
  
    <TouchableOpacity
     style={globalStyles.boxOne}
     onPress={(pressUmfrage)}>
     <Text  style={globalStyles.Titel}>Umfrage</Text>
     </TouchableOpacity>
  
      
   
     <TouchableOpacity
     style={globalStyles.boxTwo}
     onPress={(pressSpiele)}>
     <Text style={globalStyles.Titel}>Spiele</Text>
     </TouchableOpacity>
     
     <TouchableOpacity
     style={globalStyles.boxThree}
     onPress={(pressChat)}>
     <Text style={globalStyles.Titel}>Chat</Text>
     </TouchableOpacity>
    
    
      
    </View>
    );

  }