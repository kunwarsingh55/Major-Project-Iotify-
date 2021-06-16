import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

String globalS1;
String globalS2;
String globalS3;

var getDataUrl =
    Uri.parse('https://68bb78d02ffd.ngrok.io/dataExchange/androidData/');

void main() {
  runApp(Iotify());
}

class Iotify extends StatefulWidget {
  //const Iotify({Key? key}) : super(key: key);

  @override
  _IotifyState createState() => _IotifyState();
}

var available = 'images/parking.png';
var full = 'images/car.png';
var reserved = 'images/revvv.png';

var spot_1 = available;
var spot_2 = available;
var spot_3 = available;

var availableIcon = Icon(
  Icons.double_arrow_rounded,
  size: 30.0,
  color: Colors.green,
);
var fullIcon = Icon(
  Icons.double_arrow_rounded,
  size: 30.0,
  color: Colors.red,
);
var reservedIcon = Icon(
  Icons.double_arrow_rounded,
  size: 30.0,
  color: Colors.blue,
);

var iconS1 = availableIcon;
var iconS2 = availableIcon;
var iconS3 = availableIcon;

String textS1 = 'Tap to Reserve';
String textS2 = 'Tap to Reserve';
String textS3 = 'Tap to Reserve';

class _IotifyState extends State<Iotify> {
  void reserve1() async {
    var payload;

    payload = {'Spot_1': 'R', 'Spot_2': globalS2, 'Spot_3': globalS3};

    var response = await http.post(getDataUrl, body: payload);

    print(response.body);
  }

  void reserve2() async {
    var payload;

    payload = {'Spot_1': globalS1, 'Spot_2': 'R', 'Spot_3': globalS3};

    var response = await http.post(getDataUrl, body: payload);

    print(response.body);
  }

  void reserve3() async {
    var payload;

    payload = {'Spot_1': globalS1, 'Spot_2': globalS2, 'Spot_3': 'R'};

    var response = await http.post(getDataUrl, body: payload);

    print(response.body);
  }

  void cancle1() async {
    var payload;

    payload = {'Spot_1': 'E', 'Spot_2': globalS2, 'Spot_3': globalS3};

    var response = await http.post(getDataUrl, body: payload);

    print(response.body);
  }

  void cancle2() async {
    var payload;

    payload = {'Spot_1': globalS1, 'Spot_2': 'E', 'Spot_3': globalS3};

    var response = await http.post(getDataUrl, body: payload);

    print(response.body);
  }

  void cancle3() async {
    var payload;

    payload = {'Spot_1': globalS1, 'Spot_2': globalS2, 'Spot_3': 'E'};

    var response = await http.post(getDataUrl, body: payload);

    print(response.body);
  }

