import * as React from 'react';
import { StyleSheet, View} from 'react-native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { NavigationContainer } from '@react-navigation/native';
import Maps from "./Maps"
import Header from './Header';
import Doors from './Doors';


const Drawer = createDrawerNavigator()

let MapsRoute = ({navigation}) =>{
     return(

        <View>
            <Header navigation={navigation}/>
            <Maps/>
        </View>

     )
}



let Router=()=> {
    return (
        <NavigationContainer>

            <Drawer.Navigator initialRouteName="Harta">
                <Drawer.Screen name="Harta" component={MapsRoute} />
                <Drawer.Screen name="Parter">
                    {props => <Doors {...props} extraData={0}/>}
                </Drawer.Screen>
                <Drawer.Screen name="Etajul 1">
                    {props => <Doors {...props} extraData={1}/>}
                </Drawer.Screen>
                <Drawer.Screen name="Etajul 2">
                    {props => <Doors {...props} extraData={2}/>}
                </Drawer.Screen>
                <Drawer.Screen name="Etajul 3">
                    {props => <Doors {...props} extraData={3}/>}
                </Drawer.Screen>
                <Drawer.Screen name="Etajul 4">
                    {props => <Doors {...props} extraData={4}/>}
                </Drawer.Screen>
                <Drawer.Screen name="Etajul 5">
                    {props => <Doors {...props} extraData={5}/>}
                </Drawer.Screen>
                <Drawer.Screen name="Etajul 6">
                    {props => <Doors {...props} extraData={6}/>}
                </Drawer.Screen>
                <Drawer.Screen name="Etajul 7">
                    {props => <Doors {...props} extraData={7}/>}
                </Drawer.Screen>

            </Drawer.Navigator>
        </NavigationContainer>
    );
}

export default Router




const styles = StyleSheet.create(
    {

        btn:
            {

                alignItems: 'flex-end',
                justifyContent: 'space-around',
                paddingRight: 20,
                paddingBottom:35,


            },

    }
);
