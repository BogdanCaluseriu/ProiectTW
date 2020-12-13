import React from "react";
import {
    StyleSheet,
    Text,
    View,
    SafeAreaView,
    SectionList,
    TouchableOpacity,
    FlatList
} from "react-native";




const Doors = ({extraData}) => {
    console.log("Floor is:",extraData)

    const DATA = [
        {

            title: '101',

        },
        {

            title: '102',
        },
        {

            title: '103',
        },
    ];

    return(
        <SafeAreaView style={styles.container}>
            <FlatList
            data = {DATA}
            renderItem={({item})=>{
                return(
                    <View style={styles.item}>
                        <Text style ={styles.title}> {item.title} </Text>
                    </View>
                    )

            }}
            keyExtractor={(data)=>data.title}
            />


        </SafeAreaView>

    )

}






const styles = StyleSheet.create({
    container: {
        flex: 1,
        marginTop:10,
        marginHorizontal: 16
    },
    item: {
        backgroundColor: "#f9c2ff",
        padding: 20,
        marginVertical: 8
    },
    title: {
        fontSize: 24,
        alignItems:'center'
    }
});

export default Doors
