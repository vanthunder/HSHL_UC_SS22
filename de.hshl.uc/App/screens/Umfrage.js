import React from 'react';
import { StyleSheet, View, Text } from 'react-native';


export default function Umfrage() {
  return (
    <View style={styles.container}>
      <Text style={styles.boxOne}>Was ist deine Meingung?</Text>
      <Text style={styles.boxTwo}>A</Text>
      <Text style={styles.boxThree}>B</Text>
      <Text style={styles.boxFour}>C</Text>
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
      justifyContent: 'space-between',
      textAlign: 'center',
      textAlignVertical: 'center',
      borderRadius: 25,
      fontFamily: "JosefineSansMedium",
      fontSize: 50,
      marginBottom: 30,
    },
    boxTwo: {
      flex: 1,
      backgroundColor: '#B28BBC',
      textAlign: 'center',
      textAlignVertical: 'center',
      borderTopLeftRadius: 25,
      borderTopRightRadius: 25,
      fontFamily: "JosefineSansMedium",
      fontSize: 50,
    },
    boxThree: {
      flex: 1,
      backgroundColor: '#4B6E74',
      textAlign: 'center',
      textAlignVertical: 'center',
      fontFamily: "JosefineSansMedium",
      fontSize: 50,
    },
    boxFour: {
      flex: 1,
      backgroundColor: '#F7AF9D',
      borderBottomLeftRadius: 25,
      borderBottomRightRadius: 25,
      textAlign: 'center',
      textAlignVertical: 'center',
      fontFamily: "JosefineSansMedium",
      fontSize: 50,
    }
    
  });
  