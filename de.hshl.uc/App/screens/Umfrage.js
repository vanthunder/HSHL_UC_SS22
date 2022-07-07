import React, { useState } from "react";
import { StyleSheet, View, Text, TouchableOpacity, ScrollView } from 'react-native';


export default function Umfrage() {
  
  //* Locales Abspeichern der Variablen für die Auszählung der Stimmen

  const [intHamm, setHamm] = useState(0);
  const [intLippstadt, setLippstadt] = useState(0);
  const [intWohnung, setWohnung] = useState(0);
  const [intEltern, setEltern] = useState(0);
  const [intWohnheimm, setWohnheim] = useState(0);
 
  //* für Prozentangaben gedachte gewesen: const [intVoteL, setVoteL] = useState(0);
   //* für Prozentangaben gedachte gewesen:const [intVoteH, setVoteH] = useState(0);


    //* Funktionen für die Auszählung der Stimmen

  const Hamm = () => {
    setHamm(prevInt => prevInt + 1)
     /** für Prozentangaben gedachte gewesen:setVoteL(prevInt => prevInt = (intLippstadt / (intHamm + ntLippstadt)*100))
     für Prozentangaben gedachte gewesen:setVoteH(prevCount => prevCount = (countHamm / (countHamm + countLippstadt)*100)) 
     */
    
  };
   const Lippstadt = () => {
   setLippstadt(prevCount => prevCount + 1 )
  };

  const Wohnung = () => {
    setWohnung(prevCount => prevCount + 1 )
   };

   const Eltern = () => {
    setEltern(prevCount => prevCount + 1 )
   };

   const Wohnheim = () => {
    setWohnheim(prevCount => prevCount + 1 )
   };
     /** Ausgabe der Komponenten die auf der Seite angezeigt werden. Die Scrollview ermöglich es zu scrollen und die
         Toauchable Opacirties sind Bottons die individuell gestaltet werden können
     */
      
  return (
    <ScrollView>
    <View style={styles.container}>
    <Text style={styles.boxOne}>An welchem Campus studierst du?</Text>
     
     <TouchableOpacity 
     style={styles.boxTwo}
     onPress={Hamm}> 
     <View style={{fontFamily: 'JosefineSansMedium'}}>
     <Text style={{fontSize:50, textAlign:"center"}}>Hamm</Text>
     <Text style={{fontSize:30, textAlign:"center"}}>Stimmen: {intHamm}</Text>
     </View>
     </TouchableOpacity>

     <TouchableOpacity
      style={styles.boxFive}
      onPress={Lippstadt}> 
      <View style={{fontFamily: 'JosefineSansMedium'}}>
     <Text style={{fontSize:50, textAlign:"center"}}>Lippstadt</Text>
     <Text style={{fontSize:30, textAlign:"center"}}>Stimmen: {intLippstadt}</Text>
     </View>
     </TouchableOpacity>
     </View>



     <View style={styles.container}>
      <Text style={styles.boxOne}>Wo wohnst du?</Text>
     
      <TouchableOpacity 
      style={styles.boxTwo}
      onPress={Wohnung}> 
      <Text style={{fontFamily: 'JosefineSansMedium', textAlign:"center", fontSize:50}}>Eigene Wohnung</Text>
      <Text style={{fontSize:30, textAlign:"center"}}>Stimmen: {intWohnung}</Text>
      </TouchableOpacity>
     
      <TouchableOpacity 
      style={styles.boxThree} 
      onPress={Eltern}> 
      <Text style={{fontFamily: 'JosefineSansMedium', textAlign:"center", fontSize:50}}>Eltern</Text>
      <Text style={{fontSize:30, textAlign:"center"}}>Stimmen: {intEltern}</Text>
      </TouchableOpacity>

      <TouchableOpacity 
      style={styles.boxFour}
      onPress={Wohnheim}>
      <Text style={{fontFamily: 'JosefineSansMedium', textAlign:"center", fontSize:50}}>Wohnheim</Text>
      <Text style={{fontSize:30, textAlign:"center"}}>Stimmen: {intWohnheimm}</Text>
      </TouchableOpacity>
    </View>
    </ScrollView>
  );
  
  /** Hier befinden sich die CSS-Befehle zum Abändern der einzelnen Komponenten */

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
  