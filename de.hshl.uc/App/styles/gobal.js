import { StyleSheet } from 'react-native';

/**Erzeugen eines ausgelagerten Style Sheets für die Seiten Chat und Home */


export const globalStyles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#FFFFFF',
        paddingBottom: 30,
        paddingTop: 50,
        paddingLeft: 20,
        paddingRight: 20,
      },
     
      containerTwo: {
        flex: 1,
        backgroundColor: '#FFFFFF',
        paddingBottom: 10,
        paddingTop: 10,
    
      
      },
    Titel: {
      fontFamily: "PermanentMarker",
      fontSize: 50,
    },
      boxOne: {
        height: 175,
        backgroundColor: '#8BC1E9',
        margin: 30,
        justifyContent: "center",
        alignItems: "center",
        borderRadius: 25,
        
      },
      boxTwo: {
        height: 175,
        backgroundColor: '#B28BBC',
        margin: 30,
        justifyContent: "center",
        alignItems: "center",
        borderRadius: 25,
        fontFamily: "PermanentMarker",
        fontSize: 50,
      },
      boxThree: {
        height: 175,
        backgroundColor: '#4B6E74',
        margin: 30,
        justifyContent: "center",
        alignItems: "center",
        borderRadius: 25,
        fontFamily: "PermanentMarker",
        fontSize: 50,
      },
      boxFour: {
    
        backgroundColor: '#8BC1E9',
        height: 175,
        textAlign: 'center',
        textAlignVertical: 'center',
        borderRadius: 25,
        fontFamily: "PermanentMarker",
        fontSize: 50,
        margin: 20,
      },
      boxFive: {
        height: 175,
        backgroundColor: '#F7AF9D',
        margin: 30,
        justifyContent: "center",
        alignItems: "center",
        borderRadius: 25,
        fontFamily: "PermanentMarker",
        fontSize: 50,
      },

      Chat :{
        maxHeight:500,
        marginLeft: 20,
        marginRight: 20,
        borderWidth: 5,
        borderLeftWidth: 2,
        borderRightWidth: 2,
        borderColor: '#F7AF9D',
        borderRadius: 25,
        padding: 10,
      },
  
     Chatinput :{
   
       flexDirection: "row",
       justifyContent: 'space-between',
       alignItems: "flex-end",
       borderColor: '#888888',
       marginTop: 20,
       borderTopWidth:2
      
      },

      ButtonStyle :{
        marginTop:5,
        backgroundColor: '#8BC1E9',
        borderRadius: 10,
        alignItems: "center",
        padding: 8,
        width: 35,
        height: 35,
       
      },

      item :{
        margin:2,
        width: 342,
        
      }
  });