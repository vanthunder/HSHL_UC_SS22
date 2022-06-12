import { StyleSheet } from 'react-native';

export const globalStyles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#EBEFF0',
        paddingBottom: 40,
        paddingTop: 60,
        paddingLeft: 20,
        paddingRight: 20,
      },
     
      containerTwo: {
        flex: 1,
        backgroundColor: '#EBEFF0',
        paddingBottom: 10,
        paddingTop: 60,
        fontFamily: "JosefineSansMedium"
      
      },
      boxOne: {
        flex: 1,
        backgroundColor: '#8BC1E9',
        margin: 30,
        textAlign: 'center',
        textAlignVertical: 'center',
        borderRadius: 25,
        fontFamily: "PermanentMarker",
        fontSize: 50,
      },
      boxTwo: {
        flex: 1,
        backgroundColor: '#B28BBC',
        margin: 30,
        textAlign: 'center',
        textAlignVertical: 'center',
        borderRadius: 25,
        fontFamily: "PPermanentMarker",
        fontSize: 50,
      },
      boxThree: {
        flex: 1,
        backgroundColor: '#4B6E74',
        margin: 30,
        textAlign: 'center',
        textAlignVertical: 'center',
        borderRadius: 25,
        fontFamily: "PermanentMarker",
        fontSize: 50,
      },
      boxFour: {
        flex: 1,
        backgroundColor: '#8BC1E9',
        height: 150,
        textAlign: 'center',
        textAlignVertical: 'center',
        borderRadius: 25,
        fontFamily: "PermanentMarker",
        fontSize: 50,
        margin: 20,
      },

      Chat :{
        height: 500,
        margin: 20,
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
       paddingTop: 420,
       fontFamily: "PermanentMarker",
      },

  
      ButtonStyle :{
        backgroundColor: '#8BC1E9',
        borderRadius: 10,
        alignItems: "center",
        padding: 8,
        width: 35,
        height: 35
      }

  });