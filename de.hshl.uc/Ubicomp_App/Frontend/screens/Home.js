import React from 'react';
import { StyleSheet, View, Text } from 'react-native';
import { globalStyles } from '../styles/gobal';

export default function Home() {
  return (
    <View style={globalStyles.container}>
      <Text style={globalStyles.boxOne}>Umfrage</Text>
      <Text style={globalStyles.boxTwo}>Spiele</Text>
      <Text style={globalStyles.boxThree}>Chat</Text>
    </View>
    );

  }