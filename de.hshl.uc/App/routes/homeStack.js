import { createStackNavigator } from 'react-navigation-stack';
import 'react-native-gesture-handler';
import { createAppContainer } from 'react-navigation';
import Home from '../screens/Home';
import Chat from '../screens/Chat'
import Umfrage from '../screens/Umfrage'
import Spiele from '../screens/Spiele'


const screens = {
  Home: {
    screen: Home,
  },
  Umfrage: {
    screen: Umfrage,
    navigationOptions: {
        title: '',
      }
  },
  Spiele: {
    screen: Spiele,
    navigationOptions: {
        title: '',
      }
  },
  Chat: {
    screen: Chat,
    navigationOptions: {
        title: '',
      }
  },
};

// home stack navigator screens
const HomeStack = createStackNavigator(screens, {
    defaultNavigationOptions: {
    
      headerStyle: { backgroundColor: '#FFFFFF', height: 80}
      
    }
  });

export default createAppContainer(HomeStack);
