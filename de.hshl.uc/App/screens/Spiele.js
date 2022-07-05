import React from 'react';
import { StyleSheet, View, Text, TouchableOpacity} from 'react-native';


export default function Spiele() {
  return (
    
     <View style={styles.container}>
      <Text style={styles.boxOne}>Welches Spiel möchtest du spielen?</Text>
     
      <TouchableOpacity style={styles.boxTwo}> 
      <Text style={{fontFamily: 'JosefineSansMedium', fontSize:50}}>Phong</Text>
      </TouchableOpacity>
     
      <TouchableOpacity style={styles.boxThree}> 
      <Text style={{fontFamily: 'JosefineSansMedium', fontSize:50}}>Tick Tack Toe</Text>
      </TouchableOpacity>
     
      <TouchableOpacity style={styles.boxFour}>
      <Text style={{fontFamily: 'JosefineSansMedium', fontSize:50}}> C</Text>
      </TouchableOpacity>
    </View>

  );

}const styles = StyleSheet.create({
    container: {
      flex:1,
      backgroundColor: '#EBEFF0',
      paddingBottom: 30,
      paddingTop: 20,
      paddingLeft: 20,
      paddingRight: 20,
    },
    boxOne: {
      flex:2,
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
      flex:1,
      backgroundColor: '#B28BBC',
      borderTopLeftRadius: 25,
      borderTopRightRadius: 25,
      justifyContent:"center",
      alignItems: "center",
    
    },
    boxThree: {
      flex:1,
      backgroundColor: '#4B6E74',
      justifyContent:"center",
      alignItems: "center",
    },
    boxFour: {
      flex:1,
      backgroundColor: '#F7AF9D',
      borderBottomLeftRadius: 25,
      borderBottomRightRadius: 25,
      justifyContent:"center",
      alignItems: "center",
    
    },
  });
  