  void refresh() async {
    var data;
    var response = await http.get(getDataUrl);
    if (response.statusCode == 200) {
      var decodedData = jsonDecode(response.body);
      data = decodedData;
      print(response.body);
    } else
      print('Error getting data');
    setState(() {
      if (data['spot_1'] == 'E') {
        spot_1 = available;
        iconS1 = availableIcon;
        textS1 = 'Tap To Reserve';
        globalS1 = 'E';
      } else if (data['spot_1'] == 'F') {
        spot_1 = full;
        iconS1 = fullIcon;
        textS1 = 'Full';
        globalS1 = 'F';
      } else if (data['spot_1'] == 'R') {
        spot_1 = reserved;
        iconS1 = reservedIcon;
        textS1 = 'Long press to Undo';
        globalS1 = 'R';
      }

      if (data['spot_2'] == 'E') {
        spot_2 = available;
        iconS2 = availableIcon;
        textS2 = 'Tap To Reserve';
        globalS2 = 'E';
      } else if (data['spot_2'] == 'F') {
        spot_2 = full;
        iconS2 = fullIcon;
        textS2 = 'Full';
        globalS2 = 'F';
      } else if (data['spot_2'] == 'R') {
        spot_2 = reserved;
        iconS2 = reservedIcon;
        textS2 = 'Long press to Undo';
        globalS2 = 'R';
      }

      if (data['spot_3'] == 'E') {
        spot_3 = available;
        textS3 = 'Tap To Reserve';
        iconS3 = availableIcon;
        globalS3 = 'E';
      } else if (data['spot_3'] == 'F') {
        spot_3 = full;
        iconS3 = fullIcon;
        textS3 = 'Full';
        globalS3 = 'F';
      } else if (data['spot_3'] == 'R') {
        spot_3 = reserved;
        iconS3 = reservedIcon;
        textS3 = 'Long press to Undo';
        globalS3 = 'R';
        print('----------------'+data['spot_3']);
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData.dark().copyWith(primaryColor: Color(0xFFd9a554)),
      //scaffoldBackgroundColor: Color(0xFF0a0d22)),
      home: Scaffold(
        backgroundColor: Color(0xFF181818),
        appBar: AppBar(
          title: Text('Parking Space'),
        ),
        body: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Expanded(
              flex: 3,
              child: Container(
                padding: EdgeInsets.all(20.0),
                margin: EdgeInsets.all(30.0),
                decoration: BoxDecoration(
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black54,
                        blurRadius: 10.0, // soften the shadow
                        spreadRadius: 5.0, //extend the shadow
                        offset: Offset(
                          10.0, // Move to right 10  horizontally
                          10.0, // Move to bottom 10 Vertically
                        ),
                      ),
                    ],
                    color: Color(0xFF212121),
                    borderRadius: BorderRadius.circular(20.0)),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Column(
                      mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        Image.asset(
                          spot_1,
                          scale: 3,
                        ),
                        SizedBox(
                          height: 35.0,
                        ),
                        Image.asset(
                          spot_2,
                          scale: 3,
                        ),
                        SizedBox(
                          height: 35.0,
                        ),
                        Image.asset(
                          spot_3,
                          scale: 3,
                        ),
                      ],
                    ),
                    Column(
                      mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        iconS1,
                        SizedBox(
                          height: 1.0,
                        ),
                        iconS2,
                        SizedBox(
                          height: 1.0,
                        ),
                        iconS3,
                      ],
                    ),
                    SizedBox(
                      width: 15,
                    ),
                    Column(
                      mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        TextButton(
                          onLongPress: cancle1,
                          onPressed: reserve1,
                          child: Text(
                            textS1,
                            style: TextStyle(color: Colors.white),
                          ),
                        ),
                        SizedBox(
                          height: 40.0,
                        ),
                        TextButton(
                          onLongPress: cancle2,
                          onPressed: reserve2,
                          child: Text(
                            textS2,
                            style: TextStyle(color: Colors.white),
                          ),
                        ),
                        SizedBox(
                          height: 40.0,
                        ),
                        TextButton(
                          onLongPress: cancle3,
                          onPressed: reserve3,
                          child: Text(
                            textS3,
                            style: TextStyle(color: Colors.white),
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            ),
            SizedBox(
              height: 60.0,
            ),
            //--> Refresh
            Container(
              padding: EdgeInsets.all(30.0),
              margin: EdgeInsets.all(30.0),
              decoration: BoxDecoration(
                boxShadow: [
                  BoxShadow(
                    color: Colors.black54,
                    blurRadius: 7.0, // soften the shadow
                    spreadRadius: 3.0, //extend the shadow
                    offset: Offset(
                      6.0, // Move to right 10  horizontally
                      6.0, // Move to bottom 10 Vertically
                    ),
                  ),
                ],
                color: Color(0xFF212121),
                borderRadius: BorderRadius.circular(20.0),
              ),
              child: TextButton(
                onPressed: refresh,
                child: Icon(
                  Icons.refresh,
                  size: 50.0,
                  color: Color(0xFFd9a554),
                ),
              ),
            ),
            SizedBox(
              height: 60.0,
            ),
          ],
        ),
      ),
    );
  }
}
