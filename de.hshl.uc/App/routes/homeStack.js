import { createStackNavigator } from 'react-navigation-stack';
import 'react-native-gesture-handler';
import { createAppContainer } from 'react-navigation';
import Home from '../screens/Home';
import Chat from '../screens/Chat'

const screens = {
  Home: {
    screen: Home,
  },
  Chat: {
    screen: Chat,
  },
};

// home stack navigator screens
const HomeStack = createStackNavigator(screens);

export default createAppContainer(HomeStack);
