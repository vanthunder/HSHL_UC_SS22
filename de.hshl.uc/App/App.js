import { StatusBar } from 'expo-status-bar';
import AppLoading from 'expo-app-loading';
import { useFonts } from 'expo-font';
import Navigator from './routes/homeStack'

export default () => {
  let [fontsLoaded] = useFonts({
   'PermanentMarker' : require('./assets/fonts/PermanentMarker-Regular.ttf'),
   "JosefineSansMedium" : require('./assets/fonts/JosefinSans-Medium.ttf')
  });




  if (!fontsLoaded) {
    return <AppLoading />;
  } 
  return (
      <Navigator />
  );

}
