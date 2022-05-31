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
      },

      Chat :{
        height: 500,
        margin: 12,
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
      },

  
      ButtonStyle :{
        backgroundColor: '#8BC1E9',
        borderRadius: 25,
        alignItems: "center",
        padding: 5,
        marginBottom: 1,
        width: 60,
  
      }

  });