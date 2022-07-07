import { StatusBar } from 'expo-status-bar';
import AppLoading from 'expo-app-loading';
import { useFonts } from 'expo-font';
import Navigator from './navigation/homeStack'

/**Exportieren der Schriftarten für das Projekt */
export default () => {
  let [fontsLoaded] = useFonts({
   'PermanentMarker' : require('./assets/fonts/PermanentMarker-Regular.ttf'),
   "JosefineSansMedium" : require('./assets/fonts/JosefinSans-Medium.ttf')
  });



/** Laden der Schriftarten bevor die App startet und 
     ausführen der Stack Navifation, welche den Home 
     Screen zuerst aufruft.*/
  if (!fontsLoaded) {
    return <AppLoading />;
  } 
  return (
      <Navigator />
  );

}
