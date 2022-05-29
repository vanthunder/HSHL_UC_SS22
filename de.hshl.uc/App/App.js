import { StatusBar } from 'expo-status-bar';
import AppLoading from 'expo-app-loading';
import { useFonts, PermanentMarker_400Regular } from '@expo-google-fonts/permanent-marker';
import Home from './screens/Home';
import CreateUser from './screens/createUser';

export default () => {
  let [fontsLoaded] = useFonts({
    PermanentMarker_400Regular,
  });



  let fontSize = 24;
  let paddingVertical = 6;

  if (!fontsLoaded) {
    return <AppLoading />;
  } 
  return (
      <CreateUser />
  );

}
