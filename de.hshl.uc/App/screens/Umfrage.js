import React from 'react';
import { StyleSheet, View, Text } from 'react-native';


export default function Umfrage() {
  return (
    <View style={styles.container}>
      <Text style={styles.boxOne}>A</Text>
      <Text style={styles.boxTwo}>B</Text>
      <Text style={styles.boxThree}>C</Text>
      <Text style={styles.boxThree}>D</Text>
    </View>
  );

}const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#EBEFF0',
      paddingBottom: 40,
      paddingTop: 60,
      paddingLeft: 20,
      paddingRight: 20,
    },
    boxOne: {
      flex: 1,
      backgroundColor: '#8BC1E9',
      margin: 30,
      textAlign: 'center',
      textAlignVertical: 'center',
      borderRadius: 25,
      fontFamily: "PermanentMarker_400Regular",
      fontSize: 50,
    },
    boxTwo: {
      flex: 1,
      backgroundColor: '#B28BBC',
      margin: 30,
      textAlign: 'center',
      textAlignVertical: 'center',
      borderRadius: 25,
      fontFamily: "PermanentMarker_400Regular",
      fontSize: 50,
    },
    boxThree: {
      flex: 1,
      backgroundColor: '#4B6E74',
      margin: 30,
      textAlign: 'center',
      textAlignVertical: 'center',
      borderRadius: 25,
      fontFamily: "PermanentMarker_400Regular",
      fontSize: 50,
    }
  });
  