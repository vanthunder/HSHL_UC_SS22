import React from 'react';
import { StyleSheet, View, Text } from 'react-native';
import { TouchableOpacity } from 'react-native-gesture-handler';
import { globalStyles } from '../styles/gobal';

export default function Home( { navigation }) {
  const pressChat = () => {
    navigation.navigate('Chat')
  }
  return (
    <View styles={globalStyles.container}>
  
    <TouchableOpacity
     style={globalStyles.boxOne}
     onPress={(pressChat)}>
     <Text  style={globalStyles.Titel}>Umfrage</Text>
     </TouchableOpacity>
  
      
   
     <TouchableOpacity
     style={globalStyles.boxTwo}
     onPress={(pressChat)}>
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